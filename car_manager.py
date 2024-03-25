from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]  # The different colors a car could possibly be.
STARTING_MOVE_DISTANCE = 5  # The starting speed for which a car moves on the first level
MOVE_INCREMENT = 10  # Continuously increases the speed of cars each level by 10 pixels.


class CarManager:
    # Constructor for the list of cars created in the current game.
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE  # Have all the cars move at the same starting speed.

    def create_car(self):
        random_chance = random.randint(1, 5)  # Generates a random number for frequency of cars.
        if random_chance == 1:  # If random number ==1, create the car. Or else wait until it does reach 1 to make car.
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))  # Randomly choose color of vehicle.
            random_y = random.randint(-250, 250)  # Randomly put car in range from top to bottom of screen.
            new_car.goto(x=300, y=random_y)   # Places the car at a random vertical position, right side of screen.
            self.all_cars.append(new_car)  # Adds car to the collection of cars in the current game.

    # Moves all cars from right side of screen to left.
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    # When you level up, the car movement increases speed.
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
