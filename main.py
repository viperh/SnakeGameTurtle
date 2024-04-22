from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
width = 600
height = 600
screen.setup(width=width, height=height)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

s = Snake()
f = Food(width, height)
score = Scoreboard()

screen.listen()
screen.onkey(s.move_up, "w")
screen.onkey(s.move_down, "s")
screen.onkey(s.move_left, "a")
screen.onkey(s.move_right, "d")

screen_width = screen.window_width() // 2
screen_height = screen.window_height() // 2

game_is_on = True

points_counter = 0

while game_is_on:
    screen.update()
    time.sleep(0.1)
    s.move()

    if s.segments[0].xcor() > screen_width or s.segments[0].xcor() < -screen_width or s.segments[
        0].ycor() > screen_height or s.segments[0].ycor() < -screen_height:
        game_is_on = False
        print("Game Over")

    if s.segments[0].distance(f) < 15:
        f.refresh()
        s.extend()
        points_counter += 1
        score.update()

screen.exitonclick()
