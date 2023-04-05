from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def game_ove(self):
        self.goto(0, 0)
        self.write(f"Game Over", True, align=ALIGN, font=FONT)