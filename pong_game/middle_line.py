from turtle import Turtle

class MiddleLine (Turtle):
    def __init__(self) :
        super().__init__()
        self.all_line = []

    def line (self):
        GOTO_X = -300
        
        for x in range(30):
            lineturtle = Turtle()
            lineturtle.speed(0)
            lineturtle.shapesize(0.2)
            lineturtle.shape("square")
            lineturtle.color("white")
            lineturtle.penup()
            lineturtle.shapesize(0.2)
            lineturtle.goto(0,GOTO_X)
            GOTO_X =  GOTO_X + 20
            self.all_line.append(lineturtle)




