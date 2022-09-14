from turtle import Turtle, Screen

downy = Turtle()
screen = Screen()


# moves the turtle object forward
def move_forwards():
    downy.forward(10)


# moves the turtle object backwards
def move_backwards():
    downy.back(10)


# turns the turtle object left
def turn_left():
    downy.setheading(downy.heading() + 10)


# turns the turtle object right
def turn_right():
    downy.setheading(downy.heading() - 10)


# clears the window and sets the turtle object into its initial position
def clear():
    downy.home()
    downy.clear()


# assigns functions to certain keys
screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear, key="c")

screen.exitonclick()
