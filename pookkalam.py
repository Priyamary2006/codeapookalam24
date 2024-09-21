import turtle

s = turtle.Turtle()
s.speed(100)

s.forward(200)
s.left(90)
s.color('dark green', 'dark green')
s.begin_fill()
s.circle(200)
s.end_fill()

s.left(90)
s.forward(18)
s.right(90)
s.color('orange', 'orange')
s.begin_fill()
s.circle(180)
s.end_fill()

s.left(90)
s.forward(10)
s.right(90)
s.color('magenta', 'magenta')
s.begin_fill()
s.circle(170)
s.end_fill()

s.left(90)
s.forward(170)
s.color('gold', 'gold')

s.begin_fill()
for i in range(30):
    s.left(12)
    s.forward(90)
    s.left(90)
    s.forward(90)
    s.left(90)
    s.forward(90)
    s.left(90)
    s.forward(90)
    s.left(90)
s.end_fill()

s.left(30)
s.color('khaki', 'khaki')

s.begin_fill()
for i in range(30):
    s.left(12)
    s.forward(85)
    s.left(90)
    s.forward(85)
    s.left(90)
    s.forward(85)
    s.left(90)
    s.forward(85)
    s.left(90)
s.end_fill()

s.left(30)
s.color('dark red', 'dark red')

s.begin_fill()
for i in range(30):
    s.left(12)
    s.forward(100)
    s.left(90)
    s.forward(100)
    s.left(90)
    s.forward(100)
    s.left(90)
    s.forward(100)
    s.left(90)
s.end_fill()

s.left(30)
s.color('lime green', 'lime green')

s.begin_fill()
for i in range(30):
    s.left(12)
    s.forward(90)
    s.left(90)
    s.forward(90)
    s.left(90)
    s.forward(90)
    s.left(90)
    s.forward(90)
    s.left(90)
s.end_fill()

s.left(30)
s.color('khaki', 'khaki')

s.begin_fill()
for i in range(30):
    s.left(12)
    s.forward(85)
    s.left(90)
    s.forward(85)
    s.left(90)
    s.forward(85)
    s.left(90)
    s.forward(85)
    s.left(90)
s.end_fill()

for i in range(4):
    for colours in {"gold", "orange"}:
        s.speed(100)
        s.color(colours)
        s.begin_fill()
        s.circle(50)
        s.left(50)
        s.end_fill()

for i in range(8):
    s.begin_fill()
    s.color("dark red", "dark red")
    s.circle(40)
    s.left(50)
    s.end_fill()

turtle.lt(30)
turtle.pen(pencolor="orange", pensize="1")


def square(size):
    for i in range(4):
        turtle.fd(size)
        turtle.lt(90)


for i in range(6):
    turtle.begin_fill()
    if i % 2 == 0:
        turtle.pen(pencolor="yellow", pensize="1")
        turtle.fillcolor("yellow")
    else:
        turtle.pen(pencolor="orange", pensize="1")
        turtle.fillcolor("orange")
    square(40)
    turtle.rt(60)
    turtle.end_fill()

s.penup()

s.forward(600)

turtle.mainloop()
