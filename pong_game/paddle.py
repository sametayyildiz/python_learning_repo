from turtle import Turtle


class Paddle (Turtle):
    def __init__(self) :
        super().__init__()
        self.all_paddle_right = []
        self.all_paddle_left = []       
        
    
    def right_paddle (self):
        goto_y = -50
        for x in range(10):
            r_paddle = Turtle()
            r_paddle.speed(0)
            r_paddle.shapesize(0.5)
            r_paddle.shape("square")
            r_paddle.color("white")
            r_paddle.penup()
            r_paddle.goto(-480,goto_y)
            goto_y =  goto_y + 10
            self.all_paddle_right.append(r_paddle)
        for x_ in range(10):
            self.all_paddle_right[x_].right(-90)           

    def right_paddle_move (self):
        for x in range(10):
            self.all_paddle_right[x].forward(25)

    def r_p_m_control_up (self):
        for x in range(10):        
            self.all_paddle_right[x].setheading(90)

    def r_p_m_control_down (self):
        for x in range(10):        
            self.all_paddle_right[x].setheading(270)

#left ----------------------------------------------------


    def left_paddle (self):
        goto_y = -50
        for x in range(10):
            l_paddle = Turtle()
            l_paddle.speed(0)
            l_paddle.shapesize(0.5)
            l_paddle.shape("square")
            l_paddle.color("white")
            l_paddle.penup()
            l_paddle.goto(480,goto_y)
            goto_y =  goto_y + 10
            self.all_paddle_left.append(l_paddle)
        for x_ in range(10):
            self.all_paddle_left[x_].right(-90)           

    def left_paddle_move (self):
        for x in range(10):
            self.all_paddle_left[x].forward(25)

    def l_p_m_control_up (self):
        for x in range(10):        
            self.all_paddle_left[x].setheading(90)

    def l_p_m_control_down (self):
        for x in range(10):        
            self.all_paddle_left[x].setheading(270)



    
