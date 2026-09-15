# Privacy Policy for Forge Master Companion

**Last updated: 15 September 2026**

Forge Master Companion is a free Android app developed by Bobski as a personal
project. This policy explains what the app does with your data. The short
version: nothing leaves your phone except a small config download, and a bug
report if you choose to send one. Both are explained below.

## Data the app collects

The app has no user accounts and sends no usage data, telemetry, or analytics
anywhere. There is no crash reporting SDK, no advertising SDK, and no
third-party analytics.

The only time information about your device, or anything you write, leaves your
phone is when you open the bug report form. See "Bug reports" below.

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
ML Kit and Tesseract), the text is read out, and the screenshot is discarded.
Captured frames are never saved to your device's storage and are never
transmitted anywhere. Android shows a system dialog the first time the app
uses this permission so you can refuse it.

Google ML Kit's text recognition model is supplied and kept up to date by
Google Play services on your device. The recognition itself runs on your phone.

## Network requests

The app connects to the internet for two things only.

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
- **Internet**: only for the config download and the bug report form described
  above.

## Children

The app is not directed at children. It does not ask anyone for personal
information, including children under 13 (US) or 16 (UK/EU). Please don't
include personal information in bug reports.

## Changes to this policy

If anything changes, I'll update this page and bump the "Last updated" date at
the top.

## Contact

Questions: fmoverlay@gmail.com
