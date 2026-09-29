# ☕ Coffee Machine

A CLI-based coffee machine simulator built in Python, as part of my **#100Projects** challenge. Order drinks, insert coins, get change, and keep an eye on the machine's resources.

## 📖 About

This program simulates a real coffee vending machine. It tracks water, milk, coffee, and money. You can order a drink, pay with coins, and the machine will tell you if it has enough resources or if you've paid enough. It even has a hidden maintenance mode for checking stock and shutting down.

## 🎮 How to Use

Run the program and you'll be prompted:

```
What would you like? (espresso/latte/cappuccino):
```

### Commands

| Input        |          Action                                      |
|--------------|------------------------------------------------------|
| `espresso`   |          Order an espresso ($1.50)                   |
| `latte`      |          Order a latte ($2.50)                       |
| `cappuccino` |          Order a cappuccino ($3.00)                  |
| `report`     | Print current resources (water, milk, coffee, money) |
| `off`        |          Turn off the machine                        |

### Ordering Flow

1. Choose a drink.
2. The machine checks if it has enough **water, milk, and coffee**.
3. You're asked how many **quarters, dimes, nickels, and pennies** you want to insert.
4. If you underpay → refund. If you overpay → change is returned.
5. If everything checks out, your drink is made and resources are deducted.

## 🛠️ Requirements

- Python 3.x
- No external libraries needed — pure standard library

## 📁 Project Structure

```
coffee-machine/
├── main.py       # All game logic, MENU, and resources
└── README.md     # You're here!
```

## 🧾 Menu & Resources

The machine starts with:

```python
resources = {
    "water": 300,   # ml
    "milk": 200,    # ml
    "coffee": 100,  # g
}
```

Drinks and their requirements are defined in the `MENU` dictionary at the top of `main.py`.

## 🚀 Run It

```bash
python main.py
```

## 🧠 What I Learned

- Structuring nested dictionaries (`MENU` → drink → ingredients → amounts)
- Iterating over dict keys to compare requirements vs. available resources
- Chained function calls with boolean returns (`make_drink` → `check_resource` → `payment`)
- Simulating real-world logic (coin math, change calculation, refunds)
- Using a `while` loop as a persistent program state
- Rounding floats with `.__round__(2)` to avoid floating point display issues

## 🔮 Possible Improvements

- [ ] Handle non-integer input for coin counts (currently crashes on `"abc"`).
- [ ] Add a `--reset` option to restore resources.
- [ ] Track total drinks sold.
- [ ] Display resource units (`300ml` instead of `300`) in the report.
- [ ] Prevent ordering if the machine has no money for change.
- [ ] Refactor the big `if/elif` chain for drink selection with a dictionary lookup.


## 🏆 Part of #100Projects

This is project **[X]/100** in my journey to build 100 projects.

