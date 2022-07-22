from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

# coffee_maker.report()
# money_machine.report()
menu = Menu()

turn_off = 0
while turn_off != 1:
    options = Menu().get_items()
    user_choice = input(f"What would you like? ({options}): ")
    if user_choice == "off":
        turn_off = 1
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
