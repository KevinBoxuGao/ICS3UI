#THIS GAME LETS THE USER PLAY A DICE ROLLING GAME UNTIL HE/SHE GOES BUST, WINS OVER $1000 OR QUITS

#SET UP
from random import *
print("This is a dice rolling game.  You have $100 to start.")
print("If your  roll a total of 7 or 11, you win double your bet.")
print("If you roll double, you break even.")
print("Otherwise, you lose your bet." + "\n")

balance = 100
playAgain = "y"


#GAME LOOP. THIS REPEATS FOR AS LONG AS THE USER'S BALANCE IS BETWEEN $0 AND $1000 AND THE USER WANTS TO KEEP PLAYING
while 0 < balance < 1000 and playAgain in ["yes", "YES", "Yes", "y", "Y", "sure"]:
    bet = int(input( "Enter your bet: $"))

    while bet < 0 or bet > balance:
        if bet < 0:
            print("you need to bet a postive amout")
            bet = int(input( "Enter your bet: $"))
        else:
            print("you don't have the funds to do that")
            bet = int(input( "Enter your bet: $"))
            
    die1 = randint(1,6) #GET TWO RANDOM DIE ROLLS
    die2 = randint(1,6)

    dieTotal = die1 + die2

    print( "\n" + "You rolled a", die1, "and a", die2)

    if dieTotal == 7 or dieTotal == 11: #PLAYER WINS DOUBLE WHAT THEY BET
        winAmount = 2*bet
        print( "You win $" + str( winAmount ) )
        balance = balance + winAmount

    elif die1 == die2: #PLAYER BREAKS EVEN
        print( "You broke even" )

    else: #PLAYER LOSES THEIR BET
        print( "You lose $" + str(bet) )
        balance = balance - bet

    print("You now have $" + str(balance) + "\n")

    playAgain = input("Play again? (y/n)") #ASK PLAYER IF THEY WANT TO KEEP PLAYING
    



#######
#THE LOOP IS NOW FINISHED. NOW WE USE AN IF-STATEMENT TO DETERMINE WHY THE LOOP STOPPED, AND GIVE AN APPROPRIATE RESPONSE
#######

if balance >= 1000:
    print("Congratulations! You have reached $1000!")

elif balance <= 0:          
    print("Sorry, you have gone bust.")

else: #THE USER QUIT
    print("Giving up so soon?!  Well, okay.  Your final balance is $" + str(balance))
