from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Consolas", 24, "bold")


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
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.write_text()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

