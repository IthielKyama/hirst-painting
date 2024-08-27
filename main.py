from turtle import Turtle, Screen
import random

color_list = [(230, 227, 225), (229, 223, 226), (217, 227, 220), (195, 172, 121), (222, 227, 232), (157, 97, 59), (185, 159, 52), (9, 53, 77), (125, 37, 25), (55, 33, 27), (110, 69, 85), (118, 162, 175), (27, 118, 164), (74, 35, 43), (85, 138, 67), (10, 62, 44), (71, 153, 130), (121, 35, 40), (182, 98, 82), (207, 202, 146)]

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
