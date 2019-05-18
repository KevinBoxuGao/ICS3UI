#mmCount = 0

def getMove( myScore, mySnowballs, myDucksUsed, myMovesSoFar, oppScore, oppSnowballs, oppDucksUsed, oppMovesSoFar ):
    global valueOfWin

    maxDepth = 5 #THE CRUCIAL PARAMETER
    valueOfWin = 999

    roundNumber = len(myMovesSoFar) + 1
     
    if myMovesSoFar == []:
        myLastMove = ""

    else:
        myLastMove = myMovesSoFar[-1]

    #WE STORE A GAME STATE AS AN ARRAY OF STATISTICS
    state = [myScore, mySnowballs, myDucksUsed, oppScore, oppSnowballs, oppDucksUsed, roundNumber]
    
    valueOfWin = 999
    
    myMove = miniMax(state, maxDepth, maxDepth, "me", myLastMove)

    return myMove[1]


#-----------------------------------------------------------------------#
def miniMax(state, n, nMax, whoseTurnItIs, myMove):
    global valueOfWin
    
    e = evalState(state, valueOfWin)
    
    if n==0 or e in [-valueOfWin, valueOfWin]:
        return e

    else:
        if whoseTurnItIs == "me":
            legalMoves = getLegalMoves(state, "me")
            maxEvaluationSoFar = -2*valueOfWin
            bestMove = ""

            for m in legalMoves:
                nextState = getNextState( state, "me", m, "")
                nextEval = miniMax(nextState, n, nMax, "opp", m)
                
                if nextEval > maxEvaluationSoFar:
                    maxEvaluationSoFar = nextEval
                    bestMove = m

            if n == nMax:
                  #print("Finishing with n=nMax")
                  return [maxEvaluationSoFar, bestMove]

            else:
                  return maxEvaluationSoFar
                
        else:
            legalMoves = getLegalMoves(state, "opp")
            minEvaluationSoFar = 2*valueOfWin

            for oppMove in legalMoves:
                nextState = getNextState( state, "opp", myMove, oppMove) 

                nextEval = miniMax(nextState, n-1, nMax, "me", myMove)
                
                if nextEval < minEvaluationSoFar:
                    minEvaluationSoFar = nextEval

            return minEvaluationSoFar


#-----------------------------------------------------------------------#
def getLegalMoves(state, whoseTurnItIs):
    legalMoves = ["THROW", "DUCK", "RELOAD"]
    
    if whoseTurnItIs == "me":
        if state[1] == 0:
            legalMoves.remove( "THROW" )

        if state[1] == 10:
            legalMoves.remove( "RELOAD" )
     
        if state[2] == 5:
            legalMoves.remove( "DUCK" )

    else:
        if state[4] == 0:
            legalMoves.remove( "THROW" )

        if state[4] == 10:
            legalMoves.remove( "RELOAD" )
     
        if state[5] == 5:
            legalMoves.remove( "DUCK" )

    return legalMoves


#-----------------------------------------------------------------------#
def getNextState(state, whoseTurnItIs, myMove, oppMove):
    nextState = list(state)

    if whoseTurnItIs == "me":

        if myMove == "THROW":
            nextState[1] = state[1] - 1

        elif myMove == "DUCK":
            nextState[2] = state[2] +1

        elif myMove == "RELOAD":
            nextState[1] = state[1] + 1

    else:
        if oppMove == "THROW":
            nextState[4] = state[4] - 1

            if myMove == "RELOAD":
                nextState[3] = state[3] + 1

        elif oppMove == "DUCK":
            nextState[5] = state[5] +1

        elif oppMove == "RELOAD":
            nextState[4] = state[4] + 1

            if myMove == "THROW":
                nextState[0] = state[0] + 1

        nextState[6] = state[6] + 1 #Increase round number after opponent makes move
                
    return nextState


#-----------------------------------------------------------------------#
def evalState(state, valueOfWin):
    if state[0] == 3:
        return valueOfWin

    elif state[3] == 3:
        return -valueOfWin

    elif state[6] >= 31:
        if state[0] > state[3]:
            return valueOfWin-1

        else:
            return -valueOfWin+1       

    else: #IF WE'RE NOT AT A WINNING STATE BUT WE'VE REACHED MAXIMUM DEPTH
        pointsUtilties = [0, 3, 6]
        ducksUtilities = [-1, 1, 2, 3, 4, 5]
        ballsUtilities = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        myDucksLeft = 5 - state[2]
        oppDucksLeft = 5 - state[5]

        pointsUtility = pointsUtilties[state[0]] - pointsUtilties[state[3]]
        ducksUtility = 2*(ducksUtilities[myDucksLeft] - ducksUtilities[oppDucksLeft])
        ballsUtility = 1.5*ballsUtilities[state[1]] - ballsUtilities[state[4]]

        return pointsUtility + ducksUtility + ballsUtility

    
