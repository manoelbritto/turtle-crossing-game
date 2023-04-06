from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1, 1.6)
        self.color(random.choice(COLORS))
        # self.move_car()
        self.goto(300, 0)

    def move_car(self):
        self.setheading(180)
        # self.pendown()
        new_x = self.xcor() - MOVE_INCREMENT
        self.goto(new_x,self.ycor())