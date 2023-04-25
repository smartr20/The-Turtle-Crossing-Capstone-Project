from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.level = 1
        self.write_screen()

    def level_up(self):
        self.level += 1
        self.write_screen()

    def write_screen(self):
        self.clear()
        self.write(f"level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(-100, 0)
        self.write("GAME OVER", align="left", font=FONT)
