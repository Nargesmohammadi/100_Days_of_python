# for once or twice
# import turtle

# tim = turtle.Turtle()

# for several time or more
from turtle import Turtle

# tim1 = Turtle


# create a new object
# import turtle as t
# tim2 = t.Turtle()

# for _ in range(15):
# tim2.forward(10)
# tim2.penup()
# tim2.forward(10)
# tim2.pendown()


# import heroes
# print(heroes.gen())

import turtle as t
import random

tim = t.Turtle()

colours = ["lime green", "blue", "gold", "red", "dark magenta", "deep sky blue", "chartreuse", "light coral"]


def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_sides_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shapes(shape_sides_n)
