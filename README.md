# NST Medivia BOT

NST is a bot for Medivia designed to automate mana training and rune creation.

The program utilizes the client's image recognition, minimizing detection issues related to software anti-bot measures. However, please note that **using the bot may result in a ban if a GM investigates and observes suspicious activity, such as mana refills during play**.

| **Table of Contents**                 |
| ------------------------------------- |
| [Getting Started](#getting-started)   |
| [Usage](#usage)                       |
| [Important Notes](#important-notes) ❗ |
| [Contributions](#contributions)       |

## Getting Started

1. Go to the [Releases](https://github.com/nebelorz/NST-medivia-bot/releases) section and download the latest release.
2. Extract the downloaded .zip file (otherwise, your antivirus might trigger a false positive).
3. Run the .exe file to start the program.

## Usage

![NST Medivia BOT](https://github.com/nebelorz/NST-medivia-bot/assets/65920053/4a0924b6-9247-44fb-b25c-45a106e1447a)

Setting up the NST Medivia BOT is easy. Just follow these steps:

1. **Spell**: Choose the spell your character will cast in the in-game chat. If it requires a blank rune, check the "needs blank rune" option.

2. **Food**: Pick a food item from the list (hams, fish, or brown mushrooms).

   - ❗ *Note: The BOT detects full item stacks only, like 5 or more hams.*

3. **Boost**: Select an item to boost mana regeneration.

4. **Settings**: Customize the BOT's behavior:

   - **Focus Interval**: Specify how often the Medivia client should be in focus (e.g., every 2 minutes).
   - **Minimize**: Enable this checkbox to minimize the client after casting.
   - **Logout if No Supplies**: Logout when no blank runes, food or boost items remain.

## Important Notes
- NST uses image recognition, so you'll need to setup your resolution on 1920x1080 and show:
  - HP/MANA bars
  - Inventory (w/ empty ring slot)
  - Food to use
 
    ![medivia-settings-to-show](https://github.com/nebelorz/NST-medivia-bot/assets/65920053/f7d53ce8-606c-4e01-af55-e95adf2e4b56)

- NST will detect and bring to focus any program with "Medivia" in its name. Ensure no unrelated program shares this name (e.g., Google Chrome while visiting Medivia-related websites).

- The BOT will only cast the spell when the character has more than half of their total mana. This threshold is not configurable. It will continue casting until mana falls below half (e.g., with 300/300 mana, casting stops at 150/300). The BOT will then use food, boost items, and wait until the next check.

- Certain food items (like "Hams") are detected only when the image matches a stack's maximum amount (e.g., stacks of 5 or more in case of hams).

- If "minimize" is enabled, the game will remain minimized until the next time check, useful if you're using your PC to watch some Youtube.

- Enabling "logout if no supplies" will prompt the character to log out if no supplies (blank runes/food/boost items) are left. The "force" option is used for this logout.

## Contributions

Contributions to the project are welcome. Feel free to open pull requests or issues if you would like to contribute.
