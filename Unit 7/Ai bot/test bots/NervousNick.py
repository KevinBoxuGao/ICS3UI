from random import *

#STRATEGY SUMMARY:  THROW, RELOAD, THROW, RELOAD, THROW, RELOAD, etc.

def getMove( myScore, myBalls, myDucksUsed, myMovesSoFar,
                        oppScore, oppBalls, oppDucksUsed, oppMovesSoFar ):

    if len(myMovesSoFar) == 0:  #THROW ON THE FIRST ROUND
        return "THROW"

    else:  #FOR ROUNDS 2-30...
        if myMovesSoFar[-1] == "THROW":  #IF I THREW LAST ROUND, THEN RELOAD THIS ROUND  
            return "RELOAD"
        
        else:
            return "THROW"  #IF I RELOADED LAST ROUND, THEN THROW THIS ROUND  


#L[-1] means the last item in array L







    
