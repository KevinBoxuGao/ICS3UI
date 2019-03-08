import turtle
t = turtle.Pen()

t.speed(0)
t.width(4)

for y in range(100):
    for direction in "LRDDRLDRLDRLDL": #try changing this
        
        if direction == "L":
            t.left(95)
            t.color("green")
            t.width(3)
            t.forward(11) #try changing this
            
        elif direction == "R":
            t.right(90)
            t.color("hot pink")
            t.width(3)
            t.forward(13) #try changing this
            
        elif direction == "D":
            t.right(45)
            t.color("dark blue")
            t.width(3)
            t.forward(17) #try changing this


                    
