from turtle import Turtle

class ScoreBoard (Turtle):
    def __init__(self) :
        super().__init__()
        self.score_right = 0
        self.score_left = 0
        self.text_score_right = Turtle()
        self.text_score_left = Turtle()

    def score_board_right (self):
        self.text_score_right.color("white")
        self.text_score_right.hideturtle()
        self.text_score_right.penup()
        self.text_score_right.goto(-50,250)
        self.text_score_right.write(f"{self.score_right}", font=("Arial", 30, "normal"))
   

    def score_board_left (self):
        self.text_score_left.color("white")
        self.text_score_left.hideturtle()
        self.text_score_left.penup()
        self.text_score_left.goto(30,250)
        self.text_score_left.write(f"{self.score_left}", font=("Arial", 30, "normal"))


    def s_b_r_clear (self):
        self.text_score_right.clear()


    def s_b_l_clear (self):
        self.text_score_left.clear()

    def g_o_s (self):
        g_o_s = Turtle()
        g_o_s.color("white")
        g_o_s.hideturtle()
        g_o_s.penup()
        g_o_s.write(" GAME OVER ",align="center", font=("Arial", 50, "normal"))

