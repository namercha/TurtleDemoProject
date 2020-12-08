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
DEGREES = 360
colors = ["blue", "cyan", "pale green", "orange", "red", "violet",
          "blue violet", "indigo"]
for i in range(3, 11):
    tim.color(random.choice(colors))
    for _ in range(i):
        tim.forward(100)
        tim.right(DEGREES/i)



screen = Screen()
screen.exitonclick()
