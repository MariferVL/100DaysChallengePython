### Coffee Machine Program Requirements ###
from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
machine_on = True


def report():
    print("\nReport 🗳️:")
    for key in resources:
        print(f"{key.capitalize()}: {resources[key]}")
    print(f"Money: ${money}")


def check_resources(ingredients):
    """Check sufficient resources to make coffee."""
    for item in resources:
        if resources[item] < ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True


def coins():
    print("Please, insert coins")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def check_money(payment, cost, drink): # traer bebida y costo. Arrastrar dinero
    global money
    if payment > cost:
        change = payment - cost
        money += cost
        print(f"Here is ${change} dollars in change.")
        print(f"Here is your {drink}. ☕ Enjoy!")
        return True

    elif payment == cost:
        print(f"Here is your {drink}. ☕ Enjoy!")
        money += cost
        return True

    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def report_update(ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]


while machine_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "report":
        report()
    elif order == "off":
        machine_on = False
    elif order in MENU.keys():
        drink = MENU[order]
        if check_resources(drink["ingredients"]):
            payment = coins()
            if check_money(payment, drink["cost"], order):
                report_update(drink["ingredients"])
    else:
        print("Wrong Answer.")
