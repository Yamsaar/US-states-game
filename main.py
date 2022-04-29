import turtle
import pandas


screen = turtle.Screen()
screen.title("wellcome to the USA states game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
df_data = pandas.read_csv("50_states.csv")
us_states = df_data.state.to_list()

states_list = []

while len(states_list) < 50:
    chose_state = screen.textinput(title=f"{len(states_list)}/50 Guess states",
                                   prompt="please enter state's name if you know").title()
    if chose_state == "Exit":
        the_missing_states = []
        for state in us_states:
            if state not in states_list:
                the_missing_states.append(state)

        new_df_data = pandas.DataFrame(the_missing_states)
        # generate a dataframe csv file with all the missing states
        new_df_data.to_csv("states_to_study.csv")
        break

    if chose_state in us_states:
        states_list.append(chose_state)
        player_choice = turtle.Turtle()
        player_choice.penup()
        player_choice.hideturtle()
        data_state = df_data[df_data.state == chose_state]
        player_choice.goto(int(data_state.x), int(data_state.y))
        player_choice.write(chose_state)


screen.exitonclick()
