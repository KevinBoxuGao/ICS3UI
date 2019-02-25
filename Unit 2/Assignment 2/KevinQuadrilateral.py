################################################################################
#Programmer: Kevin Gao                                                         #          
#Project: Unit 2 Assignment 2: Quadrilateral Solver                            #
#Class: ICS3UI                                                                 #              
################################################################################
from math import *

def slope(x1, y1, x2, y2):
    if x1 == x2:
        return "undefined"
    else:
        return (y2 - y1)/(x2 - x1)

while True:
    #point A
    x1 = int(input("Enter x1: ")) 
    y1 = int(input("Enter y1: "))
    #point B
    x2 = int(input("Enter x2: ")) 
    y2 = int(input("Enter y2: "))
    #point C
    x3 = int(input("Enter x3: ")) 
    y3 = int(input("Enter y3: "))
    #point D
    x4 = int(input("Enter x4: ")) 
    y4 = int(input("Enter y4: "))

    #create an list of the points and uses it to create a list of unique points
    points = [[x1,y1],[x2,y2],[x3,y3],[x4,y4]]
    uniquepoints = []
    for i in points:
        if i not in uniquepoints:
            uniquepoints.append(i)

    if len(uniquepoints) < 4: #check to see there are no points that overlap
        print("O no, two points overlap, please try to input a quadrilateral")
    else:
        lengthAB = sqrt((x2-x1)**2 + (y2-y1)**2)
        lengthBC = sqrt((x3-x2)**2 + (y3-y2)**2)
        lengthCD = sqrt((x4-x3)**2 + (y4-y3)**2)
        lengthDA = sqrt((x1-x4)**2 + (y1-y4)**2)

        diagonalAC = sqrt((x3-x1)**2+(y3-y1)**2)
        diagonalBD = sqrt((x4-x2)**2+(y4-y2)**2)

        parallelSides = 0 
        #Check if AB and CD are parallel sides
        if slope(x1,y1,x2,y2) == slope(x3,y3,x4,y4):
            parallelSides = parallelSides + 1
        #Check if AD and BC are parallel sides
        if slope(x1,y1,x4,y4) == slope(x2,y2,x3,y3):
            parallelSides = parallelSides + 1

        #First check for parallel sides to classify shapes
        if parallelSides == 2: #Square, Rectangle, or rhombus    
            if diagonalAC == diagonalBD: #Squre or Rectangle
                if lengthAB == lengthBC == lengthCD == lengthDA:
                    if slope(x1,y1,x4,y4) == 0 or slope(x1,y1,x4,y4) == "undefined": #checks if one side is vertical or horizontal to find if square is horizontal to x axis 
                        print("horizontal square")
                    else
                        print("tilted square")
                else:
                    if slope(x1,y1,x4,y4) == 0 or slope(x1,y1,x4,y4) == "undefined": #same as above
                        print("horizontal rectangle")
                    else:
                        print("tilted rectangle")

            else:
                if lengthAB == lengthBC == lengthCD == lengthDA:
                    print("rhombus")
                else:
                    #check for both possibilities for pair of parallel lines that are horizontal
                    if slope(x1,y1,x2,y2) == 0 and slope(x3,y3,x4,y4) == 0: #lines AB and CD
                        print("horizontal parallelogram")
                    elif slope(x1,y1,x4,y4) == 0 and slope(x2,y2,x3,y3) == 0: #lines AD and BC
                        print("horizontal parallelogram")
                    else:
                        print("tilted parallelogram")
                        
        elif parallelSides == 1: #Trapezoid
            #check for both possibilities for pair of parallel lines that are horizontal
            if slope(x1,y1,x2,y2) == 0 and slope(x3,y3,x4,y4) == 0: #same as above 
                print("horizontal trapezoid")
            elif slope(x1,y1,x4,y4) == 0 and slope(x2,y2,x3,y3) == 0: #same as above 
                print("horizontal trapezoid")
                
            #check for both possibilities for pair of parallel lines that are vertical
            elif slope(x1,y1,x2,y2) == "undefined" and slope(x3,y3,x4,y4) == "undefined": #lines AB and CD
                print("vertical trapezoid")
            elif slope(x1,y1,x4,y4) == "undefined" and slope(x2,y2,x3,y3) == "undefined": #lines AD and BC
                print("vertical trapezoid")

            else:
                print("tilted trapezoid")       
            
        else: #Kite or quadrilateral
            #check for two pairs of adjacent sides are equal
            if lengthAB == lengthDA and lengthCD == lengthBC:
                print("kite")
            elif lengthDA == lengthCD and lengthAB == lengthBC:
                print("kite")
            else:
                print("weird quadrilateral")
