"""Validate remote_config.json against the rules Forge Master Companion's parser uses.

Why this exists: the app parses this file TOLERANTLY. A typo'd key, a number
written as a string, a zero, or a short array is not an error in the app, it is
silently ignored and the compiled default is used instead. So a broken edit looks
like it worked, and every player quietly keeps the old value. This check turns
those silent fallbacks into a red cross on the commit.

Errors (exit 1) are things the app would ignore or fall back from.
Warnings are legal but worth a second look (a missing optional key, say).

The schema below mirrors the app's parsers (RemoteConfigManager.parseJson,
FairyConfig, TechBonusOverrides, BugReportConfig). When the app learns a new
field, add it to SCHEMA here in the same change that publishes it, or this check
will flag it as an unknown key.

Usage: python3 validate_remote_config.py remote_config.json
"""

import json
import math
import os
import re
import sys
from urllib.parse import urlparse

RARITIES = ["Common", "Rare", "Epic", "Legendary", "Ultimate", "Mythic"]

# Keys the app reads from maxStats. Move Speed and Attack Range are read too but
# deliberately not published, so their absence is only a warning.
MAX_STATS_KEYS = [
    "Critical Chance", "Critical Damage", "Attack Speed", "Double Chance", "Damage",
    "Skill Damage", "Ranged Damage", "Melee Damage", "Block Chance", "Lifesteal",
    "Health Regen", "Skill Cooldown", "Health", "Reflect Chance",
    "Move Speed", "Attack Range",
]
MAX_STATS_UNPUBLISHED_OK = {"Move Speed", "Attack Range"}

FAIRY_IDS = ["mira", "tira", "lora"]
FAIRY_FIELDS = ["ratePerLevel", "sourceStep", "cap"]

TECH_TIERS = 5          # TechBonusCatalog.TIERS
SKILL_MAX_LEVEL = 100   # SkillCombatData.MAX_LEVEL


class Report:
    def __init__(self, text):
        self.errors = []
        self.warnings = []
        self.lines = text.splitlines()

    def _line_of(self, path):
        # Best effort: the line where the last named key in the path first appears.
        keys = re.findall(r'"([^"]+)"|([A-Za-z_][A-Za-z0-9_]*)', path)
        names = [a or b for a, b in keys if (a or b)]
        if not names:
            return None
        needle = '"%s"' % names[-1]
        for i, line in enumerate(self.lines, start=1):
            if needle in line:
                return i
        return None

    def error(self, path, msg):
        self.errors.append((path, msg, self._line_of(path)))

    def warn(self, path, msg):
        self.warnings.append((path, msg, self._line_of(path)))


def is_int(v):
    return isinstance(v, int) and not isinstance(v, bool)


def is_number(v):
    return (isinstance(v, (int, float)) and not isinstance(v, bool)
            and math.isfinite(v))


def describe(v):
    if isinstance(v, str):
        return 'the text "%s"' % v
    if isinstance(v, bool):
        return "true" if v else "false"
    if v is None:
        return "null"
    return json.dumps(v)


def positive_int(r, path, v):
    if not is_int(v) or v <= 0:
        r.error(path, "must be a whole number above 0, got %s" % describe(v))


def positive_number(r, path, v):
    if not is_number(v) or v <= 0:
        r.error(path, "must be a number above 0, got %s" % describe(v))


def non_negative_number(r, path, v):
    if not is_number(v) or v < 0:
        r.error(path, "must be a number, 0 or more, got %s" % describe(v))


def expect_object(r, path, v):
    if not isinstance(v, dict):
        r.error(path, "must be an object { ... }, got %s" % describe(v))
        return False
    return True


def unknown_keys(r, path, obj, allowed):
    for k in obj:
        if k not in allowed:
            r.error('%s."%s"' % (path, k),
                    "unknown key, the app ignores it (typo? allowed: %s)" % ", ".join(allowed))


# ---- per-field checks ---------------------------------------------------------

def check_rarity_map(r, path, v):
    if not expect_object(r, path, v):
        return
    unknown_keys(r, path, v, RARITIES)
    for rarity in RARITIES:
        if rarity not in v:
            r.error('%s."%s"' % (path, rarity), "missing, the app would use its compiled default")
        else:
            positive_int(r, '%s."%s"' % (path, rarity), v[rarity])


