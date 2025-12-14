from turtle import Turtle

START_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280

class Man(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.color("black")
        self.goto(START_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        if self.ycor() > -280:
            self.backward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(START_POSITION)

    def reached_finish(self):
        return self.ycor() > FINISH_LINE_Y
