from turtle import Turtle                                                            # Importing class Turtle from turtle file
import random                                                                        # Tmporting random module


class Food(Turtle):                                                                  # Creating sub class and inherting the turtle super class
    def __init__(self):
        super().__init__()
        self.shape("circle")                                                         # Creating an Object using turtle class of square shape
        self.penup()                                                                 # Telling that Object to Penup
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)                             # Assigning the shape size
        self.color("orange")                                                         # Assigning that Oject an white colour
        self.speed("fastest")                                                        # Telling the object to move fast
        self.food_move()                                                             # Calling the method
        
    def food_move(self):                                                             # Assigning the Object to random places using this method
           self.goto(random.randint(-250, 250), random.randint(-250, 250))
 