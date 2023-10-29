import turtle
import pandas as pd 
from turt import TurtleCase

data = pd.read_csv("50_states.csv")
correct_data = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.setup(height=491,width=725)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct = True
correct_answer = 0

while correct :
    answer_state = screen.textinput(title=f"{correct_answer}/50 States Correct",prompt="what is your state name ?")
    
    if answer_state in data["state"].str.lower().values :
        correct_answer += 1 

        index_no = data[data["state"].str.lower()==answer_state].index.values
        
        new_data = correct_data.drop(index_no,inplace=True)

        x_cor = data.loc[index_no[0],"x"]
        y_cor = data.loc[index_no[0],"y"]
        my_turtle = TurtleCase(x_cor,y_cor,answer_state)
        my_turtle.turtlec()

    elif answer_state == "exit" :
        correct = False


correct_data.to_csv("newcsv")