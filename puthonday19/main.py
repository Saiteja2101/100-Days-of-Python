from turtle import Turtle, Screen

sully = Turtle()
bully = Turtle()
mully = Turtle()
gully = Turtle()

colors = ["red", "orange", "yellow", "green", "blue", "black"]

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput("Welcome to the 'TRG'","Place your bets on turtle ('Blue','Green','Red','Black')").lower()
print(user_bet)

sully.color(colors[0])
bully.color(colors[3])
mully.color(colors[4])
gully.color(colors[5])


def turtle1_startingpoint():
    sully.penup()
    sully.goto(-240,25)

def turtle2_startingpoint():
    bully.penup()
    bully.goto(-240,-25)

def turtle3_startingpoint():
    mully.penup()
    mully.goto(-240,75)

def turtle4_startingpoint():
    gully.penup()
    gully.goto(-240,-75)

turtle1_startingpoint()
turtle2_startingpoint()
turtle3_startingpoint()
turtle4_startingpoint()

# def move_forward():
#     sully.forward(100)
# def move_backward():
#     sully.backward(90)
# def move_anticlockwise():
#     sully.left(45)
#     sully.circle(100,80)
# def move_clockwise():
#     sully.right(45)
#     sully.circle(100,80)
# def clear_screen():
#     sully.clear()
#     sully.penup()
#     sully.home()
#     sully.pendown()


# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=move_anticlockwise)
# screen.onkey(key="d", fun=move_clockwise)
# screen.onkey(key="space",fun=clear_screen)












screen.exitonclick()