def check_max_stats(r, path, v):
    if not expect_object(r, path, v):
        return
    unknown_keys(r, path, v, MAX_STATS_KEYS)
    for key in MAX_STATS_KEYS:
        if key in v:
            positive_number(r, '%s."%s"' % (path, key), v[key])
        elif key not in MAX_STATS_UNPUBLISHED_OK:
            r.warn('%s."%s"' % (path, key), "missing, the app will use its compiled default")


def check_announcement(r, path, v):
    if not expect_object(r, path, v):
        return
    unknown_keys(r, path, v, ["id", "title", "body"])
    ann_id = v.get("id", 0)
    if not is_int(ann_id) or ann_id < 0:
        r.error(path + ".id", "must be a whole number, 0 or more, got %s" % describe(ann_id))
        return
    title, body = v.get("title", ""), v.get("body", "")
    for name, text in (("title", title), ("body", body)):
        if not isinstance(text, str):
            r.error("%s.%s" % (path, name), "must be text in quotes, got %s" % describe(text))
    if ann_id > 0 and (not isinstance(title, str) or not title.strip()
                       or not isinstance(body, str) or not body.strip()):
        r.error(path, "id is %d but title or body is blank, so the popup will never show" % ann_id)


def check_fairies(r, path, v):
    if not expect_object(r, path, v):
        return
    unknown_keys(r, path, v, FAIRY_IDS)
    for fid, fv in v.items():
        if fid not in FAIRY_IDS:
            continue
        fpath = "%s.%s" % (path, fid)
        if not expect_object(r, fpath, fv):
            continue
        unknown_keys(r, fpath, fv, FAIRY_FIELDS)
        for field in FAIRY_FIELDS:
            if field in fv:
                positive_number(r, "%s.%s" % (fpath, field), fv[field])
            else:
                r.warn("%s.%s" % (fpath, field), "missing, the app will use its compiled default")


def check_tech_overrides(r, path, v):
    if not expect_object(r, path, v):
        return
    allowed = ["tierSteps", "subLevelsPerTier", "popupText", "aliases"]
    for line_id, lv in v.items():
        lpath = "%s.%s" % (path, line_id)
        if not expect_object(r, lpath, lv):
            continue
        unknown_keys(r, lpath, lv, allowed)
        if "tierSteps" in lv:
            steps = lv["tierSteps"]
            if not isinstance(steps, list) or len(steps) != TECH_TIERS:
                r.error(lpath + ".tierSteps",
                        "must be a list of exactly %d whole numbers, the app ignores anything else" % TECH_TIERS)
            else:
                for i, s in enumerate(steps):
                    positive_int(r, "%s.tierSteps[%d]" % (lpath, i), s)
        if "subLevelsPerTier" in lv:
            positive_int(r, lpath + ".subLevelsPerTier", lv["subLevelsPerTier"])
        if "popupText" in lv and (not isinstance(lv["popupText"], str) or not lv["popupText"].strip()):
            r.error(lpath + ".popupText", "must be non-blank text, got %s" % describe(lv["popupText"]))
        if "aliases" in lv:
            al = lv["aliases"]
            if not isinstance(al, list) or not all(isinstance(a, str) and a.strip() for a in al):
                r.error(lpath + ".aliases", "must be a list of non-blank texts")
    if v:
        r.warn(path, "line ids can't be checked here (the catalog lives in the app); "
                     "an unknown id is ignored by the app, so double-check the spelling")


def check_skill_overrides(r, path, v):
    if not expect_object(r, path, v):
        return
    numbers = ["cooldown", "activeDuration", "hitCount", "hitInterval", "hitDelay"]
    arrays = ["damagePerLevel", "healthPerLevel"]
    allowed = numbers + arrays + ["libraryValueIsPerHit"]
    for skill_id, sv in v.items():
        spath = "%s.%s" % (path, skill_id)
        if not expect_object(r, spath, sv):
            continue
        unknown_keys(r, spath, sv, allowed)
        for n in numbers:
            if n in sv:
                non_negative_number(r, "%s.%s" % (spath, n), sv[n])
        if "libraryValueIsPerHit" in sv and not isinstance(sv["libraryValueIsPerHit"], bool):
            r.error(spath + ".libraryValueIsPerHit", "must be true or false without quotes")
        for a in arrays:
            if a in sv:
                arr = sv[a]
                if (not isinstance(arr, list) or len(arr) != SKILL_MAX_LEVEL
                        or not all(is_number(x) for x in arr)):
                    r.error("%s.%s" % (spath, a),
                            "must be a list of exactly %d numbers, the app ignores anything else" % SKILL_MAX_LEVEL)
    if v:
        r.warn(path, "skill ids can't be checked here (the list lives in the app); "
                     "an unknown id is ignored by the app, so double-check the spelling")


