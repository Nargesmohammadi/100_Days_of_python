# import another_module

# print(another_module.another_variable)

# import turtle

# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color('coral')
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.bandwidth)

# my_screen.exitonclick()


# import prettytable

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "water", "Fire"])
table.align = "l"

print(table)
