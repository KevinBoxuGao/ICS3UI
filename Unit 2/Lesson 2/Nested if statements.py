light = input("enter traffic light color: ")

if light == "red":
    print("stop")
elif light == "yellow":
    distance = int(input("how close are you from the intersection in m: "))
    if distance < 20:
        print("go")
    else:
        print("stop")
elif light == "green":
    print("go")
else:
    print("pull over and make an appointment with your optometrist")
