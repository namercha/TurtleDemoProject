import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

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
# colors = ["blue", "cyan", "pale green", "orange", "red", "violet",
#           "blue violet", "indigo"]


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
#
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(40)
#     tim.setheading(random.choice(directions))


# Draw a spirograph
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")
tim.color(random_color())
tim.circle(100)

screen = t.Screen()
screen.exitonclick()

