from turtle import Screen       #  Importing class Screen from turtle file
from paamu import Paamu         #  Importing class Paamu from paamu file
from food import Food           #  Importing class Food from food file
from scoreboard import Scoreboard   #  Importing class Scoreboard from scoreboard file
import time                     #  Importing time module

screen = Screen()                       # Creatinmg an Object name screen from Screen Class
screen.setup(width=600,height=600)      # Setting the screen size by given width and height
screen.bgcolor("black")                 # Setting the screen background colour
screen.title("Snake Game")              # Creating title for the screen
screen.tracer(0)                        

python = Paamu()                        # Creating an Object using Class
tindi = Food()                          # Creating an OBject using Class
scoreboard = Scoreboard()               # Creating an OBject using Class
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
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:              # Telling the variable not cross boundry
        snake_move = False              # If crosses boolean function is wrong
        scoreboard.game_over()
    if head.distance(tindi) < 15:       # If distance between the head and tindi is less than 15cm
        tindi.food_move()               # Calling the food_move method from Food class
        scoreboard.increase()           # Calling the increase method from scoreboard class
        python.extend()                 # Calling the food_move method from Food class
    
    for segment in python.snake[1:]:                    # Sarting the for loop from list starting from index 1 this is called list slicing
        if head.distance(segment) < 10:                 # If the distance of head and any of the segment from the list is less than 10cm
            snake_move = False                          # Boolean function is wrong
            scoreboard.game_over()                      # Calling game_over method from SCoreboard Class


screen.exitonclick()                    # Close the screen whenever click on the screen 


