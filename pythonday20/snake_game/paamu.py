from turtle import Turtle

cordinates = [(0,0),(-20,0),(-40,0)]
move_distance = 20

class Paamu:
    def __init__(self):
        self.snake= []
        self.snake_creation()

    def snake_creation(self):
        for i in range(len(cordinates)):
            turtles = Turtle(shape="square")
            turtles.color("white")
            turtles.penup()
            turtles.goto(cordinates[i])
            self.snake.append(turtles)

    def move_up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def move_down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def move_left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def move_right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

        
    def move(self):
        for snakes in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[snakes-1].xcor()
            new_y = self.snake[snakes-1].ycor()
            self.snake[snakes].goto(new_x,new_y)
        self.snake[0].forward(move_distance)

        









 




        

                
        

