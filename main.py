import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S states Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)








answer_state = screen.textinput(title="Guess a state", prompt="What's another state?")
print(answer_state.title())

data = pandas.read_csv("50_states.csv")
with open("50_states.csv") as state:
    states = data["state"]
    print(states)

turtle.mainloop()


