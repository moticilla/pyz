from turtle import Turtle

t = Turtle()
t.penup()
t.sety(-400)
t.pendown()
t.left(135)
t.forward(450)

for step in range(450):
    t.right(0.5)
    t.forward(3.14159/2)
t.left(180)

for step in range(450):
    t.right(0.5)
    t.forward(3.14159/2)

t.forward(450)

