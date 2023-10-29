from turtle import Turtle
import random 

DEGREE = [45,-45,225,135,45,-45,225,135,45,-45,225,135]

class Ball (Turtle):
    def __init__(self) :
        super().__init__()


    def ball_create (self):
        self.ball = Turtle()
        self.ball.right(random.choice(DEGREE))
        #self.ball.right(225)
        self.ball.speed(0)
        self.ball.shapesize(1)
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        
            
    def ball_move (self):
        self.ball.forward(20)  

    
    def ball_move_ex (self):
        self.ball.forward(1)  


    def ball_change_r (self):
        self.ball.right(90)

    def ball_change_l (self):
        self.ball.left(90)

    def ball_call_back (self):
        self.ball.goto(0,0)
