import turtle as t

t .pen()
t .bgcolor("black")
t .speed(15)
colors = ["red", "purple", "blue", "green", "orange", "yellow"]
for x in range (360):
    t .pencolor(colors[x%6] )
    t .width( x/100+1 )
    t .forward(x)
    t .left(59)
