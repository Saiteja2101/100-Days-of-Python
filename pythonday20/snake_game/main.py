from turtle import Screen       #  Importing classes Turtle and Screen from turtle file
from paamu import Paamu

import time

screen = Screen()                       # Creatinmg an Object name screen from Screen Class
screen.setup(width=600,height=600)      # Setting the screen size by given width and height
screen.bgcolor("black")                 # Setting the screen background colour
screen.title("Snake Game")              # Creating title for the screen
screen.tracer(0)

python = Paamu()

head = python.snake[0]


screen.listen()
screen.onkey(python.move_up, "w")
screen.onkey(python.move_down, "s")
screen.onkey(python.move_left, "a")
screen.onkey(python.move_right, "d")

snake_move = True

while snake_move:
    screen.update()
    time.sleep(0.15)
    python.move()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        snake_move = False

            



screen.exitonclick()                    # Close the screen whenever click on the screen 


