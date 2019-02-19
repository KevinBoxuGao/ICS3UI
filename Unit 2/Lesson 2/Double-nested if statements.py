credits = int(input("How many credits have you earned? "))
if credits >= 30:
    literacy = input("Have you passed the Grade 10 literacy test, type T or F ")
    if literacy == "T":
        hours = int(input("How many volunteer hours do you have completed "))
        if hours >= 40:
            print("You can graduate!")
        else:
            print("You need",str(40-hours),"volunteer hours to graduate")
    else:
        print("You can't graduate without passing the lit test")
else:
    print("You can't graduate yet because you need",str(30-credits),"more credits")
