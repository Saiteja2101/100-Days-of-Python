from turtle import Screen
from man import Man
from car import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Car Crossing Game")
screen.tracer(0)

man = Man()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(man.move_up, "Up")
screen.onkey(man.move_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    car_manager.remove_offscreen_cars()

    # 🚗 Collision detection
    for car in car_manager.cars:
        if car.distance(man) < 20:
            game_is_on = False
            scoreboard.game_over()

    # 🏁 Level complete
    if man.reached_finish():
        man.reset_position()
        car_manager.increase_speed()
        scoreboard.increase_level()

screen.exitonclick()
