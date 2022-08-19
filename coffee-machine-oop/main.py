from menu import Menu, MenuItem
from coffee_maker import CoffeMaker
from money_machine import  MoneyMachine

menu = Menu()
coffee_maker = CoffeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"what would you like to order? {options}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if money_machine.make_payment(drink.cost) and coffee_maker.is_resources_sufficient(drink):
            coffee_maker.make_coffee(drink)