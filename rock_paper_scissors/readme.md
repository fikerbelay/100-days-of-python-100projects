# ✂️ Rock, Paper, Scissors

## 📌 Project Description
Rock, Paper, Scissors is a classic command-line game built with Python. The player competes against the computer by choosing either Rock, Paper, or Scissors. The computer randomly selects its move, and the program determines the winner based on the game rules.

This project introduces randomization, lists, loops, and conditional statements while creating a fun interactive game.

## 🛠️ How It Works
1. The player chooses:
   - `0` for Rock
   - `1` for Paper
   - `2` for Scissors
2. The computer randomly selects one of the three options.
3. Both choices are displayed using ASCII art.
4. The program compares the choices and announces the result:
   - Win
   - Lose
   - Draw
5. The game repeats, allowing the player to play multiple rounds.

## 💻 Example

```
What do you choose?
Type 0 for Rock, 1 for Paper or 2 for Scissors.

> 2

You chose:

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

Computer chose:

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

You win!
```

## 📚 Concepts Practiced
- Variables
- Lists
- Multi-line strings
- User input with `input()`
- Random number generation using the `random` module
- `while` loops
- Conditional statements (`if`, `elif`, `else`)
- ASCII art
- Building an interactive command-line game

## 🎮 Game Rules
- 🪨 Rock beats Scissors
- 📄 Paper beats Rock
- ✂️ Scissors beats Paper
- If both players choose the same option, the game ends in a draw.

## Future Improvements
Possible improvements:
- Validate user input to prevent crashes from invalid numbers.
- Add an option to quit the game.
- Keep track of wins, losses, and draws.
- Allow players to play a "best of three" or "best of five" series.
- Add sound effects or create a graphical version using Tkinter or Pygame.

## Author
**Fiker Belay**

Part of my **100 Days of Python Projects** journey.
