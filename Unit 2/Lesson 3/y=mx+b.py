m = int(input("enter slope of line: "))
b = int(input("enter the y-intercept: "))

if b == 0:
    bOutput=""
elif b < 0:
    bOutput = str(b)
else:
    bOutput="+"+str(b)
    
if m == 0:
    mOutput = ""
    bOutput = str(b)
elif m == 1:
    mOutput = "x"
elif m == -1:
    mOutput = "-x"
else:
    mOutput = str(m)+"x"
    
print("The equation of the line is y="+mOutput+bOutput)
