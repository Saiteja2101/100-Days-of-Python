from turtle import *
import random


screen = Screen()
screen.colormode(255)

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
#     sully.pensize(5)
#     sully.color(random.choice(colors))
#     drew_shape(shape_side)
# r = random.randint(0,255)
# g = random.randint(0,255)
# b = random.randint(0,255)

# directions = [ 0,90,180,270,360]

# count = 0
# while count <101:
#     count += 1
#     sully.pensize(10)
#     sully.pencolor(r, g, b)
#     sully.speed("fastest")
#     if (-300 < sully.xcor() <300) and (-300 < sully.ycor() <300):
#         sully.forward(random.randint(20,40))
#         sully.right(random.choice(directions))
#         r = random.randint(0,255)
#         g = random.randint(0,255)
#         b = random.randint(0,255)
#     else:
#        count = 102



# for _ in range(0,120):
#     sully.pencolor(r, g, b)
#     sully.speed("fastest") 
#     sully.circle(100)
#     current_heading = sully.heading()
#     sully.setheading(current_heading + 3)
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)

# gap_size = 5
# for _ in range(int(360/gap_size)):
#     sully.pencolor(r, g, b)
#     sully.speed("fastest") 
#     sully.circle(100)
#     current_heading = sully.heading()
#     sully.setheading(current_heading + gap_size)
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)

# for _ in range(0,10):
#     sully.pencolor(r, g, b)
#     sully.speed("fastest")
#     sully.pensize(10)     
#     sully.penup()
#     sully.forward(10)
#     sully.pendown()
#     sully.forward(1)
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)

sully.speed("fastest")
sully.penup()

# Parameters
dot_size = 10
spacing = 20

rows_and_coloums = int(735/(spacing))

# Move to upper-left corner
sully.goto(-360, 350)

for y in range(rows_and_coloums):  # rows
    for x in range(rows_and_coloums):  # columns
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)

        sully.dot(dot_size, (r, g, b))
        sully.forward(spacing)

    # move down and back to left edge
    sully.backward(spacing * rows_and_coloums)
    sully.right(90)
    sully.forward(spacing)
    sully.left(90)


# screen = Screen()
screen.exitonclick()


