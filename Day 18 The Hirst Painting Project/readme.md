
# 🎨 Hirst Dot Painting

A Python recreation of Damien Hirst's famous spot paintings, drawn using the `turtle` graphics module. Built as part of my **#100Projects** challenge.

## 📖 About

This program draws a grid of randomly colored dots inspired by Damien Hirst's iconic spot paintings. Each dot gets a random RGB color, creating a unique piece of generative art every time you run it.

## 🎮 How It Works

1. The turtle starts at the top-left corner (`-300, 250`) with no trail drawn.
2. It moves right, drawing 16 dots per row, each with a random color.
3. It snakes its way down and back for 7 rows.
4. Click anywhere on the window to close it.

## 🛠️ Requirements

- Python 3.x
- `turtle` (included with Python — no install needed)

## 📁 Project Structure

```
hirst-painting/
├── main.py       # All drawing logic
└── README.md     # You're here!
```

## 🚀 Run It

```bash
python main.py
```

A window will pop up showing the painting. **Click anywhere** to exit.

## 🧠 What I Learned

- Using the `turtle` module for graphics
- Enabling RGB color mode with `turtle.colormode(255)`
- Generating random colors with `randint`
- Drawing without lines using `penup()` / `pendown()`
- Moving the turtle with `forward()`, `back()`, `right()`, `left()`, `goto()`
- Snaking through a grid with turns to reverse direction

## 🎨 Customization

Want to tweak the artwork? Try changing:

- **Dot size** → `tim.pensize(40)`
- **Spacing** → `tim.forward(40)` inside `paint()`
- **Grid size** → the `range(16)` in `paint()` and `range(7)` in the main loop
- **Starting position** → `tim.goto(-300, 250)`

## 🔮 Possible Improvements

- [ ] Replace `tim.back(40)` in `turn()` with a simpler repositioning approach
- [ ] Add a `while` loop that keeps drawing until the user closes the window, allowing multiple paintings
- [ ] Save the drawing as an image using `screen.getcanvas().postscript()`
- [ ] Add a colored background (`turtle.bgcolor()`)
- [ ] Parameterize dot count, spacing, and rows as constants at the top
- [ ] Use `random.choice()` from a curated palette instead of fully random RGB for a more Hirst-like aesthetic

## 🏆 Part of #100Projects

This is project **18/100** in my journey to build 100 projects. Follow along!

---

⭐ If you enjoyed this, feel free to star the repo!
```

## Quick notes on the code

A few small cleanups worth mentioning if this is going public:

1. **`tim.forward(0)`** in `paint()` does literally nothing — you can delete it.

2. **`tup` variable** in `random_color()` — you can just `return (r, g, b)` directly without storing it, or rename it to something meaningful like `rgb`.
