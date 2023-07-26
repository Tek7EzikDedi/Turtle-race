from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
screen.title("Welcome to the turtle zoo!")

all_turtles = []
y = 125
for i in range(6):
    new_turle = Turtle(shape="turtle", )
    new_turle.color(colors[i])
    new_turle.penup()
    new_turle.goto(x=-230, y=y)
    y -= 50
    all_turtles.append(new_turle)
    
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                screen.textinput(title="Winner Winner Chicken Dinner!👍", prompt=f"You've Won! The {winning_color} turtle is winner!")
            else:
                screen.textinput(title="Better Luck Next Time!👎",
                                 prompt=f"You've Lost! The {winning_color} turtle is winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)




screen.exitonclick()