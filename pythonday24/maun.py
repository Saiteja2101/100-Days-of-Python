from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Pong Game")
screen.tracer(0)

bat1 = Paddle((-350, 0))
bat2 = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(bat1.move_up, "w")
screen.onkey(bat1.move_down, "s")
screen.onkey(bat2.move_up, "Up")
screen.onkey(bat2.move_down, "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.08)
    ball.move()

    # Wall bounce (top & bottom)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Paddle bounce (right paddle)
    if ball.distance(bat2) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Paddle bounce (left paddle)
    if ball.distance(bat1) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Ball out of bounds
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_increase()
    
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_increase()
    
screen.exitonclick()
