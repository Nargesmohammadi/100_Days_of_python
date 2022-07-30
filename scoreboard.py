from turtle import Turtle


class Scoreboard(Turtle):
    def __int__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        # self.write(arg="score", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg="score", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        # self.write(arg="score", align="center", font=("Arial", 24, "normal"))
        self.clear()
        self.update_scoreboard()
