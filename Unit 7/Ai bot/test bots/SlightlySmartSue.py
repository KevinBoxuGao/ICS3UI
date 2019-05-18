from random import *

#STRATEGY SUMMARY:  DON'T DUCK IF THE OPPONENT HAS NO SNOWBALLS. OTHERWISE, PICK RANDOMLY.

def getMove( myScore, mySnowballs, myDucksUsed, myMovesSoFar,
             oppScore, oppSnowballs, oppDucksUsed, oppMovesSoFar ):

    if mySnowballs == 10:  #I have 10 snowballs, so I must throw
        return "THROW"

    elif oppSnowballs > 0: #If opponent does have snowballs...
        
        if mySnowballs == 0: #...and if I have no snowballs left

            if myDucksUsed == 5: #...and if I have no ducks left either, then must RELOAD
                return "RELOAD"
            
            else:                #...otherwise, pick between DUCK and RELOAD
                return choice([ "DUCK", "RELOAD" ])
        
        elif myDucksUsed == 5: #If my opponent and I both have snowballs left, but I'm out of ducks
            return choice([ "THROW", "RELOAD" ])
                
        else: #I have no restrictions
            return choice([ "THROW", "DUCK", "RELOAD" ])



    else:  #If my opponent is out of snowballs, then don't duck!
        if mySnowballs == 0:
            return "RELOAD"
        
        else:
            return choice([ "RELOAD", "THROW" ])


    
