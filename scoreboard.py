from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write_text()

    def write_text(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "bold"))

    def update(self):
        self.score += 1
        self.clear()
        self.write_text()