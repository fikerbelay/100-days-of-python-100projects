# Coffee Machine (OOP Edition) ☕

A command-line coffee machine simulator built with **Object-Oriented Programming** in Python.

Originally built procedurally on **Day 15** of the 100 Days of Python challenge, then refactored into a clean **OOP design on Day 16**. The machine handles drink selection, resource management, coin processing, and change calculation — just like a real vending machine.

---

## 📁 Project Structure

```
Coffee Machine/
├── main.py             # Entry point — runs the machine loop
├── menu.py             # Menu & MenuItem classes (drinks and their recipes)
├── coffee_maker.py     # CoffeeMaker class (resources & brewing)
├── money_machine.py    # MoneyMachine class (coins, payment, profit)
└── README.md
```

---

## 🚀 How to Run

Requires **Python 3.7+**.

```bash
python main.py
```

### Example session

```
What would you like to drink? (latte/espresso/cappuccino/): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $0.0 in change.
Here is your latte ☕️. Enjoy!
```

### Special commands

| Input     | Effect                                      |
|-----------|---------------------------------------------|
| `latte`   | Order a latte                               |
| `espresso`| Order an espresso                           |
| `cappuccino` | Order a cappuccino                       |
| `report`  | Print current resources and profit          |
| `off`     | Turn off the machine (exit the program)     |

---

## 🧩 Class Overview

### `menu.py`

Two classes:

- **`MenuItem`** — represents a single drink. Stores its name, cost, and required ingredients.
- **`Menu`** — holds the list of available drinks and provides helpers:
  - `get_items()` → returns a `/`-separated string of drink names
  - `find_drink(name)` → returns the matching `MenuItem` or `None`

```python
MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)
```

### `coffee_maker.py`

- **`CoffeeMaker`** — models the physical machine.
  - Holds a `resources` dict: water (ml), milk (ml), coffee (g)
  - `report()` — prints current resource levels
  - `is_resource_sufficient(drink)` — checks if the machine can make the drink
  - `make_coffee(order)` — deducts ingredients and serves the drink

### `money_machine.py`

- **`MoneyMachine`** — handles all money logic.
  - `report()` — prints accumulated profit
  - `process_coins()` — prompts user for coin counts and returns total inserted
  - `make_payment(cost)` — validates payment, returns change, updates profit

Supported coins: `quarters` (0.25), `dimes` (0.10), `nickles` (0.05), `pennies` (0.01)

### `main.py`

Ties everything together in a `while` loop:

```python
if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
    coffee_maker.make_coffee(drink)
```

The drink is only made if **both** resources are sufficient **and** payment succeeds.

---

## 🧠 Why OOP Here?

The procedural version of this project (Day 15) had everything in one file — menus, resources, and money logic were all mixed together. Refactoring into OOP gave us:

| Benefit              | How                                                                 |
|----------------------|---------------------------------------------------------------------|
| **Separation**       | Menu, machine, and money logic live in separate files               |
| **Reusability**      | `MenuItem` objects make adding new drinks trivial                   |
| **Encapsulation**    | Each class owns its own state (resources, profit, menu items)       |
| **Readability**      | `main.py` reads like a sentence: check resources → take payment → make coffee |

---

## 🛠 Possible Improvements

- [ ] Accept `t/f`, uppercase inputs, or abbreviations (e.g. `l` for latte).
- [ ] Prevent negative coin counts.
- [ ] Refill resources via a hidden command (e.g. `refill`).
- [ ] Move menu items to a JSON file for easy editing.
- [ ] Add a simple Tkinter or terminal-UI front end.
- [ ] Track and display a sales history.

---

## 📚 Part of

[100 Days of Code — The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)

- **Day 15** — Coffee Machine (procedural)
- **Day 16** — Coffee Machine (OOP refactor) ← *this version*

