from math import *
def slope(x1, y1, x2, y2):
    if x1 == x2:
        return "undefined"
    else:
        return (y2 - y1)/(x2 - x1)

while True:
    orientation = input("enter either clockwise or counterclockwise")
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    x3 = int(input("Enter x3: "))
    y3 = int(input("Enter y3: "))
    x4 = int(input("Enter x4: "))
    y4 = int(input("Enter y4: "))

    lengthAB = sqrt((x2-x1)**2 + (y2-y1)**2)
    lengthBC = sqrt((x3-x2)**2 + (y3-y2)**2)
    lengthCD = sqrt((x4-x3)**2 + (y4-y3)**2)
    lengthDA = sqrt((x1-x4)**2 + (y1-y4)**2)

    diagonalAC = sqrt((x3-x1)**2+(y3-y1)**2)
    diagonalBD = sqrt((x4-x2)**2+(y4-y2)**2)

    #check for parallel sides
    parallelSides = 0

    #AB and CD
    if slope(x1,y1,x2,y2) == slope(x3,y3,x4,y4):
        parallelSides = parallelSides + 1
    #AD and CC
    if slope(x1,y1,x4,y4) == slope(x2,y2,x3,y3):
        parallelSides = parallelSides + 1

    #driver
    if parallelSides == 2:
        if diagonalAC == diagonalBD:
            if lengthAB == lengthBC == lengthCD == lengthDA:
                if slope(x1,y1,x4,y4) == 0:
                    print("horizontal square")
                else:
                    print("tilted square")
            else:
                if slope(x1,y1,x4,y4) == 0:
                    print("horizontal rectangle")
                else:
                    print("tilted rectangle")
        else:
            if lengthAB == lengthBC == lengthCD == lengthDA:
                print("rhombus")
            else:
                if slope(x1,y1,x4,y4) == 0:
                    print("horizontal parallelogram")
                elif slope(x1,y1,x4,y4) == "undefined":
                    print("vertical parallelogram")
                else:
                    print("tilted parallelogram")

    elif parallelSides == 1:
        print("trapezoid")
        
    else:
        if lengthAB == lengthDA and lengthCD == lengthBC:
            print("kite")
        elif lengthDA == lengthCD and lengthAB == lengthBC:
            print("kite")
        else:
            print("quadrilateral")


