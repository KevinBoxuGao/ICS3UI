

#FIVE QUIZ QUESTIONS  (you can change these if you want)
q1 = "What is Mr. Schattman's favourite video game? "
q2 = "Which famous irrational number starts with the digits 2.71828...? "
q3 = "After the Soviet Union, which country suffered the most number of deaths in World War 2? "
q4 = "What survival game features the main character steve? "
q5 = "What operating system is Linus Torvalds known for? "


#MAKING AN ARRAY OUT OF THE QUESTIONS
questions = [q1, q2, q3, q4, q5]
numQuestions = len( questions )


#THE FIVE CORRECT ANSWERS
a1 = "World of Warcraft"
a2 = "e"
a3 = "China"
a4 = "Minecraft"
a5 = "Linux"

#Hints
h1 = "The famous game Blizzard Entertainment is known for "
h2 = "Is only a single letter "
h3 = "A country in Asia "
h4 = "This games features a distinct block art style "
h5 = "Is similar in spelling to Linus "

hints = [h1,h2,h3,h4,h5]


#MAKING AN ARRAY OUT OF THE CORRECT ANSWERS
correctAnswers = [a1, a2, a3, a4, a5]


#THE USER TAKES THE QUIZ.  STORE THEIR RESPONSES IN THE ARRAY userGuesses
userGuesses = []

for i in range(numQuestions):
    print(questions[i])
    answer = input("Type your answer: ")
    if answer == "hint":
        print(hints[i])
        answer = input("Type your answer: ")
    userGuesses.append(answer)

#THE PROGRAM MARKS THE QUIZ AND TELLS THE USER WHICH ONES THEY GOT RIGHT
scoreSoFar = 0

for i in range( numQuestions ):
    if correctAnswers[i] == userGuesses[i]:
        scoreSoFar = scoreSoFar + 1
    
print(scoreSoFar)
#TELL THE USER HIS/HER FINAL SCORE
