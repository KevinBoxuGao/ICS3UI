myFavMovies= ["The Last Jedi", "Zootopia", "51.6 Shades of Grey", "Batman vs. Hello Kitty"] 
print( "You should definitely watch", myFavMovies )
print(myFavMovies[0])
print(myFavMovies[1])
print(myFavMovies[2])
print(myFavMovies[3])

for i in range(4):
    print(myFavMovies[i])

numMovies = len(myFavMovies)
print(numMovies)

for i in range(len(myFavMovies)):
    print(myFavMovies[i])

myFavMovies[3] = "Sponge Bob Goes to the Dentist"
myFavMovies[1] = myFavMovies[1] + " II"  
print( "Wait, I've changed my mind.  You should watch", myFavMovies )

myFavMovies.append( "Twilight 6: They All Die" )
print( "With this addition, the array is now", myFavMovies )

myMarks = [90, 77, 42, 91, 77, 16, 100]
print( "My CS marks so far are", myMarks)

for i in range(len(myMarks)):
    myMarks[i] = myMarks[i] + 10

print("The marks have to raised to", myMarks)

myIndex = myFavMovies.index("51.6 Shades of Grey")
print("SOG is at index", myIndex)

coolTeachers = []  

for numTeachers in range(4):
    teacherName = input("Enter a cool teacher at SJAM: ")
    coolTeachers.append( teacherName )     
print( coolTeachers )


coolTeachers.remove("Mr. Schattman")
print( coolTeachers )
