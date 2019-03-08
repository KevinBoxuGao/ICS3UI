import turtle

x = turtle.Pen()
y = turtle.Pen()
z = turtle.Pen()
a = turtle.Pen() 
b = turtle.Pen()
c = turtle.Pen()


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

b.width(1)
b.speed(1000)
b.shape("turtle")
b.color("green")

b.width(1)
b.speed(1000)
b.shape("turtle")
b.color("yellow")

for i in range(10000):
    x.forward(i)
    y.forward(i)
    z.back(i)
    a.back(i)
    b.forward(i)
    c.forward(i)
    x.right(61)
    y.left(61)
    z.right(61)
    b.left(91)
    c.right(91)
    a.left(61)
    
