import turtle
import pandas
screen = turtle.Screen()
screen.title("US-states-game")
image="./DAY-25/US_STATES-GAME/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# answer_state= screen.textinput(title="Guess The State", prompt="What's another state? ")

# print(answer_state)

data=pandas.read_csv("./DAY-25/US_STATES-GAME/50_states.csv")
all_states=data.state.to_list()
guessed_states=[]

while len(guessed_states)<50:
    
    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 states Correct",
    prompt="What's another state's namae").title()
    

    if answer_state== "Exit":
        missing_states= [state for state in all_states if state not in guessed_states]
        new_data= pandas.DataFrame(missing_states)
        new_data.to_csv("./DAY-25/US_STATES-GAME/States_to_learn.csv")
        break
    
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        ans_row=data[data["state"] == answer_state]
        t.goto(int(ans_row.x),int(ans_row.y))
        t.write(answer_state)





