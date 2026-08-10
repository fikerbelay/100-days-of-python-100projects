# 🎯 Hangman Game

## 📌 Project Description
Hangman is a classic word-guessing game built entirely in Python and played in the terminal. The player attempts to guess a randomly selected word one letter at a time while avoiding too many incorrect guesses.

The game displays the current progress of the word, keeps track of guessed letters, and updates the hangman ASCII art after every incorrect guess. The player wins by revealing the entire word before running out of lives.

This project is organized into multiple Python files to improve code structure and readability.

---

## 📂 Project Structure

```
Hangman/
│
├── main.py                # Main game logic
├── hangman_words.py       # List of possible words
├── hangman_stages.py      # ASCII art for each hangman stage
└── README.md
```

### File Overview

- **main.py**
  - Runs the game.
  - Handles user input.
  - Checks guessed letters.
  - Tracks lives.
  - Determines win or loss.

- **hangman_words.py**
  - Stores the list of words that can be randomly selected for the game.

- **hangman_art.py**
  - Contains the ASCII art representing each stage of the hangman as the player loses lives and the games logo.

---

## 🛠️ How It Works

1. A random word is selected from `hangman_words.py`.
2. The player guesses one letter at a time.
3. Correct guesses reveal their positions in the word.
4. Incorrect guesses reduce the player's remaining lives.
5. The hangman drawing updates after each wrong guess.
6. The game ends when:
   - The player guesses the entire word (Win 🎉)
   - The player runs out of lives (Game Over 💀)

---

## 💻 Example

```
Welcome to Hangman!

Word: _ _ _ _ _

Guess a letter:
> a

Good guess!

Word: A _ _ A _

Lives Remaining: 6

Guess a letter:
> z

Wrong guess!

Lives Remaining: 5
```

---

## 📚 Concepts Practiced

- Variables
- Lists
- Strings
- Loops (`while`)
- Conditional statements (`if`, `elif`, `else`)
- Functions
- Importing modules
- Random number generation
- Organizing code into multiple Python files
- ASCII art
- Building an interactive terminal application

---

##  Future Improvements

Possible improvements:

- Add difficulty levels.
- Prevent duplicate letter guesses.
- Display guessed letters.
- Add categories (Animals, Countries, Movies, etc.).
- Allow players to replay without restarting the program.
- Add a graphical user interface (GUI) using Tkinter or Pygame.
- Load words from an external text file.

---

##  Author

**Fiker Belay**

Part of my **100 Days of Python Projects** journey.
