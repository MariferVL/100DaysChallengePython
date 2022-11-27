import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "us_states2.gif"
screen.addshape(image)
turtle.shape(image)

# get the cors
"""def get_mouse_cors(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_cors)
turtle.mainloop()"""

correct_answers = []
missing_answers = []
StatesData = pd.read_csv("50_states.csv")

while len(correct_answers) < 50:
    guess = screen.textinput(title=f"{len(correct_answers)}/50 Corrects👏🏻", prompt="What's another state's name? 🕵🏻").title()
    if guess == "Exit":
        for state_name in StatesData["state"]:
            if state_name not in correct_answers:
                missing_answers.append(state_name)
        user_data = pd.DataFrame(missing_answers)
        user_data.to_csv("stateTolearn.csv")
        break
    for state_name in StatesData["state"]:
        if guess == state_name:
            check = turtle.Turtle()
            check.hideturtle()
            check.penup()
            info = StatesData[StatesData.state == state_name]
            check.goto(int(info.x), int(info.y))
            check.pencolor("blue")
            check.write(state_name)
            correct_answers.append(guess)










screen.exitonclick()
