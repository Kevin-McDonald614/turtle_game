from turtle import Turtle

FONT = ("Courier", 24, "normal")

# Constructor for the scoreboard, which initializes the scoreboard level to 1.
# And updates the scoreboard to increase level for each completed level.
class Scoreboard(Turtle):#
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=250)
        self.update_scoreboard()

    # Clears the old score and writes the updated score.
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    # Increases scoreboard by 1 for each completed level.
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    # Game over, returns the character to the bottom center of screen,
    # And outputs GAME OVER to the user in the middle of the screen.
    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", align="center", font=FONT)
