from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
condition = True
while condition :

    question_coffee = input("would you drink coffee ? espresso/latte/cappuccino ")

    if question_coffee == "off":
        print("machineis closed")
        sys.exit()
    elif question_coffee == "report":
        coffe_maker.report()
        money_machine.report()
    elif question_coffee == "latte" or question_coffee == "espresso" or question_coffee == "cappuccino":
        drink = menu.find_drink(question_coffee)
        if coffe_maker.is_resource_sufficient(drink) :
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)

            

            


