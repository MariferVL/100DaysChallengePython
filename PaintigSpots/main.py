"""
import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('spotspainting.jpg', 33)

rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
"""
import turtle as t
import random

palette = [(207, 161, 84), (54, 89, 132),
           (146, 91, 39), (139, 26, 49), (222, 207, 106), (132, 176, 202), (46, 55, 103), (170, 158, 39), (157, 45, 82),
           (129, 188, 143), (83, 19, 43), (36, 43, 69), (185, 93, 106), (186, 139, 169), (84, 123, 181), (58, 38, 30),
           (87, 156, 92), (78, 152, 164), (194, 77, 72), (161, 201, 219), (79, 73, 44), (45, 74, 77), (56, 126, 121),
           (218, 176, 187), (220, 182, 168), (170, 206, 175), (179, 188, 213), (47, 74, 73), (143, 38, 36)]

lala = t.Turtle()
lala.shape("turtle")
lala.color("aquamarine", "gold")
lala.pensize(4)
lala.resizemode("auto")
lala.speed(0)
t.colormode(255)


for _ in range(10):

    lala.pencolor(random.choice(palette))
    lala.penup()
    lala.forward(33)
    lala.dot(11, random.choice(palette))




screen = t.Screen()
screen.exitonclick()