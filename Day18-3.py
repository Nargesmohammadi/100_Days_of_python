import turtle as t
import random

tim = t.Turtle()

colours = ["lime green", "blue", "gold", "red", "dark magenta", "deep sky blue", "chartreuse", "light coral"]

# for _ in range(200):
# tim.color(random.choice(colours))
# tim.(random.choice(walk))

direction = [0, 90, 180, 270]
tim.pensize(5)
tim.speed("slow")
for _ in range(200):
    tim.forward(30)
    tim.setheading(random.choice(direction))
    tim.color(random.choice(colours))
