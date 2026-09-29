MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
machine = True
resources["money"] = 0

def report():
    for item in resources:
        print(f"{item}: {resources[item]}")


def check_resource(drink):
    for needs in MENU[drink]['ingredients']:
        if MENU[drink]['ingredients'][needs] > resources[needs]:
            print(f"Sorry there is not enough {needs}.")
            return False
    return True

def  make_drink(drink):
    if check_resource(drink):
        if payment(drink):
            for needs in MENU[drink]['ingredients']:
                resources[needs] -= MENU[drink]['ingredients'][needs]

def payment (drink):

    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    cost = MENU[drink]['cost']

    a = int(input("how many quarters?: "))
    b = int(input("how many dimes?: "))
    c = int(input("how many nickles?: "))
    d = int(input("how many pennies?: "))

    paid_money = (a * quarters)+ (b * dimes)+ (c * nickles)+ (d * pennies)

    if paid_money < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif paid_money >= cost:
        print(f"Here is ${round(paid_money - cost, 2)} dollars in change.")
        resources["money"] += cost
        print(f"Here is your {drink}. Enjoy!")
        return True


while machine:
    user_drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_drink == 'espresso':
        make_drink('espresso')

    elif user_drink == 'latte':
        make_drink('latte')

    elif user_drink == 'cappuccino':
        make_drink('cappuccino')

    elif user_drink == 'off':
        machine = False

    elif user_drink == 'report':
        report()

    else:
        print("Wrong input lets try again.")