#! env bin/python
# codding = utf-8
import turtle
import pprint
import math

print('Input a = ')
a = int(input())

print('Input coordinates first point x1 = ')
X1 = int(input())

print('Input coordinates first point y1 = ')
Y1 = int(input())

print('Input number of levels ')
n = int(input())


def get_coordinates(x1, y1, a):
    x2 = x1 + a
    y2 = y1
    x3 = x1 + a/2
    y = math.sqrt(pow(a, 2) - pow(a/2, 2))
    y3 = y1 + y
    return x1, y1, x2, y2, x3, y3

X1, Y1, X2, Y2, X3, Y3 = get_coordinates(X1, Y1, a)


def triangle(x1, y1, x2, y2, x3, y3, N):
    if N > 0:
        x12 = (x1 + x2) // 2
        y12 = (y1 + y2) // 2
        x23 = (x2 + x3) // 2
        y23 = (y2 + y3) // 2
        x31 = (x3 + x1) // 2
        y31 = (y3 + y1) // 2
        turtle.penup()
        turtle.goto(x31, y31)
        turtle.pendown()
        turtle.goto(x12, y12)
        turtle.goto(x23, y23)
        turtle.goto(x31, y31)
        triangle(x1, y1, x12, y12, x31, y31, N - 1)
        triangle(x2, y2, x12, y12, x23, y23, N - 1)
        triangle(x3, y3, x31, y31, x23, y23, N - 1)

turtle.pu()
turtle.setpos(X1, Y1)
turtle.pd()
turtle.forward(a)
turtle.left(120)
turtle.forward(a)
turtle.left(120)
turtle.forward(a)


triangle(X1, Y1, X2, Y2, X3, Y3, n)
turtle.exitonclick()


