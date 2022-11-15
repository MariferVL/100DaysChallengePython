
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMachine = CoffeeMaker()
moneyMachine = MoneyMachine()
drinks = menu.get_items()

machine_on = True


while machine_on:
    order = input(f"What drink do you want? Type: {drinks}\n")

    if order == "report":
        coffeeMachine.report()
        moneyMachine.report()
    elif order == "off":
        machine_on = False
    elif order in drinks:
        detail = menu.find_drink(order)
        if coffeeMachine.is_resource_sufficient(detail):
            if moneyMachine.make_payment(detail.cost):
                coffeeMachine.make_coffee(detail)
    else:
        print("Wrong answer.")