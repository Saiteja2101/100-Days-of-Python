from turtle import Turtle                                                               # Importing class Turtle from turtle file

class Scoreboard(Turtle):                                                               # Creating sub class and inherting the turtle super class
    def __init__(self):
        super().__init__()
        self.score = 0                                                                  # Assigning the score to the Object
        self.hideturtle()                                                               # Telling to the hide the object
        self.penup()                                                                    # Telling that Object to Penup
        self.color("white")                                                             # Assigning that Oject an white colour
        self.goto (0,268)                                                               # Telling to Object to go to that location
        self.update_score()                                                             # Calling the function
        
    def update_score(self):                                                             # Creating the method to to show scoreboard 
        self.write(f"Score: {self.score}", align="center", font=("Arial",15,"normal"))  # Using write function giving the font size, type and allignmnet

    def game_over(self):                                                                # Creating the method when game over
        self.goto(0,0)                                                                  # Telling the object to center
        self.write(f"GAME OVER", align="center", font=("Arial",15,"normal"))            # Using the write function telling Game Over

    def increase(self):                                                                 # Creating a method to increase the score
        self.score += 1
        self.clear()
        self.update_score()                                                             # WHenever score increases clear the before score and then update the score