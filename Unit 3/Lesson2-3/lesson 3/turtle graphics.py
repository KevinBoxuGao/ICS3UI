import turtle

    
x = turtle.Pen()
window = turtle.Screen()
x.width(3)
x.color("black")


def click_handler(x,y):
    window.onscreenclick(None)
    x.setheading(x.towards(x,y))
    x.goto(x,y)
    window.onscreenclick(click_handler)

window.onscreenclick(click_handler)


window.listen()

window.mainloop()


