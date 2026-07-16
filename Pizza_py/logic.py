"""
logic.py
---------
Contains all business logic for PizzaPy.
"""


# -----------------------------
# Pizza Prices
# -----------------------------

PIZZA_PRICES = {
    "S": 15,
    "M": 20,
    "L": 25
}

PEPPERONI_PRICES = {
    "S": 2,
    "M": 3,
    "L": 3
}

CHEESE_PRICE = 1


# -----------------------------
# Bill Calculation
# -----------------------------

def calculate_bill(size, pepperoni=False, cheese=False):
    """
    Calculates the total bill.

    Args:
        size (str): S, M or L
        pepperoni (bool)
        cheese (bool)

    Returns:
        int
    """

    size = size.upper()

    if size not in PIZZA_PRICES:
        raise ValueError("Invalid pizza size.")

    total = PIZZA_PRICES[size]

    if pepperoni:
        total += PEPPERONI_PRICES[size]

    if cheese:
        total += CHEESE_PRICE

    return total


# -----------------------------
# Receipt Creation
# -----------------------------

def create_receipt(name, size, pepperoni=False, cheese=False, delivery=False):
    """
    Returns receipt information as a dictionary.
    """

    size = size.upper()

    receipt = {
        "customer": name if name.strip() else "Guest",
        "size": size,
        "base_price": PIZZA_PRICES[size],
        "pepperoni": pepperoni,
        "pepperoni_price": PEPPERONI_PRICES[size] if pepperoni else 0,
        "cheese": cheese,
        "cheese_price": CHEESE_PRICE if cheese else 0,
        "delivery": delivery,
        "eta": "20-30 Minutes" if delivery else "Ready in 10-15 Minutes",
        "total": calculate_bill(size, pepperoni, cheese)
    }

    return receipt


# -----------------------------
# Format Receipt
# -----------------------------

def format_receipt(receipt):
    """
    Returns a printable receipt string.
    """

    lines = [
        "🍕 PizzaPy",
        "=" * 30,
        f"Customer : {receipt['customer']}",
        "",
        f"{receipt['size']} Pizza        ${receipt['base_price']}"
    ]

    if receipt["pepperoni"]:
        lines.append(f"Pepperoni      ${receipt['pepperoni_price']}")

    if receipt["cheese"]:
        lines.append(f"Extra Cheese   ${receipt['cheese_price']}")

    lines.extend([
        "",
        "-" * 30,
        f"TOTAL          ${receipt['total']}",
        "",
        f"ETA: {receipt['eta']}",
        "",
        "❤️ Thank you for choosing PizzaPy!",
        "=" * 30
    ])

    return "\n".join(lines)


# -----------------------------
# Test
# -----------------------------

if __name__ == "__main__":

    receipt = create_receipt(
        name="Yuta",
        size="L",
        pepperoni=True,
        cheese=True,
        delivery=True
    )

    print(format_receipt(receipt))