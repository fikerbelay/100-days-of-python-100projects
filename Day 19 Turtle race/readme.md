Turtle Race 🐢

A fun little turtle racing game built with Python's `turtle` module. Place your bet on which colored turtle you think will win, then watch them race across the screen!

This is **Day 19** of my [#100DaysOfCode](https://www.udemy.com/course/100-days-of-code/) journey the **Turtle Race** project from Dr. Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp*.

---

## 🎮 How It Works

1. Run the script.
2. A pop-up asks you to **bet on a turtle color**: `red`, `orange`, `yellow`, `green`, `blue`, or `purple`.
3. Six turtles line up at the starting line and race across the screen — each one taking random steps forward.
4. The first turtle to reach the finish line wins.
5. The terminal tells you if you won or lost.

---

## 🧠 Concepts Practiced

- **Object-Oriented Programming (OOP)** — creating and managing multiple `Turtle` objects.
- **The `turtle` module** — `Screen`, `Turtle`, `shape()`, `color()`, `goto()`, `forward()`, `xcor()`.
- **`screen.tracer(0)` + `screen.update()`** — manual screen refreshing for smooth, flicker-free animation.
- **The `random` module** — `random.choice()` to pick a random turtle each turn.
- **Loops & conditionals** — a `while` loop that runs until a turtle crosses the finish line.
- **User input** — `screen.textinput()` to capture the player's bet.
- **Coordinate system** — positioning turtles with `x`/`y` coordinates.

---

## 🛠️ Requirements

- Python 3.x
- The `turtle` module (comes pre-installed with standard Python)

No third-party libraries needed.

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/<your-username>/<your-repo>.git

# Navigate into the project folder
cd <your-repo>

# Run the game
python main.py
```

> ⚠️ **Note:** The `turtle` module requires a graphical display. It will not run in a headless environment (e.g., most online sandboxes without a screen).

---

## 📂 Project Structure

```
day-19-turtle-race/
│
├── main.py       # The full game logic
└── README.md     # You're reading it!
```

---

## 🐛 A Note on `tracer(0)`

A common gotcha with this project: calling `screen.tracer(0)` disables automatic screen refreshes, which means **nothing moves on screen unless you call `screen.update()`** after each turtle movement.

If the race appears frozen, check that `screen.update()` is being called inside the race loop  not just during setup.

---

## 💡 Possible Improvements

- Add a visible **finish line** drawn with a turtle.
- Show the **winner's name in a pop-up** instead of just the terminal.
- Add **multiple rounds** and track scores.
- Let the player choose their **turtle color from a dropdown** instead of typing.
- Add sound effects with `winsound` (Windows) or `playsound`.

---
