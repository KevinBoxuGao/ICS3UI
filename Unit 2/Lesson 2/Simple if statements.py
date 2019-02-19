grade = int(input("enter your grade level: "))
if 1 <= grade <= 6:
    print("Elementary school")
elif 7 <= grade <= 8:
    print("Middle school")
elif 9 <= grade <= 12:
    print("High school")
else:
    print("I don't know what school level you're in.")
