from math import *
x1 = int(input(“Enter y1: ”))
y1 = int(input(“Enter x2: ”))
x2 = int(input(“Enter x1: ”))
y2 = int(input(“Enter y1: ”))
x3 = int(input(“Enter x2: ”))
y3 = int(input(“Enter x1: ”))
x4 = int(input(“Enter y1: ”))
y4 = int(input(“Enter x2: ”))

lengthAB = sqrt(abs(x2-x1)**2 + abs(y2-y1)**2))
lengthBC = sqrt(abs(x3-x2)**2 + abs(y3-y2)**2))
lengthCD = sqrt(abs(x4-x3)**2 + abs(y4-y3)**2))
lengthDA = sqrt(abs(x1-x4)**2 + abs(y1-y4)**2))

diagonalAC = sqrt(lengthAD**2+lengthCD**2)
diagonalBD = sqrt(lengthAD**2+lengthAB**2)

def slope(x1, y1, x2, y2):
    if x1 == x2:
        return "undefined"
    else:
        return (y4 – y3)/(x4 – x3)
