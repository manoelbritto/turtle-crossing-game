from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 0
        self.penup()
        self.hideturtle()
        self.scoreboard_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", True, align=ALIGN, font=FONT)

    def scoreboard_level(self):
        self.goto(-200, 250)
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", True, align=ALIGN, font=FONT)
