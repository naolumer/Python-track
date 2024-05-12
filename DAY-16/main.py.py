# DAY-16


#OOP
# from turtle import Turtle, Screen
# timmy= Turtle()
# timmy.color("green")
# print(timmy)
# timmy.back(40)
# timmy.shape("turtle")
# my_screen= Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick

# import prettytable
# from prettytable import PrettyTable
# table= PrettyTable()
# table.add_column("Pickachu Name", ["pickachu", "squirtle", "chermander"])
# table.add_column( "Type", ["electric","water","fire"])
# print(table)
# table.align
# table.align="l"
# print(table)


#COFFEE MACHINE USING OOP
# from menu import Menu, MenuItem
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine

# money_machine= MoneyMachine()
# coffee_maker= CoffeeMaker()
# menu=Menu()

# is_on= True
# while is_on:
#     order= menu.get_items()
#     choice=input(f"What would you like: {order}")
#     if choice=="off":
#         is_on=False
#     elif choice=="report":
#         coffee_maker.report()
#         money_machine.report()
#     else:
#         drink= menu.find_drink(choice)
#         if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
#             coffee_maker.make_coffee(drink)
        



