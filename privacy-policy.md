# Privacy Policy for Forge Master Companion

**Last updated: 4 November 2026**

Forge Master Companion is a free Android app developed by Bobski as a personal
project. This policy explains what the app does with your data. The short
version: nothing leaves your phone except a small config download, a bug report
if you choose to send one, exports you choose to send to the Botski Discord
bot, and your scanned profile if you choose to send it to 1vcian.me. All four
are explained below.

## Data the app collects

The app has no user accounts and sends no usage data, telemetry, or analytics
anywhere. There is no crash reporting SDK, no advertising SDK, and no
third-party analytics.

Information about your device, or anything you write, leaves your phone only
when you open the bug report form, when you tap Send to Botski, or when you tap
Send profile. See "Bug reports", "Sending to Botski" and "Sending your profile
to 1vcian.me" below.

## Data stored on your device

The app stores the following on your device only, using Android's standard
SharedPreferences and local files:

- Game-related stats, profiles, and inventory data that you enter or that the
  app reads from your screen.
- Your in-app settings (overlay positions, toggles, UI preferences).
- The time you last sent a bug report, used to space reports out.

This data is sandboxed under Android's normal app-data rules. Uninstalling the
app removes it. None of it is uploaded anywhere.

## Screen capture and OCR

The app uses Android's MediaProjection API to capture screenshots when you
trigger a scan. Each capture is processed in memory by on-device OCR (Google
ML Kit), the text is read out, and the screenshot is discarded.
Captured frames are never saved to your device's storage and are never
transmitted anywhere. Android shows a system dialog the first time the app
uses this permission so you can refuse it.

Google ML Kit's text recognition model is supplied and kept up to date by
Google Play services on your device. The recognition itself runs on your phone.

## Network requests

The app connects to the internet for four things only.

### Game balance values

The app fetches game balance values from a public file on GitHub:

`https://raw.githubusercontent.com/ForgeOverlay/FMOverlay/main/remote_config.json`

The request is read-only and contains no personal information. GitHub, as the
host, will see your device's IP address and a standard User-Agent string, the
same as if your browser fetched the file. GitHub's privacy policy applies to
that interaction: https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement

The response is cached locally for one hour before being refreshed.

### Bug reports

Nothing is sent unless you open **Settings → Report a bug**. That screen loads
a form hosted by Tally (tally.so) inside the app.

**When the form opens**, it arrives with these details already filled in, so
Tally receives them at that point:

- The app version.
- Your Android version.
- Your device's manufacturer and model.

**When you tap Send report**, the form also sends:

- What you type: the issue title, type of request, priority and steps to
  reproduce, plus feature details and additional comments or links if you fill
  them in.
- Your email address, only if you choose to enter one. It is used only to reply
  to you about your report.
- Any screenshots you choose to attach. A screenshot shows whatever was on your
  screen, which may include your in-game name, so check it before attaching.

The form does not include your name, any account details, or the stats stored in
the app.

Tally (Tally BV, Belgium) stores submissions on servers in the European Union.
Tally's privacy notice: https://tally.so/help/privacy-policy

To keep track of reports, each submission is copied automatically to my private
project board on Trello (Atlassian) using Make (make.com), an automation service.
Their privacy policies: https://www.atlassian.com/legal/privacy-policy and
https://www.make.com/en/privacy-notice

The form uses Google reCAPTCHA to block spam, so Google processes information
such as your IP address and browser details. Google's privacy policy:
https://policies.google.com/privacy

As with any web page, Tally and Google also see your IP address and a standard
User-Agent string when the form loads.

Reports are used only to fix bugs and consider feature requests. To have a
report you sent deleted, email the address at the bottom of this page with
roughly when you sent it and its title.

### Sending to Botski

Botski is a Discord bot that tracks clan resources. Nothing is sent unless you
link the app to it (run `/link` in Discord, then enter the code in the app) and
then tap **Send to Botski**.

**What is sent:** exactly what the matching Copy button would put on your
clipboard: your clan's war bonuses, your tech bonuses, or your resource counts.
Nothing else from the app, and nothing about your device.

**How:** the export is encrypted on your phone so that only Botski can read it,
then passed through a small relay I run on Cloudflare Workers. The relay holds the
encrypted export until Botski collects it, which it does within about a minute,
and deletes it then or after 15 minutes at the latest. It keeps a random mailbox
number for your link and a scrambled form of a random code your phone made; it
never learns your Discord name or ID. It briefly sees your Discord server's name
while you link (until the code is used, 10 minutes at most), and Botski's short
note about each import ("Imported resources: 6 lines"), which it deletes once the
app shows it, or after 15 minutes. A link unused for 90 days is deleted.

Cloudflare, as the host, sees your IP address and a standard User-Agent string.
Cloudflare's privacy policy: https://www.cloudflare.com/privacypolicy/

What Botski does with an import, such as showing your resources to your clan, is
decided by the Discord server it is in. To stop sending, tap Disconnect in
Settings or run `/unlink` in Discord.

### Sending your profile to 1vcian.me

1vcian.me is a Forge Master fan site run by someone else, where you can keep a
profile of your build. Nothing is sent unless you make a key on that site
(Profile, Settings, Linked apps), add it in the app's Settings, and then tap
**Send profile**. The app shows what it will send and asks first.

**What is sent:** your key, and what the app has scanned: your active pets
(which pet, level and bonus stats), your mount (which mount and its level), the
levels of your equipped skills, your forge level, and the clockwinder, skill
ticket and egg shell counts you saved. Nothing else from the app, and nothing
about your device.

**How:** over an encrypted (HTTPS) connection to the site's database, hosted by
Supabase. The site shows you the update and you choose whether to apply it.
Your key is stored encrypted on your phone and is never included in backups.

The site's owner and Supabase, as the host, see your IP address and a standard
User-Agent string. What the site keeps and shows is decided by 1vcian.me.
Supabase's privacy policy: https://supabase.com/privacy

To stop sending, tap Remove key in Settings, or revoke the key on the site.

### Links that open your browser

Some buttons, such as the Ko-fi support link, open a website in your browser.
The app sends nothing itself; that website's own privacy policy applies.

## Permissions and why they exist

- **Display over other apps** (`SYSTEM_ALERT_WINDOW`): to show the overlay UI
  on top of the game.
- **Foreground service** and **media projection**: to keep the overlay running
  and to capture the screen for OCR.
- **Post notifications**: to show the persistent notification Android requires
  while the foreground service is active.
- **Internet**: only for the config download, the bug report form, Send to
  Botski and Send profile, described above.

## Children

The app is not directed at children. It does not ask anyone for personal
information, including children under 13 (US) or 16 (UK/EU). Please don't
include personal information in bug reports.

## Changes to this policy

If anything changes, I'll update this page and bump the "Last updated" date at
the top.

## Contact

Questions: fmoverlay@gmail.com
