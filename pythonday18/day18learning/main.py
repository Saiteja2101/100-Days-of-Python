from turtle import *
import random

sully = Turtle()
sully.shape("turtle")
sully.color("blue")

colors = ["red", "orange", "yellow", "green", "blue", "pink"]


# def drew_shape (sides):
#     angle = 360 / sides
#     for q in range(sides):
#         for _ in range(1):
#             sully.forward(50)   # Move forward 100 units
#             sully.right(angle)
#         sides  += 1

# for shape_side in range(3,11):
#     sully.color(random.choice(colors))
#     drew_shape(shape_side)

r = random.random()
g = random.random()
b = random.random()

directions = [ 0,90,180,270,360]

count = 0
while count <101:
    count += 1
    sully.pensize(10)
    rgb = (r,g,b)
    sully.pencolor(rgb)
    if (-300 < sully.xcor() <300) and (-300 < sully.ycor() <300):
        sully.forward(random.randint(30,60))
        sully.right(random.choice(directions))
    else:
       count = 102

screen = Screen()
screen.exitonclick()

