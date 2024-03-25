import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create your turtle object.
player = Player()

# Create your car managing object.
car_manager = CarManager()

# Create your scoreboard object.
scoreboard = Scoreboard()

# Have your screen "listen" to what key you press and based on which key you press,
# your turtle will do the corresponding move.
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

# Keep playing the game until you have hit a car.
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car, if there is collision stop game and let user know that the game is over.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:  # 20 pixels is about the size of the car.
            game_is_on = False
            scoreboard.game_over()

    # Detect the player reaching a new level, if so increase scoreboard by 1 and speed up cars.
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

# When you click with your mouse, the game screen will disappear.
screen.exitonclick()