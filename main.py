import turtle
import pandas as pd
from turtle import Turtle,Screen
screen=turtle.Screen()
screen.title("U.S.A. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df=pd.read_csv("50_states.csv")
states=df["state"].to_list()
guessed_state=[]
while len(guessed_state)<50:
    answer_state=screen.textinput(title=f"{len(guessed_state)}/50 states correct",prompt="what's another state's name").title()
    if answer_state=="Exit":
        missing_states=[]
        for state in states:
            if state not in guessed_state:
                missing_states.append(state)
        print(missing_states)
        new_data=pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=df[df["state"]==answer_state]
        t.goto(state_data.x.item() , state_data.y.item())
        t.write(answer_state)
        guessed_state.append(answer_state)



screen.exitonclick()
