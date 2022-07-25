from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")

# create a snake body
snake = Turtle()
snake_x_positions = [0, -20, -40]
for snake_index in range(0, 2):
    snake = Turtle("square")
    snake.color("white")
    snake.goto(x=snake_x_positions[snake_index], y=0)

