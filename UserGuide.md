# Forge Master Stats Overlay - User Guide

## Getting Started

### First Time Setup
1. Install the app
2. Open the app and tap **Start Overlay** on the Scan tab
3. Grant **overlay permission** when prompted (allows the scan button to appear over other apps)
4. Grant **screen capture permission** when prompted (allows reading item stats)

---

## Features

### 🔍 Scanning Items

The scan feature shows you how good each stat roll is compared to the maximum possible value.

**How to use:**
1. In Forge Master, open any item to see its stats
2. Tap the **SCAN** button (green, top-right of screen)
3. Colored percentages appear next to each stat:
   - 🟢 **Green (90%+)** = Excellent roll, keep it!
   - 🟡 **Yellow (60-89%)** = Decent roll
   - 🔴 **Red (below 60%)** = Poor roll, consider replacing
4. Tap **CLEAR** (red button) to remove the overlay

**Example:** If an item shows "+9.6% Critical Chance" and the max is 12%, the overlay shows **80%** in yellow.

---

### ⚖️ Comparing Items

When Forge Master shows you a comparison between your equipped item and a new item, you can get a detailed breakdown.

**How to use:**
1. In Forge Master, pick up a new item so it shows the comparison popup
2. Tap **SCAN** to detect both items
3. Tap **COMPARE** (blue button)
4. A detailed overlay shows:
   - All your current total stats
   - What each stat becomes if you equip the new item
   - The change for each stat (green = better, red = worse)
5. Tap **EQUIP ITEM** to equip, or **CANCEL** to close

**Note:** For accurate comparisons, import your stats first (see below).

---

### 📥 Importing Your Stats

Import your total stats directly from your Forge Master profile instead of typing them manually.

**How to use:**
1. In the app, go to the **Import** tab
2. Tap **Start Import Overlay**
3. In Forge Master, open your player profile (shows all your combined stats)
4. Tap the **IMPORT** button (purple)
5. A confirmation popup shows detected stats
6. **Scroll down** in Forge Master to reveal more stats
7. Tap **IMPORT** again to add them
8. When all stats are captured, tap **SAVE**

**Tips:**
- Stats not detected are automatically set to 0%
- You can tap **MORE** to close the popup and scroll, then **IMPORT** again
- The popup stays at the top so you can see the game below

---

### 📊 My Stats Tab

View and manually edit your total stats.

- Stats are automatically updated when you use **Import**
- You can also type values manually
- Tap **Save Stats** to store changes
- These values are used for the **Compare** feature

---

### 🐕 Pets Live Scanning

Live scanning refreshes the scan automatically once per second, making it easy to bulk check pets without tapping SCAN each time.

**How to use:**
1. Tap **Start Overlay** on the Scan tab
2. Enable **Live Scan** mode on the overlay
3. Browse through your pets in Forge Master — stats update automatically
4. Disable Live Scan or tap **CLEAR** when you're done

**Tip:** Live scanning only captures while the toggle is active, so it won't drain battery when you don't need it.

---

### ⚔️ Skill War Points Calculator

Estimates the war points you'll earn from spending skill tokens on a Ghost Town dungeon summon, based on the rarity probabilities for your chosen level.

**How to use:**
1. Go to the **Calculators** tab
2. Tap **Start Overlay** to open the Skill War Points panel
3. Tap the **level selector** to choose your Ghost Town dungeon level (levels 1-1 through 10-10 are all supported)
4. Enter your **token count** and **cost per summon**
5. The estimated war points total is calculated instantly

**Note:** Calculations assume 5 skills per summon and assign points based on rarity (Common = 50, Rare = 75, Epic = 100, Legendary = 125, Ultimate = 150, Mythic = 175).

---

### 👥 Clan Admin

A dedicated tab for clan management tools, including the Weekly Points Scanner.

#### 📋 Weekly Points Scanner

Automatically reads your clan's in-game weekly leaderboard and extracts each member's name and score — no manual data entry needed.

**First time setup:**
The scanner uses a three-step permission flow on first use:
1. Tap **Grant Overlay** — allows the scanner panel to appear on screen
2. Tap **Grant Screen Capture** — allows the app to read the leaderboard
3. Tap **Start Scanning** — begins active capture

**How to scan:**
1. Go to the **Clan Admin** tab and tap **Start Scanner**
2. In Forge Master, open the clan weekly points leaderboard
3. The scanner uses **stillness detection** — it waits for the screen to stop moving before capturing, so scroll slowly and pause between scrolls
4. Member names and scores appear in the panel as they're detected
5. Scroll through the full leaderboard to capture all members — results are accumulated across multiple captures

**Correcting results:**
The game's stylised font can cause occasional OCR misreads. The scanner corrects many of these automatically, but you can also fix them manually:
- Tap any **name or score** in the results list to edit it directly
- Tap the **🗑️ delete icon** to remove an incorrect entry
- Entries with very similar names are automatically merged to avoid duplicates

**Tips:**
- Pause for a moment between scrolls to let stillness detection kick in
- If a member's score looks wrong, check for digit/letter misreads (e.g. S instead of 5, G instead of 6) and correct manually

---

## Overlay Buttons

| Button | Color | Function |
|--------|-------|----------|
| **SCAN** | Green | Capture and analyze item stats |
| **CLEAR** | Red | Remove stat overlay |
| **COMPARE** | Blue | Show detailed comparison |
| **IMPORT** | Purple | Scan profile stats (Import mode) |
| **START SCAN** | Green | Begin clan leaderboard capture |
| **✕** | Grey | Stop the overlay service |

---

## Tips & Tricks

1. **Quick scanning:** You can scan multiple times without clearing — new results replace old ones

2. **Comparison accuracy:** Import your stats first for the most accurate comparison results

3. **OCR issues:** If stats aren't detected correctly, try:
   - Making sure the item popup is fully visible
   - Avoiding chat messages overlapping the item
   - Scanning again

4. **Clan scanning:** Scroll slowly and pause between scrolls — the stillness detector needs a moment of stability to capture cleanly

5. **Battery:** The overlay only captures the screen when you tap a button or when Live Scan is active, so it won't drain battery in the background

---

## Troubleshooting

**"No stats found" message:**
- Make sure an item with stats is visible on screen
- Check that the stats text isn't covered by other UI elements

**Percentages seem wrong:**
- The app compares against maximum possible values for each stat
- Values over 100% are possible if your total exceeds the single-item max

**Buttons not appearing:**
- Check that overlay permission is granted in Settings → Apps → Forge Master Stats Overlay → Display over other apps

**Compare not working:**
- Make sure you have two items visible (equipped + new)
- Try tapping SCAN first, then COMPARE

**Clan scanner not picking up members:**
- Scroll more slowly and pause between scrolls
- Make sure the leaderboard card area is fully visible and not partially off-screen

**Clan scanner showing wrong scores:**
- Use the manual edit feature to correct any misread digits
- Common misreads: S→5, G→6, Q/A→4, B→8, O→0, T→7

---

## Need Help?

If you encounter issues or have suggestions, please reach out through GitHub - https://github.com/ForgeOverlay/FMOverlay/issues.

Happy forging! 🔨
