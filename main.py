from turtle import Turtle, Screen
import random

tim = Turtle()

# tim.color("red")

# Draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)


# Draw a dashed line, 10 paces on and 10 paces off for 15 lines
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# Draw concentric triangle, square, pentagon...decagon
# DEGREES = 360
# colors = ["blue", "cyan", "pale green", "orange", "red", "violet",
#           "blue violet", "indigo"]
# for i in range(3, 11):
#     tim.color(random.choice(colors))
#     for _ in range(i):
#         tim.forward(100)
#         tim.right(DEGREES/i)


# Program a random walk using random colors
colors = ["blue", "cyan", "pale green", "orange", "red", "violet",
          "blue violet", "indigo"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")
for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(40)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