def check_bug_report(r, path, v):
    if not expect_object(r, path, v):
        return
    unknown_keys(r, path, v, ["enabled", "formUrl"])
    if "enabled" in v and not isinstance(v["enabled"], bool):
        r.error(path + ".enabled", "must be true or false without quotes, got %s" % describe(v["enabled"]))
    if "formUrl" in v:
        url = v["formUrl"]
        ok = False
        if isinstance(url, str) and url == url.strip():
            parsed = urlparse(url)
            ok = parsed.scheme == "https" and bool(parsed.netloc) and " " not in url
        if not ok:
            r.error(path + ".formUrl", "must be a full https:// link, got %s" % describe(url))


SCHEMA = {
    "version": positive_int,
    "announcement": check_announcement,
    "skillWarPoints": check_rarity_map,
    "mountWarPoints": check_rarity_map,
    "mergePetWarPoints": positive_int,
    "mergeMountWarPoints": positive_int,
    "maxStats": check_max_stats,
    "eggSummonCost": positive_int,
    "skillMaxCost": positive_int,
    "mountSummonBaseCost": positive_int,
    "baseCritMultiplier": positive_number,
    "pvpHpMultiplier": positive_number,
    "rangedHeadStartSeconds": positive_number,
    "pvpTimeLimitSeconds": positive_number,
    "fairies": check_fairies,
    "fairyMaxLevel": positive_int,
    "techBonusOverrides": check_tech_overrides,
    "skill_combat_overrides": check_skill_overrides,
    "bugReport": check_bug_report,
}
OPTIONAL_TOP_LEVEL = {"announcement", "techBonusOverrides", "skill_combat_overrides"}


def reject_duplicates(pairs):
    seen = {}
    for k, v in pairs:
        if k in seen:
            raise ValueError('the key "%s" appears twice in the same object; '
                             "only the last one would count" % k)
        seen[k] = v
    return seen


def validate(text):
    r = Report(text)
    try:
        data = json.loads(text, object_pairs_hook=reject_duplicates)
    except json.JSONDecodeError as e:
        r.errors.append(("(file)", "not valid JSON: %s (line %d, column %d). "
                         "Common causes: a missing or extra comma, or a missing quote"
                         % (e.msg, e.lineno, e.colno), e.lineno))
        return r
    except ValueError as e:
        r.errors.append(("(file)", str(e), None))
        return r
    if not isinstance(data, dict):
        r.errors.append(("(file)", "the whole file must be one object { ... }", 1))
        return r
    unknown_keys(r, "(top level)", data, list(SCHEMA))
    for key, check in SCHEMA.items():
        if key in data:
            check(r, key, data[key])
        elif key not in OPTIONAL_TOP_LEVEL:
            r.warn(key, "missing, the app will use its compiled default")
    return r


def main():
    if len(sys.argv) != 2:
        print("usage: validate_remote_config.py remote_config.json")
        return 2
    path = sys.argv[1]
    with open(path, "rb") as f:
        raw = f.read()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as e:
        print("::error file=%s::not UTF-8 text: %s" % (path, e))
        return 1
    if text.startswith("﻿"):
        text = text[1:]

    r = validate(text)
    in_actions = os.environ.get("GITHUB_ACTIONS") == "true"

    def emit(kind, items):
        for p, msg, line in items:
            if in_actions:
                loc = "file=%s" % path + (",line=%d" % line if line else "")
                print("::%s %s,title=%s::%s" % (kind, loc, p, msg))
            else:
                print("%s  %s%s: %s" % (kind.upper(), p, " (line %d)" % line if line else "", msg))

    emit("error", r.errors)
    emit("warning", r.warnings)
    verdict = ("FAILED: %d error(s), %d warning(s)" % (len(r.errors), len(r.warnings))
               if r.errors else "OK: no errors, %d warning(s)" % len(r.warnings))
    print(verdict)

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write("## remote_config.json\n\n**%s**\n\n" % verdict)
            for kind, items in (("Error", r.errors), ("Warning", r.warnings)):
                for p, msg, line in items:
                    f.write("- %s `%s`%s: %s\n" % (kind, p, " (line %d)" % line if line else "", msg))
    return 1 if r.errors else 0


if __name__ == "__main__":
    sys.exit(main())
