from random import *

#make sure there is not cheating
def canTHROW(mySnowballs):
    if mySnowballs == 0:
        return False
    else:
        return True

def canRELOAD(mySnowballs):
    if mySnowballs == 10:
        return False
    else:
        return True

def canDUCK(myDucksUsed):
    if myDucksUsed == 5:
        return False
    else:
        return True

def getMove(myScore, mySnowballs, myDucksUsed, myMovesSoFar,oppScore, oppSnowballs, oppDucksUsed, oppMovesSoFar ):
    #opening moves
    opening = ["RELOAD", "RELOAD", "THROW"]
    if len(myMovesSoFar) <= 2:     
        return opening[len(myMovesSoFar)]

    #edge cases
    if canTHROW(mySnowballs) == False:
        if oppSnowballs == 0: #logically reload to note waste a duck if both people have no snowballs
            return "RELOAD"

    if canRELOAD(mySnowballs) == False: #if I am at 10 snowballs I should throw
        return "THROW"

    if canDUCK(mySnowballs) == False:
        if canTHROW(mySnowballs): #if I can only reload
            return "RELOAD"

    #based on their score  
    #aggressive strategy
    if oppScore == 0: 
        if canTHROW(mySnowballs) == False: #restricted to only duck or reload
            return chooseMove(0, 5, 95)
        else:
            if oppSnowballs == 0: #don't duck if they have no snowballs
                return chooseMove(100, 0 , 0)
            elif mySnowballs >= 4:
                return chooseMove(90, 0 , 10) #avoid hoarding snowballs
            else:
                if myDucksUsed >= 3: #decrease duck rate
                    if myDucksUsed == 5: #restricted to only throw or reload
                        if mySnowballs > oppSnowballs: #throw rate increase
                            return chooseMove(90,0,10)
                        else:
                            return chooseMove(85,0,10)
                    else:
                        if mySnowballs > oppSnowballs: #throw rate increase
                            return chooseMove(90,0,10)
                        else:
                            return chooseMove(85,5,10)
                else: #decrease duck rate
                    if mySnowballs > oppSnowballs: #throw rate increase
                        return chooseMove(85,5,10)
                    else:
                        return chooseMove(70,10,20)

    #moderate aggression
    elif oppScore == 1: #less reload, more duck
        if canTHROW(mySnowballs) == False: #restricted to only duck or reload
            return chooseMove(0, 35, 65)
        else:
            if oppSnowballs == 0: #don't duck if they have no snowballs
                return chooseMove(85, 0 , 15)
            elif mySnowballs >= 4:
                return chooseMove(95, 0 ,5) #avoid hoarding snowballs 
            else:
                if myDucksUsed >= 3: #decrease duck rate
                    if mySnowballs > oppSnowballs:
                        return chooseMove(85,5,10)
                    else:
                        return chooseMove(75,10,15)
                else:
                    if myDucksUsed >= 3: #decrease duck rate
                        if myDucksUsed == 5: #restricted to only throw or reload
                            if mySnowballs > oppSnowballs: #throw rate increase
                                return chooseMove(77,0,20)
                            else:
                                return chooseMove(72,0,20)
                        else:
                            if mySnowballs > oppSnowballs: #throw rate increase
                                return chooseMove(77,3,20)
                            else:
                                return chooseMove(72,8,20)
                    else: #decrease duck rate
                        if mySnowballs > oppSnowballs: #throw rate increase
                            return chooseMove(72,8,20)
                        else:
                            return chooseMove(65,15,20)

    #safe strategy
    else: #less reload, more duck
        if canTHROW(mySnowballs) == False: #restricted to only duck or reload
            return chooseMove(0, 80, 20)
        else:
            if oppSnowballs == 0: #don't duck if they have no snowballs
                return chooseMove(80, 0 , 20)
            elif mySnowballs >= 4:
                return chooseMove(100, 0 ,0) #avoid hoarding snowballs
            else:
                if myDucksUsed >= 3: #decrease duck rate
                    if myDucksUsed == 5: #restricted to only throw or reload
                        if mySnowballs > oppSnowballs:
                            return chooseMove(90,0,5)
                        else:
                            return chooseMove(85,0,5)
                    else:
                        if mySnowballs > oppSnowballs:
                            return chooseMove(90,5,5)
                        else:
                            return chooseMove(85,10,5)
                else:
                    if mySnowballs > oppSnowballs:
                        return chooseMove(85,10,5)
                    else:
                        return chooseMove(80,20,5)
    
#Chooses move based on given probabilities
def chooseMove(THROWpr, DUCKpr, RELOADpr):
    move = THROWpr * ["THROW"] + DUCKpr * ["DUCK"] + RELOADpr * ["RELOAD"] #create list of 100 items where there are exactly the number of items of each move according to probability
    return choice(move)
        
