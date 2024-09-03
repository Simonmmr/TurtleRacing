import random
from turtle import Turtle, Screen
from random import randint
screen = Screen()

screen.setup(width=500, height=400)

user_bet = screen.textinput('Make you bet',"Who will win the race?Write the color :")
colors = ["red","orange","yellow","green","blue","violet","purple","black"]
y_positions = [-180, -129, -79, -30, 21, 76, 128 ,178]
game_is_on = True


all_turtles =[]
for turtle_index in range(0,8):
        new_turtle = Turtle(shape='turtle')
        new_turtle.penup()
        new_turtle.color(colors[turtle_index])
        new_turtle.goto(-200, y_positions[turtle_index])
        all_turtles.append(new_turtle)


if user_bet:
    game_is_on = True

while game_is_on:
    for turtle in all_turtles:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        if turtle.xcor() >230:
            game_is_on = False
            screen.clear()
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f" The winner is {winner} turtle and you won!")
            else:
                print(f" The winner is {winner} turtle and you lost!")

screen.exitonclick()
