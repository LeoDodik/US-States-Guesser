import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
states = data["state"].tolist()  # Convert the 'state' column to a list
coordinates_x = data["x"].tolist()
coordinates_y = data["y"].tolist()
print(coordinates_x)
print(coordinates_y)

state_turtles = {}

import pandas as pd
import turtle

# Assuming you have defined 'states', 'coordinates_x', and 'coordinates_y' somewhere in your code

correct_guesses = []

# Create a DataFrame to store correct guesses
df = pd.DataFrame(columns=['Correct Guesses'])

# Specify the file path where you want to save the CSV file
file_path = "correct_guesses.csv"

# Function to update CSV file with correct guesses
def update_csv(correct_guesses, file_path):
    df = pd.DataFrame({'Correct Guesses': correct_guesses})
    df.to_csv(file_path, index=False)

score = 0
while True:
    answer_state = screen.textinput(title=f"{score}/50 Correct", prompt="What's another state's name?")

    if answer_state in states and answer_state not in correct_guesses:
        index = states.index(answer_state)
        x = coordinates_x[index]
        y = coordinates_y[index]

        state_turtles[answer_state] = turtle.Turtle()
        state_turtles[answer_state].penup()
        state_turtles[answer_state].hideturtle()
        state_turtles[answer_state].goto(x, y)
        state_turtles[answer_state].write(answer_state, align="center", font=("Arial", 8, "normal"))

        score += 1
        correct_guesses.append(answer_state)
        update_csv(correct_guesses, file_path)
        print(correct_guesses)

    if score >= 50:  # Assuming the game ends after 50 correct guesses
        break

screen.exitonclick()
