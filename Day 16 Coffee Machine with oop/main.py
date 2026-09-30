import menu
import coffee_maker
import money_machine

menu = menu.Menu()
coffee_maker = coffee_maker.CoffeeMaker()
money_machine = money_machine.MoneyMachine()

machine = True

while machine:
    options = menu.get_items()
    user_choice = input(f"what would you like to drink? {options}")


    if user_choice == 'off':
        machine = False
    elif user_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)