# Forge Master Stats Overlay

A companion Android app for Forge Master that helps you evaluate item stats at a glance.

## Features

### 📊 Scan Items
Scan any item in Forge Master to see how good each stat roll is as a percentage of the maximum possible value.

- **Green (90%+)**: Excellent roll
- **Yellow (60-89%)**: Good roll  
- **Red (<60%)**: Poor roll

### 🔄 Compare Items
When viewing an item comparison screen (equipped vs new item), tap COMPARE to see a detailed breakdown of how equipping the new item would affect your total stats.

### 📥 Import Stats
Import your current total stats directly from your player profile:
1. Open your profile in Forge Master
2. Tap IMPORT to scan visible stats
3. Scroll down and tap IMPORT again for more stats
4. Tap SAVE to store your stats

### 📈 My Stats
View and manually edit your total stats. These are used for the comparison feature to show how equipment changes affect your build.

## Installation

1. Download the APK or install via Firebase App Distribution
2. Grant overlay permission when prompted
3. Grant screen capture permission when first scanning

## How to Use

### Scanning Items
1. Open the app and go to the **Scan** tab
2. Tap **Start Overlay**
3. Switch to Forge Master and open any item
4. Tap the **SCAN** button to analyze stats
5. Tap **CLEAR** to remove the overlay

### Comparing Items
1. In Forge Master, open an item comparison (equipped vs new)
2. Tap **SCAN** first to detect both items
3. Tap **COMPARE** to see the full stat breakdown
4. Green stats improve, red stats decrease

### Importing Your Stats
1. Go to the **Import** tab in the app
2. Tap **Start Import Overlay**
3. In Forge Master, open your player profile
4. Tap **IMPORT** to scan visible stats
5. Scroll down in the game to reveal more stats
6. Tap **IMPORT** again to add them
7. Tap **SAVE** when done

## Supported Stats

- Critical Chance (max 12%)
- Critical Damage (max 100%)
- Attack Speed (max 40%)
- Double Chance (max 40%)
- Damage (max 15%)
- Skill Damage (max 30%)
- Ranged Damage (max 15%)
- Melee Damage (max 50%)
- Block Chance (max 5%)
- Lifesteal (max 20%)
- Health Regen (max 6%)
- Skill Cooldown (max 7%)
- Health (max 15%)

## Supported Item Tiers

Primitive, Medieval, Early-Modern, Modern, Space, Interstellar, Multiverse, Quantum, Underworld, Divine

## Requirements

- Android 8.0 (API 26) or higher
- Overlay permission
- Screen capture permission

## Support Development

If you find this app useful, consider supporting development via Ko-fi!

## Privacy

This app:
- Does NOT collect any personal data
- Does NOT require internet access
- Only captures the screen when you tap SCAN/IMPORT
- Stores your stats locally on your device only
