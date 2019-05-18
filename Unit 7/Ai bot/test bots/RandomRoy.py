from random import *

#STRATEGY:  JUST PICK RANDOMLY, MAKING SURE THAT I DON'T LOSE BY CHEATING

def getMove( myScore, mySnowballs, myDucksUsed, myMovesSoFar,
             oppScore, oppSnowballs, oppDucksUsed, oppMovesSoFar ):

    if mySnowballs == 0:       #If I'm out of snowballs...
        if myDucksUsed < 5:    #...and if I have ducks left, then pick between DUCK and RELOAD
            return choice([ "DUCK", "RELOAD" ])
        
        else:                  #...otherwise I must RELOAD because I'm out of ducks and snowballs
            return "RELOAD"
        

    elif mySnowballs == 10:    #If I'm at the snowball limit...
        if myDucksUsed < 5:    #...and if I have ducks left, then pick randomly between DUCK and THROW
            return choice([ "DUCK", "THROW" ])
        
        else:                  #...otherwise I must THROW because I have 10 snowballs and I'm out of ducks 
            return "THROW"
        
       
    else:                      #If I have a few snowballs...
         if myDucksUsed < 5:   #...and have ducks left, then just pick randomly
            return choice([ "THROW", "DUCK", "RELOAD" ])
        
         else:                 #...otherwise, I can't duck, so pick randomly between THROW and RELOAD
            return choice([ "THROW", "RELOAD" ])







    
