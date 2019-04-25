from math import *

#Parse and find a, b and c in string
def findABC(trinomial):
    a = 0
    b = 0
    c = 0


    ABC = [a,b,c]

    return ABC

#Euclid's Algorithm
def GCD(first, second):
    low = min(first, second)
    high = max(first, second)

    #loop to reassign value of low to gcd
    while high % low != 0:
        #store value of low
        temporary = low
        #reassign low to remainder
        low = high % low
        #set high to old value of low
        high = temporary
    return low

def getCommonFactor(a, b, c):
    abGCD = GCD(a, b)
    return GCD(abGCD, c)

def getFactors(number):
    cf1 = []
    cf2 = []

    maxFactor = number
    #check if number is negative
    if number < 0:
        maxFactor = number * -1 #set max factor to positive so that we can loop to it

    #go through every possible factor
    for i in range(1, maxFactor):
        #if factor is divisible into number
        if number % i == 0:
            firstFactor = i
            secondFactor = number//i

            cf1.append(firstFactor)
            cf2.append(secondFactor)
            #inverse of factors
            cf1.append(firstFactor*-1)
            cf2.append(secondFactor*-1)

    return [cf1, cf2]

#get matching pair if a=1
def getMatchingPair1(cf1, cf2, b):
    matchingPair = []
    for i in range(len(cf1)):
        #if factors add up to b
        if cf1[i] + cf2[i] == b:
            matchingPair.append(cf1[i])
            matchingPair.append(cf2[i])
            return matchingPair
    
    return "Can't be factored"

#get matching pair if a>1
def getMatchingPair2(aFactors, cFactors, b):
    matchingPair = []

    for i in range(len(aFactors[0])):
        for j in range(len(cFactors[0])):
            if aFactors[0][i]*cFactors[0][j] + aFactors[1][i]*cFactors[1][j] == b:
                matchingPair.append([aFactors[0][i],cFactors[1][j]])
                matchingPair.append([aFactors[1][i],cFactors[0][j]])
                return matchingPair
            elif aFactors[0][i]*cFactors[1][j] + aFactors[1][i]*cFactors[0][j] == b:
                matchingPair.append([aFactors[0][i],cFactors[0][j]])
                matchingPair.append([aFactors[1][i],cFactors[1][j]])
                return matchingPair

    return "Can't be factored"

def factorTrinomial(abcValues):
    a = abcValues[0]
    b = abcValues[1]
    c = abcValues[2]

    trinomial = ""

    #check if terms are common factorable
    commonFactor = getCommonFactor(a, b, c)
    commonFactorable = False
    if commonFactor > 1:
        trinomial = str(commonFactor) 
        a = a//commonFactor
        b = b//commonFactor
        c = c//commonFactor
        commonFactorable = True

    sign1 = ""
    sign2 = ""

    if a == 1:
        cFactors = getFactors(c)
        numbers = getMatchingPair1(cFactors[0], cFactors[1], b)

        if numbers == "Can't be factored":
            if commonFactorable == True:
                #signs

                if b > 0:
                    sign1="+"
                if c > 0:
                    sign2="+"

                #check if any term should not be added to trinomial
                if a == 0:
                    a=""
                elif a == 1:
                    a="x^2"
                else:
                    a=str(a)+"x^2"

                if b == 0:
                    b=""
                elif a == 1:
                    b="x"
                else:
                    b=str(b)+"x"

                if c == 0:
                    c =""
                else:
                    c=str(c)
                
                trinomial = trinomial + '(' + a + sign1 + b + sign2 + c + ')'

            else:
                return "Can't be factored"
        else:
            if numbers[0] > 0: #check if the second term of the first pair of numbers is positive and if so adds a plus sign to the string
                sign1 = "+"
            if numbers[1] > 0: #check if the second term of the second pair of numbers is positive and if so adds a plus sign to the string
                sign2 = "+"

            trinomial = trinomial + "(" + "x" + sign1 + str(numbers[0]) + ")" + "(" + "x" + sign2 + str(numbers[1]) + ")"
        
        return trinomial

    elif a > 1:
        aFactors = getFactors(a)
        cFactors = getFactors(c)
        numbers = getMatchingPair2(aFactors, cFactors, b)

        if numbers == "Can't be factored":
            if commonFactorable == True:
                #check if any term should not be added to trinomial
                if a == 0:
                    a=""
                elif a == 1:
                    a="x^2"
                else:
                    a=str(a)+"x^2"

                if b == 0:
                    b=""
                elif a == 1:
                    b="x"
                else:
                    b=str(b)+"x"

                if c == 0:
                    c =""
                
                trinomial = trinomial + '(' + a + b + c + ')'
            else:
                return "Can't be factored"
        else:
            if numbers[0][1] > 0: #check if the second term of the first pair of numbers is positive and if so adds a plus sign to the string
                sign1 = "+"
            if numbers[1][1] > 0: #check if the second term of the second pair of numbers is positive and if so adds a plus sign to the string
                sign2 = "+"

            #check if a = 1 for any terms and removes it
            a1=""
            a2=""
            if numbers[0][0] > 1:
                a1 = str(numbers[0][0])
            if numbers[1][0] > 1:
                a2 = str(numbers[1][0])

            trinomial = trinomial + "(" + a1 + "x" + sign1 + str(numbers[0][1]) + ")" + "(" + a2 + "x" + sign2 + str(numbers[1][1]) + ")"

    return trinomial

def factor(trinomial):
    return factorTrinomial(findABC(trinomial))

