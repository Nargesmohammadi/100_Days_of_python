from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


# def draw_circle():
    # tim.circle(100.0)


def move_right():
    tim.setheading(tim.heading() + 10)


def move_left():
    tim.setheading(tim.heading() + 10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
# function as inputs
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_right, "d")
screen.onkey(move_left, "a")
screen.exitonclick()
