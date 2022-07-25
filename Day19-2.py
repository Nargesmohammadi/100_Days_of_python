from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="which turtle will win the race? enter a color:")
colors = ["red", "blue", "orange", "green", "purple", "yellow"]
y_positions = [-80, -50, -20, 10, 40, 70]
for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])

screen.exitonclick()
