from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_score()

    def update_score(self):
        self.write(f"Right Score: {self.r_score} , Left Score: {self.l_score}", font= FONT, align= ALIGNMENT)


    def right_increase_score(self):
        self.r_score += 1
        self.clear()
        self.update_score()

    def left_increase_score(self):
        self.l_score += 1
        self.clear()
        self.update_score()