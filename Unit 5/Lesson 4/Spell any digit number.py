import math

def spellOnesDigit( n ):    #"7" --> "seven"
    L = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    i = int(n)   #turns string n into an integer (e.g. an actual number )
    return L[i]


def spellTensDigit( n ):   # "6" --> "sixty"
    L = ["", "ERROR", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    i = int(n) #turns string n into an integer
    return L[i]


def spellTwoDigitNumber( n ):  # "95" --> "ninety five"
    numDigits = len(n)

    if numDigits == 1:
        return spellOnesDigit(n)
    
    elif numDigits != 2:
        return "error" 
    
    else:
        tensDigit = n[0]     #tens digit  "9"
        onesDigit = n[1]    #ones digit  "5"


        if tensDigit == "1":    #if n is between 10-19...
            L = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
            i = int(onesDigit)
            return L[i]
        
        else:  #if n is between 20-99...
            if tensDigit == "0":
                spelling = spellOnesDigit( onesDigit )
            elif onesDigit == "0":
                spelling = spellTensDigit( tensDigit )
            else:
                spelling = spellTensDigit( tensDigit ) + " " + spellOnesDigit( onesDigit )
            return spelling


def spellThreeDigitNumber( n ):   # "652" --> "six hundred fifty two"
    numDigits = len( n )

    if numDigits == 2:
        return spellTwoDigitNumber(n)
    elif numDigits == 1:
        return spellOnesDigit(n)
    elif numDigits != 3:
        return "Error in spellTwoDigits - received " + n
    else:
        onesDigit = n[2]
        tensDigit = n[1]
        hundredsDigit = n[0]

        if n == "000":
            spelling = ""
        elif hundredsDigit == "0":
            spelling = spellTwoDigitNumber(tensDigit+onesDigit)
        else:
            spelling = spellOnesDigit(hundredsDigit) + " hundred" + " " + spellTwoDigitNumber(tensDigit+onesDigit)
        return spelling

def spellAnyDigitNumber(n):
    numThreeDigitGroups = math.ceil(len(n)/3)
    lenOfIncompleteGroup = len(n)%3 #For example in 2365 the incomplete group is "2"
    
    L = ["", "thousand", "million", "billion", "trillion", "Quadrillion", "Quintillion", "Sextillion", "Septillion", "Octillion", "Nonillion", "Decillion", "Undecillion"]
    threeDigitGroups = []

    #If there is an incomplete group of three digits
    if lenOfIncompleteGroup != 0:
        threeDigitGroups.append(n[:lenOfIncompleteGroup])
    
    #string of all complete three digits groups
    completeThreeDigits = n[lenOfIncompleteGroup:]

    #append every complete three digit section to array
    for i in range(0, len(completeThreeDigits), 3):
        threeDigitGroups.append(completeThreeDigits[i:i+3])
        
    spelling = []
    #append each groups spelling
    for i in range(numThreeDigitGroups):
        print(numThreeDigitGroups)
        print(numThreeDigitGroups/3)
        word = spellThreeDigitNumber(threeDigitGroups[i])

        #check if number is greater than decillion
        if numThreeDigitGroups > 13:
            return "Error number too large"
        else:
            groupName = L[numThreeDigitGroups - i - 1]

        #if three digit group is not all 0's
        if word != "":   
            spelling.append(word + " " + groupName)
    
    return " ".join(spelling)

#####TESTING THE 1-DIGIT SPELLER
testCases = ["7", "6", "0", "1"]
for tc in testCases:
    print(tc, "=", spellOnesDigit( tc ))

print()


###TESTING THE TENS-DIGIT SPELLER
testCases = ["7", "1", "9", "0"]
for tc in testCases:
    print(tc, "=", spellTensDigit(tc))

print()

##TESTING THE 2-DIGIT SPELLER
testCases = ["67", "12", "19", "50", "11"]

for tc in testCases:
    print( tc, "=", spellTwoDigitNumber(tc) )
    
print()

#TESTING THE 3-DIGIT SPELLER
testCases = ["367", "814", "107", "500"]

for tc in testCases:
    print( tc, "=", spellThreeDigitNumber(tc) )

print()

#TESTING THE ANY-DIGIT SPELLER
testCases = ["13215236487123", "362342573452", "132635624", "3632", "1010001", "1000000", "1123133953959823745893275923758372593724"]

for tc in testCases:
    print( tc, "=", spellAnyDigitNumber(tc) )
