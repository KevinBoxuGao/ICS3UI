def printSlope(equation):
    xIndex = equation.find('x')
    if xIndex == -1:
        print(0)
    elif xIndex == 2:
        print(1)
    else:
        slopeString = equation[2:xIndex]
        if slopeString == "-":
            print(-1)
        else:
            print(slopeString)

printSlope("y=2x+5") #prints 2
printSlope("y=-1299x+5") #prints -1299
printSlope("y=x+5") #prints 1
printSlope("y=-x+5") #prints -1
printSlope("y=5") #prints 0
