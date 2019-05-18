from random import *

#THIS IS A STUDENT BOT THAT DID REASONABLY WELL IN THE CLASS TOURNAMENT BUT DIDN'T PLACE IN THE TOP 3
def getMove(myScore, mySnowballs, myDucksUsed, myMovesSoFar, oppScore, oppSnowballs, oppDucksUsed, oppMovesSoFar):
      
      #if I have no more snowballs, do this...
      if mySnowballs == 0:
    
              #if I still have ducks...
              if myDucksUsed <= 4:
        
                      if oppSnowballs >= 5:
                              return chooseMove(0, 90, 0)
                      else:
                              return chooseMove(0, 30, 70)   #duck or reload

              #if I'm out of ducks...
              else:
                      return chooseMove(0, 0, 100)   #only reload
  
      #if I have the maximum number of snowballs...
      elif mySnowballs == 10:
              
              #if I still have ducks...
              if myDucksUsed <= 4:
                      if oppDucksUsed == 5:
                              return chooseMove(100, 0, 0)
                      else:
                              return chooseMove(90, 10, 0)
      
      #if I'm out of ducks...
              else:
                      return chooseMove(100, 0, 0)
  
      elif oppScore == 0 and myScore >=1:
              return chooseMove(0, 0, 100)

      elif myScore == 2 and oppSnowballs <= 5:
              return chooseMove(100, 0, 0)

      elif oppMovesSoFar[-4:] == ["THROW", "RELOAD", "THROW", "RELOAD"]:	#detects a throw-reload loop
              if myDucksUsed <= 4:
                      return chooseMove(0, 100, 0)
        
              elif mySnowballs >= 1:
                      return chooseMove(100, 0, 0)

              else:
                      return chooseMove(0, 0, 100)

      elif oppMovesSoFar[-4:] == ["RELOAD", "THROW", "RELOAD", "THROW"]:	#detects the reverse of the loop
              if mySnowballs >= 1:
                      chooseMove(100, 0, 0)
              else:
                      chooseMove(0, 0, 100)
          
      elif oppScore == 2:
              if myDucksUsed <= 4:
                      if oppSnowballs >= 1:
                              if mySnowballs >=1:
                                      return chooseMove(65, 35, 0)
                              else:
                                      return chooseMove(0, 100, 0)
                      else:
                              if mySnowballs >=1:
                                      return chooseMove(90, 10, 0)
                              else:
                                      return chooseMove(0, 100, 0)
              else:
                      if mySnowballs >=1:
                              return chooseMove(95, 0, 5)
                      else:
                              return chooseMove(0, 0, 100)

      else:
      
              if myDucksUsed <= 4:
                      if oppDucksUsed == 5:
                              return chooseMove(100, 0, 0)
                      else:
                              return chooseMove(50, 50, 50)

              else:
                      if oppDucksUsed == 5:
                              return chooseMove(100, 0, 0)
                      else:
                              return chooseMove(75, 0, 25)
        


#Chooses move based on given probabilities
def chooseMove(prTHROW, prDUCK, prRELOAD):
      options = prTHROW * ["THROW"] + prDUCK * ["DUCK"] + prRELOAD * ["RELOAD"]
      return choice(options)
