from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("black")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.goto(0,0)