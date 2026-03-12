import turtle
import random


# Screen setup
screen = turtle.Screen()
screen.title("Turtle Racing Game")
screen.bgcolor("lightblue")

# Ask user for bet
user_bet = screen.textinput(
    "Make your bet",
    "Which turtle will win? (red, blue, green, yellow, purple): "
)

# Turtle colors
colors = ["red", "blue", "green", "yellow", "purple"]
y_positions = [-100, -50, 0, 50, 100]

turtles = []

# Create turtles
for i in range(5):
    t = turtle.Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-230, y_positions[i])
    turtles.append(t)

# Start race
race_on = True
while race_on:
    for t in turtles:
        move = random.randint(1, 10)
        t.forward(move)

        if t.xcor() > 220:
            race_on = False
            winning_color = t.pencolor()


# Result
if user_bet == winning_color:
    print(f"🎉 You won! The {winning_color} turtle won the race!")
else:
    print(f"😢 You lost. The {winning_color} turtle won the race.")

screen.exitonclick()