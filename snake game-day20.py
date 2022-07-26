from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
snake = Snake()
# create a snake body

# snake_positions = [(0, 0), (-20, 0), (-40, 0)]

# segments = []

# for snake_index in range(0, 3):
# for positions in snake_positions:
# snake = Turtle("square")
# snake.color("white")
# snake.penup()
# snake.goto(x=snake_x_positions[snake_index], y=0)
# snake.goto(positions)
# segments.append(snake)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # # for seg in segments:
    # # seg.forward(20)
# # for seg_num in range(start=2, stop=0, step=-1):
# for seg_num in range(len(segments) - 1, 0, -1):
# new_x = segments[seg_num - 1].xcor()
# new_y = segments[seg_num - 1].ycor()
# segments[seg_num].goto(new_x, new_y)
# segments[0].forward(20)


screen.exitonclick()
