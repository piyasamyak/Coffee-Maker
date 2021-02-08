from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

makeCoffee = True
while makeCoffee:
    order = input(f"Enter your order ({menu.get_items()}): ")
    if order == "report":
        coffeeMaker.report()
        moneyMachine.report()
    elif order == "off":
        makeCoffee = False
    else:
        drink = menu.find_drink(order)
        if drink is not None:
            menuItem = MenuItem(drink.name, drink.cost, drink.ingredients["water"], drink.ingredients["milk"],
                                drink.ingredients["coffee"])
            if coffeeMaker.is_resource_sufficient(drink):
                print("Please enter coins.")
                if moneyMachine.make_payment(menu.find_drink(order).cost):
                    coffeeMaker.make_coffee(menu.find_drink(order))







