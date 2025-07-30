import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_drawer = turtle.Turtle()
state_drawer.penup()
state_drawer.color('black')
state_drawer.hideturtle()

correct_guesses = []
df = pd.read_csv("50_states.csv")
all_states = df['state'].to_list()

while len(correct_guesses) < 50:
    if len(correct_guesses) == 0:
        title = "Guess the State"
    else:
        title = f"{len(correct_guesses)}/50 States correct"

    answer = screen.textinput(
        title=title,
        prompt="What's another state's name?"
    ).strip().capitalize()

    if answer == 'Exit':
        states_to_learn = [x for x in all_states if x not in correct_guesses]
        pd.DataFrame(states_to_learn).to_csv('states_to_learn.csv')
        break

    if answer in all_states and answer not in correct_guesses:
        correct_guesses.append(answer)

        state_data = df[df['state'] == answer]
        x = int(state_data['x'])
        y = int(state_data['y'])

        state_drawer.goto(x, y)
        state_drawer.write(answer, align='center', font=('Comic Sans MS', 8, 'normal'))

