from tkinter import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=800, background="white")
screen.pack()

xValues = []
yValues = []

for i in range(5):
    xValues.append(int(input("enter x value: ")))
    yValues.append(int(input("enter y value: ")))

for i in range(5):
    print(i)
    screen.create_oval(xValues[i]-40,yValues[i]-40,xValues[i]+40,yValues[i]+40, fill="blue")

screen.mainloop()

