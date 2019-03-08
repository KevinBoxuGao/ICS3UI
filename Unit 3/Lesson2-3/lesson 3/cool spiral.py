import turtle

x = turtle.Pen()
y = turtle.Pen()
z = turtle.Pen()
a = turtle.Pen()

x.width(1)
x.speed(1000)
x.shape("turtle")
x.color("red")

y.width(1)
y.speed(1000)
y.shape("turtle")
y.color("blue")

z.width(1)
z.speed(1000)
z.shape("turtle")
z.color("purple")

a.width(1)
a.speed(1000)
a.shape("turtle")
a.color("cyan")

for i in range(10000):
    x.forward(i)
    y.forward(i)
    z.back(i)
    a.back(i)
    x.right(61)
    y.left(61)
    z.right(61)
    a.left(61)





