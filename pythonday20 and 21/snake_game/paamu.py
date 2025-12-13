from turtle import Turtle                             # Importing class Screen from turtle file

cordinates = [(0,0),(-20,0),(-40,0)]                  # Creating file and it consists of tuples of co-ordinates
move_distance = 20                                    # Assigning the variable

class Paamu:                                          # Creating the Class
    def __init__(self):                               # Assigning the Atributes
        self.snake= []                                # Creating an empthy file of that class
        self.snake_creation()                         # Calling the method

    def snake_creation(self):                         # Creating the Method
        for position in cordinates:                   # Run the loop 3 times (because there are 3 co-ordinates)
            self.add_snake(position)                  # calling the function

    def add_snake(self, position):
        turtles = Turtle(shape="square")          # Creating an Object using turtle class of square shape
        turtles.color("white")                    # Assigning that Oject an white colour
        turtles.penup()                           # Telling that Object to Penup
        turtles.goto(position)               # Telling each oject to goto resoective co-ordinates given in that variable
        self.snake.append(turtles)                # Adding Each Object in a file after creating that Object

    def extend(self):                                 # Extending the snake whenever snake eats the food
        self.add_snake(self.snake[-1].position())     # Adding the next turtle to previous position of last turtle
        

    def move_up(self):                                # Creating the Method
        if self.snake[0].heading() != 270:            # Asking if the Turtle head is not an angle of 270
            self.snake[0].setheading(90)              # Telling that turtle to head to angle of 90

    def move_down(self):                              # Creating the Method
        if self.snake[0].heading() != 90:             # Asking if the Turtle head is not an angle of 90
            self.snake[0].setheading(270)             # Telling that turtle to head to angle of 270

    def move_left(self):                              # Creating the Method
        if self.snake[0].heading() != 0:              # Asking if the Turtle head is not an angle of 0
            self.snake[0].setheading(180)             # Telling that turtle to head to angle of 180

    def move_right(self):                             # Creating the Method
        if self.snake[0].heading() != 180:            # Asking if the Turtle head is not an angle of 180
            self.snake[0].setheading(0)               # Telling that turtle to head to angle of 0

        
    def move(self):                                   # Creating a Method
        for snakes in range(len(self.snake)-1, 0, -1):     # Running the loop 3 times but in reverse order 
            new_x = self.snake[snakes-1].xcor()            # Assigning the before (3 will take 2 co-ordinates) turtle x_co-ordinates
            new_y = self.snake[snakes-1].ycor()            # Assigning the before (3 will take 2 co-ordinates) turtle x_co-ordinates
            self.snake[snakes].goto(new_x,new_y)           # Telling that turtle to move to new co-ordinates
        self.snake[0].forward(move_distance)               # Telling that first turtle to move further with above assigned value

        









 




        

                
        

