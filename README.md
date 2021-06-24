# NST 📌
*Welcome to Nebel's Slacking Tools (NST), I encourage you to take a look at the readme before getting in with the software, I'll keep it short, I promise :)*

The NST are developed to enhance your mana training in a convenient way, helping you not missing any single mana point.

Completely built with [Python](https://www.python.org/) and using image recognition and mouse/keyboard inputs, it's not detectable unless a GM catches you in-situ.

# INSTRUCTIONS 📋
_Download ZIP, extract all the files in the same folder and execute "NST version.exe"._
 

# HOW TO USE ⚙️
>#### *HOTKEYS* ⏯
To start NST you can press 'Home' or the start button.

To stop NST you can press 'End' or the stop button.

>#### *SPELL* 🎆
The spell box is your input spell to the game, it will be casted always in the default channel.

The "needs blank rune" checkbox will check for blank runes at your inventory, if none found, an error pops.

>#### *HAND* 🖐
Basically in which hand you want to get the blank rune, by default left, if it's not empty, an error pops.

>#### *CHECK* ⏳
The check entry is the time in which it will check again if you have enough mana and resources to repeat the process, always must be numbers and the time in seconds,
by default 300 seconds (5 minutes). Minimize checkbox to minimize when the checking is done.

>#### *FOOD* 🥓
Select which food you want to eat, it will check if you have it in your inventory and right-click 4 times on it. If none found, an error pops.

>#### *BOOST* 💎
Selected item will be refilled/used every time the check occurs

---

# IMPORTANT NOTES 🟥
>[SPELL]
 
will be cast ONLY if you got more than half mana, not configurable at X manapoints.

will be casted many times until you get less than half mana. Example: 300/300 mana, you will cast the spell until 150/300 or less, then will wait the CHECK time.
 
when "needs blank rune" is checked, the selected hand always must be EMPTY.

>[CHECK]

 when "minimize" is checked, the game will be minimized after the check.

>[FOOD]
 
Hams are only detected if it's a stack of 5 or more items.
Meats are only detected if it's a stack of 10 or more items.
