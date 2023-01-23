import turtle
import pandas
from state_name import StateName

screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")
state_list = state_data["state"].to_list()
state_num = len(state_data)

corrected_state = []

while len(corrected_state) < state_num:
    answer_state = screen.textinput(title=f"{len(corrected_state)}/{state_num} Correct", prompt="What's another state name?").title()
    if answer_state == "Exit":
        state_to_learn = [state for state in state_list if state not in corrected_state]
        new_data = pandas.DataFrame(state_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        corrected_state.append(answer_state)
        guessed_state = state_data[state_data["state"] == answer_state]
        StateName(answer_state, int(guessed_state.x), int(guessed_state.y))
        state_list.remove(answer_state)

if (len(corrected_state) == state_num):
    StateName("You win!", 0, 10)
StateName("Game over! Click anywhere to exit!", 0 , -20)

screen.exitonclick()
