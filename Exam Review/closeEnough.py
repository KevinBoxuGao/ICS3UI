from math import *

def isCloseEnough(x1,y1,x2,y2,d):
    if sqrt((x1-x2)**2 + (y1-y2)**2) <= d:
        return True
    else:
        return False

print ( isCloseEnough(0, 10, 5, 6, 8) )