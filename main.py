import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract('image.jpg', 20)

color_list = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    new_color = (r, g, b)

    color_list.append(new_color)

screen = Screen()
screen.screensize(2000, 1500)
screen.colormode(255)

t = Turtle()
t.speed("fastest")
t.pensize(20)
random_color = random.choice(color_list)

rows = 0

while rows < 5:
    rows += 1
    for _ in range(9):
        t.pendown()
        t.pencolor(random.choice(color_list))
        t.dot(20, random.choice(color_list))
        t.penup()
        t.forward(50)
        t.pendown()
        t.color(random_color)
        t.pendown()

    t.dot(20, random.choice(color_list))
    t.penup()
    t.left(90)
    t.forward(50)
    t.left(90)

    for _ in range(9):
        t.pendown()
        t.color(random.choice(color_list))
        t.dot(20, random.choice(color_list))
        t.penup()
        t.forward(50)
        t.pendown()
        t.color(random_color)
        t.pendown()

    t.dot(20, random.choice(color_list))
    t.penup()
    t.right(90)
    t.forward(50)
    t.right(90)

t.hideturtle()

screen.exitonclick()
