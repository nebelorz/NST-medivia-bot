# NST Medivia BOT
NST is a bot for Medivia which will take care of raising your magic level and/or making runes while making sure your character is fed and using items to boost mana if necessary.
Also, if selected, your character will be logged out after supplies run out.

## Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- ❗[Important Notes](#important-notes)
- [Contributions](#contributions)


## Getting Started

- Head to [Releases](https://github.com/nebelorz/NST-medivia-bot/releases) and download the latest release.
- **EXTRACT** the .zip you downloaded (if not, your AV could give you a false positive) 
- Open the .exe file

### Usage

When you open NST you'll find exactly this screen:

![bot](https://user-images.githubusercontent.com/65920053/236314912-a060326d-012e-4485-be52-543637edd734.png)


To quickly setup the BOT follow these instructions, filling from top to bottom:

You should input the spell to cast, in addition you should check the "needs blank rune" if the spell requires a blank rune to be casted (e.g. "encurso").

Select a food from the list (hams, fish or brown mushrooms are available).

Optionally select a boost item.

The BOT will focus Medivia client every "X" minutes, so, if you want to check if you can cast the spell every minute, you should input "1".

Minimize checkbox if you want to minimize the client after the BOT casts the spell.

Logout if no supplies if you want your character to logout if there're no blank runes/food/boost item if selected.


### ❗Important Notes
- NST will pop-up any program that starts with the word "Medivia", so be aware not leave any other program with this name (such as Google Chrome while visiting mediviawiki etc.)
 
- The spell will be cast ONLY if you got more than half mana, not configurable at X manapoints and will be casted until you get less than half mana (*e.g. if your character has 300/300 mana, it will cast the spell until 150/300, then will eat food, use boost item and wait the time).*

- Food items as "Hams" will only be detected when the image matches the maximum amount of the stack (*e.g. hams only will be detected if the stack consists of 5 hams or more).*

- When "minimize" is checked, the game will be minimized until the next time check. It's useful if you're using your PC to watch a movie/youtube etc.

- When "logout if no supplies" is checked, the game will logout your character if there're no left supplies (blank runes/food/boost item if selected) using the "force" option.

### Contributions
If you would like to contribute to the project, feel free to open a PR/Issue or request a feature by PM on youtube or e-mail.
