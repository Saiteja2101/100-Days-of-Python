from turtle import Turtle, Screen       #  Importing classes Turtle and Screen from turtle file
import time

screen = Screen()                       # Creatinmg an Object name screen from Screen Class
screen.setup(width=600,height=600)      # Setting the screen size by given width and height
screen.bgcolor("black")                 # Setting the screen background colour
screen.title("Snake Game")              # Creating title for the screen
screen.tracer(0)

# def move_forward():
#     snake.forward(20)
# def move_backward():
#     snake.backward(20)
# def move_anticlockwise():
#     snake.left(90)
# def move_clockwise():
#     snake.right(90)
# def clear_screen():
#     snake.clear()
#     snake.penup()
#     snake.home()
#     snake.pendown()


cordinates = [(0,0),(-20,0),(-40,0)]

snake= []

for i in range(3):
    turtles = Turtle(shape="square")
    turtles.color("white")
    turtles.penup()
    turtles.goto(cordinates[i])
    snake.append(turtles)



snake_move = True


while snake_move:
    screen.update()
    time.sleep(0.25)
    for snakes in snake:
        snakes.forward(20)
        # screen.listen()
        # screen.onkey(key="w", fun=move_forward)
        # screen.onkey(key="s", fun=move_backward)
        # screen.onkey(key="a", fun=move_anticlockwise)
        # screen.onkey(key="d", fun=move_clockwise)
        # screen.onkey(key="space",fun=clear_screen)
        if snakes.xcor() > 270:
            snake_move = False
        


screen.exitonclick()                    # Close the screen whenever click on the screen 


