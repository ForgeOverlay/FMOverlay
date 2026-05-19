# Privacy Policy for Forge Master Companion

**Last updated: 19 May 2026**

Forge Master Companion is a free Android app developed by Bobski as a personal
project. This policy explains what the app does with your data. The short
version: nothing leaves your phone, with one minor exception explained below.

## Data the app collects

None. The app has no user accounts, asks for no personal information, and sends
no usage data, telemetry, or analytics anywhere. There is no crash reporting
SDK, no advertising SDK, and no third-party analytics.

## Data stored on your device

The app stores the following on your device only, using Android's standard
SharedPreferences and local files:

- Game-related stats, profiles, and inventory data that you enter or that the
  app reads from your screen.
- Your in-app settings (overlay positions, toggles, UI preferences).

This data is sandboxed under Android's normal app-data rules. Uninstalling the
app removes it. None of it is uploaded anywhere.

## Screen capture and OCR

The app uses Android's MediaProjection API to capture screenshots when you
trigger a scan. Each capture is processed in memory by on-device OCR (Google
ML Kit and Tesseract), the text is read out, and the screenshot is discarded.
Captured frames are never saved to your device's storage and are never
transmitted anywhere. Android shows a system dialog the first time the app
uses this permission so you can refuse it.

## The one network request

The app makes a single outbound request to fetch game balance values from a
public file on GitHub:

`https://raw.githubusercontent.com/ForgeOverlay/FMOverlay/main/remote_config.json`

The request is read-only and contains no personal information. GitHub, as the
host, will see your device's IP address and a standard User-Agent string — the
same as if your browser fetched the file. GitHub's privacy policy applies to
that interaction: https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement

The response is cached locally for one hour before being refreshed.

## Permissions and why they exist

- **Display over other apps** (`SYSTEM_ALERT_WINDOW`) — to show the overlay UI
  on top of the game.
- **Foreground service** and **media projection** — to keep the overlay running
  and to capture the screen for OCR.
- **Post notifications** — to show the persistent notification Android requires
  while the foreground service is active.
- **Internet** — only for the GitHub config request described above.

## Children

The app is not directed at children. It collects no personal information from
anyone, including children under 13 (US) or 16 (UK/EU).

## Changes to this policy

If anything changes, I'll update this page and bump the "Last updated" date at
the top.

## Contact

Questions: fmoverlay@gmail.com
