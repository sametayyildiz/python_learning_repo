import turtle as t 

STARTING_POS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake():
    def __init__(self) :
        self.all_turtle = []
        self.create_snake()
        self.head_snake = self.all_turtle[0]

    def create_snake(self):
        for position in STARTING_POS:
            self.add_segment(position)

    def add_segment(self,position):
        new_turtle = t.Turtle()
        new_turtle.penup()
        new_turtle.shape("square")
        #new_turtle.shapesize(1,1)
        new_turtle.color("white")
        new_turtle.goto(position)
        self.all_turtle.append(new_turtle)

    def extend(self):
        self.add_segment(self.all_turtle[-1].position())


    def move (self):
        for turtles in range(len(self.all_turtle)-1,0,-1):
            new_xcor = self.all_turtle[turtles-1].xcor()
            new_ycor = self.all_turtle[turtles-1].ycor()
            self.all_turtle[turtles].goto(new_xcor,new_ycor)
        self.head_snake.forward(MOVE_DISTANCE)
        
    def up_fun (self):
        if self.head_snake.heading() == DOWN :
            pass
        else :
            self.head_snake.setheading(UP)

    def right_fun (self):
        if self.head_snake.heading() == LEFT :
            pass
        else :        
            self.head_snake.setheading(RIGHT)

    def left_fun (self):
        if self.head_snake.heading() == RIGHT :
            pass
        else :        
            self.head_snake.setheading(LEFT)

    def down_fun (self):
        if self.head_snake.heading() == UP :
            pass
        else :        
            self.head_snake.setheading(DOWN)



"""
    def clean_fun ():
        losha.setpos(x=0,y=0)
        losha.clear()
"""
