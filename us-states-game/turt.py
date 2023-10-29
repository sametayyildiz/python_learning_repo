import turtle

class TurtleCase ():
    def __init__(self,position_x,position_y,text):
        self.position_x = position_x
        self.position_y = position_y
        self.text = text

    def turtlec (self):
        my_turtle = turtle.Turtle()
        my_turtle.penup()
        my_turtle.hideturtle()
        my_turtle.color("black")
        my_turtle.goto(self.position_x,self.position_y)
        my_turtle.write(self.text)


    
        
