import turtle
clrs = ["orange", "red", "pink", "yellow", "blue", "green"]

screen = turtle.Screen()
trl = turtle.Turtle()
trl.speed(10)
screen.bgcolor("black")

for x in range(180):
    trl.pencolor(clrs[x % 6])
    trl.width(x/5+1)
    trl.forward(x)
    trl.left(20)
