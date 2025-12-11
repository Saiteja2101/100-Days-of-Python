from turtle import Turtle, Screen       #  Importing classes Turtle and Screen from turtle file
import time

screen = Screen()                       # Creatinmg an Object name screen from Screen Class
screen.setup(width=600,height=600)      # Setting the screen size by given width and height
screen.bgcolor("black")                 # Setting the screen background colour
screen.title("Snake Game")              # Creating title for the screen
screen.tracer(0)

# def move_forward():
#     snake[0].forward(20)
# def move_backward():
#     snake[0].backward(20)
def move_anticlockwise():
    snake[0].left(90)
def move_clockwise():
    snake[0].right(90)
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
    time.sleep(0.15)
    for snakes in range(len(snake)-1, 0, -1):
        new_x = snake[snakes-1].xcor()
        new_y = snake[snakes-1].ycor()
        snake[snakes].goto(new_x,new_y)
    snake[0].forward(20)
    # snake[0].left(90)
    screen.listen()
    # screen.onkey(key="w", fun=move_forward)
    # screen.onkey(key="s", fun=move_backward)
    screen.onkey(key="a", fun=move_anticlockwise)
    screen.onkey(key="d", fun=move_clockwise)
    # screen.onkey(key="space",fun=clear_screen)
    # if snake.xcor() > 270:
    #     snake_move = False
        


screen.exitonclick()                    # Close the screen whenever click on the screen 


