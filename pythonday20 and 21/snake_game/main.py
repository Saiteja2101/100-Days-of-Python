from turtle import Screen       #  Importing class Screen from turtle file
from paamu import Paamu         #  Importing class Paamu from paamu file
import time                     #  Importing time module

screen = Screen()                       # Creatinmg an Object name screen from Screen Class
screen.setup(width=600,height=600)      # Setting the screen size by given width and height
screen.bgcolor("black")                 # Setting the screen background colour
screen.title("Snake Game")              # Creating title for the screen
screen.tracer(0)                        

python = Paamu()                        # Creating an Object using Classfile

head = python.snake[0]                  # Assigned variable of first variable of file from Object


screen.listen()                         # Assigning Screen to listen 
screen.onkey(python.move_up, "w")       # Assigning w key to move up the Object
screen.onkey(python.move_down, "s")     # Assigning s key to move down the Object
screen.onkey(python.move_left, "a")     # Assigning a key to move left the Object
screen.onkey(python.move_right, "d")    # Assigning d key to move right the Object

snake_move = True                       # Creating an Boolean function

while snake_move:                       # Run the loop till the boolean function is wrong
    screen.update()                     # Updating the screen for every step
    time.sleep(0.15)                    # After updating wait for 0.15 seconds
    python.move()                       # Then Assigning the Object to move function defined in 
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:              # Telling the variable not cross boundry
        snake_move = False              # If crosses boolean function is wrong

            



screen.exitonclick()                    # Close the screen whenever click on the screen 


