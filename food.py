from turtle import Turtle

import random


class Food(Turtle):

    def __init__(self, width, height):
        super().__init__()
        self.width = width // 2
        self.height = height // 2
        self.create_food()
        self.refresh()

    def create_food(self):
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.color("blue")
        self.speed("fastest")

    def refresh(self):
        self.goto(random.randint((self.width - 20) * -1, self.width - 20),
                  random.randint((self.height - 20) * -1, self.height))
