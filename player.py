from turtle import Turtle

STARTING_POSITION = (0, -280)  # Puts turtle the bottom of the screen in the middle.
MOVE_DISTANCE = 10   # How many pixels the turtle moves per movement.
FINISH_LINE_Y = 280  # The finish line the turtle must cross for the next level.


# Constructor for the turtle.
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    # Moves the turtle character up.
    def move_up(self):
        self.forward(MOVE_DISTANCE)

    # Moves the turtle character down.
    def move_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)

    # Moves the turtle character left.
    def move_left(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())

    # Moves the turtle character right.
    def move_right(self):
        new_x = self.xcor() + 10
        self.goto(new_x, self.ycor())

    # Returns the turtle to the starting line.
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    # Checks to see if the turtle has crossed the finish line threshold.
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


