from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Pong Game")
screen.tracer(0)

bat1 = Paddle((-350, 0))
bat2 = Paddle((350, 0))
ball = Ball()



screen.listen()
screen.onkey(bat1.move_up, "w")
screen.onkey(bat1.move_down, "s")
screen.onkey(bat2.move_up, "Up")
screen.onkey(bat2.move_down, "Down")

game_on = True
while game_on:
    screen.update()

screen.exitonclick()
