from turtle import Turtle, Screen
import random

sully = Turtle(shape="turtle")
bully = Turtle(shape="turtle")
mully = Turtle(shape="turtle")
gully = Turtle(shape="turtle")

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



# for _ in range (0,240):
#     if (-240 < sully.xcor() < 240):
#         sully.penup()
#     # speed = random.san
#         sully.forward(random.randint(0,5))

# # count = 0
# # while count < 500:
# #     count += 1
# #     # sully.speed("fastest")
# #     if (-240 < sully.xcor() < 240):
# #         sully.penup()
# #         sully.forward(random.randint(0,5))
# #     else:
# #        count = 502


# # def move_forward():
# #     sully.forward(100)
# # def move_backward():
# #     sully.backward(90)
# # def move_anticlockwise():
# #     sully.left(45)
# #     sully.circle(100,80)
# # def move_clockwise():
# #     sully.right(45)
# #     sully.circle(100,80)
# # def clear_screen():
# #     sully.clear()
# #     sully.penup()
# #     sully.home()
# #     sully.pendown()


# # screen.listen()
# # screen.onkey(key="w", fun=move_forward)
# # screen.onkey(key="s", fun=move_backward)
# # screen.onkey(key="a", fun=move_anticlockwise)
# # screen.onkey(key="d", fun=move_clockwise)
# # screen.onkey(key="space",fun=clear_screen)












# screen.exitonclick()



# from turtle import Turtle, Screen
# import random

# screen = Screen()
# screen.setup(width=500, height=400)

# user_bet = screen.textinput(
#     "Welcome to TRG",
#     "Place your bets on a turtle (red, orange, yellow, green, blue, black): "
# )

# colors = ["red", "orange", "yellow", "green", "blue", "black"]
# y_positions = [70, 40, 10, -20, -50, -80]

turtles = [sully,bully,mully,gully]

# # Create turtles
# for i in range(6):
#     racer = Turtle(shape="turtle")
#     racer.color(colors[i])
#     racer.penup()
#     racer.goto(-230, y_positions[i])
#     turtles.append(racer)

race_on = True

while race_on:
    for turtle in turtles:
        # Move each turtle forward randomly
        turtle.forward(random.randint(0, 10))

        # Check for winner
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if user_bet and user_bet.lower() == winning_color:
                print(f"You won! The {winning_color.title()} turtle won!")
            else:
                print(f"You lost! The {winning_color.title()} turtle won!")

screen.exitonclick()
