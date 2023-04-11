from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.game_start()

    def game_start(self):
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)

