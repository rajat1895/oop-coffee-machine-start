from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu_object = Menu()
coffee_maker_object = CoffeeMaker()
money_machine_object = MoneyMachine()

is_on=True
while is_on:
    options = menu_object.get_items()
    choice = input(f"What would you like? ({options}):")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker_object.report()
        money_machine_object.report()
    else:
        drink = menu_object.find_drink(choice)
        if coffee_maker_object.is_resource_sufficient(drink) and money_machine_object.make_payment(drink.cost):
            coffee_maker_object.make_coffee(drink)




