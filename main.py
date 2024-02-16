import random
from turtle import Turtle,Screen
import colorgram
timmy = Turtle()
screen = Screen()
screen.colormode(255)
# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 34)
color_list = []
timmy.penup()
timmy.setpos(-200, -100)

for _ in colors:
    rgb = _.rgb
    r = rgb.r
    g = rgb.g
    b = rgb.b
    rgb_code = (r, b, g)
    color_list.append(rgb_code)
for _ in range(10):
    default_position = timmy.pos()
    x = default_position[0]
    y = default_position[1]
    for _ in range(10):
        timmy.color(random.choice(color_list))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
    timmy.penup()
    y += 40
    print(y)
    timmy.setpos(x, y)
    timmy.pendown()


timmy.color(random.choice(color_list))
screen.exitonclick()
