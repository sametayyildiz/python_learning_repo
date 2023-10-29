from turtle import Turtle
ALLIGMENT = "center"
FONT = ('Arial', 12, 'normal')
with open("data.txt","r") as data_file :
    old_sc = data_file.read()

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.score = 0
        self.high_score = int(old_sc)
        self.write(f"Score = {self.score} High Score = {self.high_score} ", align=ALLIGMENT, font=FONT)


    def high_s (self):
        with open("data.txt","w") as data_file :
            data_file.write(f"{self.high_score}")


    def game_over (self):
        self.goto(0,0)
        self.write(" GAME OVER  ", align=ALLIGMENT, font=FONT)


    def score_cal (self):
        self.clear()
        self.score += 1 
        if self.score > self.high_score :
            self.high_score = self.score
            self.high_s()

        self.write(f"Score = {self.score} High Score = {self.high_score}", align=ALLIGMENT, font=FONT)
        


