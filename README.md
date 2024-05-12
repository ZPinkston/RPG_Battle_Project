This project is a simple text-based RPG battle simulator that I am building while I am learning to code to apply the concepts.
The user is the player character.
Enemies are selected randomly from a weighted pool. There are currently 6 enemies with 3 moves each, one of which is the boss that, when defeated, will end the game.
The player has 4 options in battle: Attack, Cast 1 of 4 spells, Defend to recover a little HP and MP, or Run Away.
The four spells are: Fireball (damage), Heal(recover HP), Barrier (negate the damage from the next 2 attacks), and Boost(double attack power for the next 2 attacks).
The player currently has four stats: Max HP, Max MP, Strength, and Magic. Stats increase with level up, with the max level currently being lvl 21. Each level requires the same amount of experience as the prior level, plus 25.
If the player is defeated, they have the option to start over, or to exit the program.
The main() is currently in the TEST file until it is at a state that I feel is deliverable, so to speak.
There are separate files and functions for leveling up, damage calculation and spell calculation, and enemy selection.
The project is not nearing its completion, and the things I still want to implement are:
- Increasing the number of enemies and improving the progression.
- Increasing the strategy/skill level by adding more spells, having spells be learned at certain levels, and varying the enemy skills, with weighting on those as well.
- Adding status ailments such as poison, paralyze, and burn.
- Adding elemental properties and elemental strengths and weaknesses.
- Adding more stats such as defense and magic defense, as well as possibly agility for evasion.
- -Incorporating stats into the enemy entities.
- Adding a shop that is accessible by running from the current battle, to purchase weapons and armor, possibly consumables. However, like older RPGs, the best items will be automatically equipped, to avoid text command inventory nonsense.
- Improving the visual display of the game in the terminal.

The project will last as long as my personal education in coding is ideal for it; as long as I am learning code that is useful for it. For example, when I transition to learning HTML/CSS, that will be my focus, so I will not be building games at that time.
