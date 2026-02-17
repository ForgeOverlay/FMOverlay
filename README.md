# Forge Master Stats Overlay

A companion Android app for Forge Master that helps you evaluate item stats, track clan performance, and calculate skill war points — all in real time, entirely offline.

---

## Features

### 📊 Scan Items
Scan any item in Forge Master to see how good each stat roll is as a percentage of the maximum possible value.

- **Green (90%+)** — Excellent roll
- **Yellow (60–89%)** — Good roll
- **Red (<60%)** — Poor roll

### 🔄 Compare Items
When viewing an item comparison screen (equipped vs new item), tap **COMPARE** to see a detailed breakdown of how equipping the new item would affect your total stats.

### 📥 Import Stats
Import your current total stats directly from your player profile in-game. Supports multi-scroll importing to capture all stats across the full profile page.

### Importing Your Stats
1. Go to the **Import** tab in the app
2. Tap **Start Import Overlay**
3. In Forge Master, open your player profile
4. Tap **IMPORT** to scan visible stats
5. Scroll down in the game to reveal more stats
6. Tap **IMPORT** again to add them
7. Tap **SAVE** when done

### 📈 My Stats
View and manually edit your stored total stats. Used by the comparison feature to calculate the net effect of any item swap.

### 🐕 Pets Live Scanning
Auto-refreshes the scan every second so you can bulk-check pets quickly without repeatedly tapping SCAN.

### ⚔️ Skill War Points Calculator
Estimates the war points you'll earn from a skill token summon. Select your Ghost Town dungeon level (all 100 levels across 10 worlds supported), enter your token count and cost per summon, and get an instant estimated points total based on rarity probabilities.

### 👥 Clan Admin
A dedicated tab for clan management tools.

**Weekly Points Scanner** scans the in-game clan weekly points leaderboard and extracts member names and scores automatically. Features include:

- Stillness detection to prevent motion blur during scrolling
- Cross-frame voting to stabilise OCR readings across multiple captures
- Flexible name/score matching using proximity-based pairing
- Automatic correction of common OCR misreads caused by the game's stylised font
- Editable results with manual correction and delete options
- Three-step permission flow: grant overlay → grant screen capture → start scanning

---

## Installation

1. Download the APK from the [Releases](https://github.com/ForgeOverlay/FMOverlay/releases) page or install via Firebase App Distribution
2. Grant **overlay permission** when prompted
3. Grant **screen capture permission** when first scanning

---

## Supported Stats

| Stat | Max Value |
|---|---|
| Critical Chance | 12% |
| Critical Damage | 100% |
| Attack Speed | 40% |
| Double Chance | 40% |
| Damage | 15% |
| Skill Damage | 30% |
| Ranged Damage | 15% |
| Melee Damage | 50% |
| Block Chance | 5% |
| Lifesteal | 20% |
| Health Regen | 6% |
| Skill Cooldown | 7% |
| Health | 15% |

---

## Supported Item Tiers

Primitive · Medieval · Early-Modern · Modern · Space · Interstellar · Multiverse · Quantum · Underworld · Divine

---

## Requirements

- Android 8.0 (API 26) or higher
- Overlay permission
- Screen capture permission

---

## Privacy

This app:
- Does **not** collect any personal data
- Does **not** require internet access
- Only captures the screen when you tap SCAN / IMPORT / START SCAN
- Stores all data locally on your device only

---

## Support Development

If you find this app useful, consider supporting development via Ko-fi!
