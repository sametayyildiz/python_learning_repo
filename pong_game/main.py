import turtle as t 
from middle_line import MiddleLine
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time 


my_screen = t.Screen()
my_screen.setup(1000,600)
my_screen.bgcolor("black")
my_screen.listen()
my_screen.tracer(0)
my_screen.title("Welcome to the pong game!")

middle_line = MiddleLine()
paddle = Paddle()
ball = Ball()
scoreboard = ScoreBoard()

paddle.right_paddle()
paddle.left_paddle()
middle_line.line()
ball.ball_create()


game = True


while game :
    my_screen.update()
    time.sleep(0.1)

    # paddlle right move part 
    paddle.right_paddle_move()
    my_screen.onkey(key="w",fun=paddle.r_p_m_control_up)
    my_screen.onkey(key="s",fun=paddle.r_p_m_control_down)    
    for x in paddle.all_paddle_right:
        if x.ycor() > 280 :
            paddle.r_p_m_control_down()
        if x.ycor() < -280 :
            paddle.r_p_m_control_up()

    # paddle left move part
    paddle.left_paddle_move()
    my_screen.onkey(key="Up",fun=paddle.l_p_m_control_up)
    my_screen.onkey(key="Down",fun=paddle.l_p_m_control_down)    
    for x in paddle.all_paddle_left:
        if x.ycor() > 280 :
            paddle.l_p_m_control_down()
        if x.ycor() < -280 :
            paddle.l_p_m_control_up()

    # ball move part 
    ball_cor_old = ball.ball.xcor()
    ball.ball_move()
    ball_cor_new = ball.ball.xcor()

    if ball.ball.ycor() > 280 :
        if ball_cor_old > ball_cor_new :
            ball.ball_change_l()
        elif ball_cor_new > ball_cor_old :
            ball.ball_change_r()

    if ball.ball.ycor() < -280 :
        if ball_cor_old > ball_cor_new :
            ball.ball_change_r()
        elif ball_cor_new > ball_cor_old :
            ball.ball_change_l()


    # new ball came part 
    if ball.ball.xcor() > 500 :
        ball.ball_call_back()
        scoreboard.score_right += 1

    if ball.ball.xcor() < -500 :
        ball.ball_call_back()      
        scoreboard.score_left += 1


    # detect ball with paddle part
    if paddle.all_paddle_left[0].ycor() < ball.ball.ycor()+50 and paddle.all_paddle_left[9].ycor() > ball.ball.ycor()-50 and 460 < ball.ball.xcor() :
        print("left")
        
        ball_cor_old = ball.ball.ycor()
        ball.ball_move_ex()
        ball_cor_new = ball.ball.ycor()

        if ball_cor_old > ball_cor_new :
            ball.ball_change_r()
        elif ball_cor_new > ball_cor_old :
            ball.ball_change_l()


    if paddle.all_paddle_right[0].ycor() < ball.ball.ycor()+50 and paddle.all_paddle_right[9].ycor() > ball.ball.ycor()-50 and -460 > ball.ball.xcor() :
        print("right")

        ball_cor_old = ball.ball.ycor()
        ball.ball_move_ex()
        ball_cor_new = ball.ball.ycor()

        if ball_cor_old > ball_cor_new :
            ball.ball_change_l()
        elif ball_cor_new > ball_cor_old :
            ball.ball_change_r()



    scoreboard.s_b_r_clear()
    scoreboard.s_b_l_clear()
    
    scoreboard.score_board_left()
    scoreboard.score_board_right()

    #my_screen.onkey(key="r",fun=ball.ball_change_r)
    #my_screen.onkey(key="l",fun=ball.ball_change_l)    

    if scoreboard.score_right == 3 :
        scoreboard.g_o_s()
        game = False

    if scoreboard.score_left == 3 :
        scoreboard.g_o_s()
        game = False


my_screen.exitonclick()
