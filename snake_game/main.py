import turtle as t 
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

my_screen = t.Screen()
my_screen.setup(width=600,height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0) 

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

my_screen.listen()
my_screen.onkey(key="Up", fun=snake.up_fun)
my_screen.onkey(key="Right", fun=snake.right_fun)
my_screen.onkey(key="Left", fun=snake.left_fun)
my_screen.onkey(key="Down", fun=snake.down_fun)

game_is_on = True

while game_is_on:
    my_screen.update()
    time.sleep(0.2)
    snake.move()
    if snake.head_snake.distance(food) < 15 :
        food.refresh()
        scoreboard.score_cal()
        snake.extend()
        
    
    if snake.head_snake.xcor() > 300 :
        game_is_on = False
        scoreboard.game_over()
    elif snake.head_snake.ycor() > 300 :
        game_is_on = False    
        scoreboard.game_over()
    elif snake.head_snake.xcor() < -300 :
        game_is_on = False    
        scoreboard.game_over()
    elif snake.head_snake.ycor() < -300 :
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.all_turtle[1::1]: 
        if snake.head_snake.distance(segment) < 10 :
            game_is_on = False
            scoreboard.game_over()


my_screen.exitonclick()