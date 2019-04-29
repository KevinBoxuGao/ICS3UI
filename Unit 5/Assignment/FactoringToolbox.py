from math import *

#Parse and find a, b and c in string
def findABC(trinomial):
    trinomialString = trinomial.replace(" ", "")
    a = 0
    b = 0
    c = 0
    
    #finds first index of the substring
    aIndex = trinomialString.find("x^2") #finds first index of the substring
    if aIndex != -1: #check if a was not found as .find() will return -1
        aCoefficient = trinomialString[:aIndex] #set coefficient to characters preceding x^2
        if aCoefficient == "": #in the case that the coefficient is 1
            a = 1
        elif aCoefficient == "-": #in the case that the coefficient character is only a negative sign
            a = -1
        else: 
            a = aCoefficient
            
        trinomialString = trinomialString[aIndex+3:] #set our trinomial string to not include a as well as x^2

    bIndex = trinomialString.find("x")
    if bIndex != -1: #check if b was not found
        b = trinomialString[:bIndex] #set b to characters proceding x in the string
        trinomialString = trinomialString[bIndex+1:] #set trinomial to characters after b
    if trinomialString != "": #check if the remainder of the string contains c since it would be empty if it isn't there
        c = trinomialString
    
    #convert ABC into integers

    #for some reason int() does not work on negative numbers in the function so we convert to positive integer then make it negative
    try: 
        a = int(a)
    except ValueError:
        a = a[1:] #makes string start right after the negative sign at the start of the string
        a = int(a)
        a = a*-1
    try:
        b = int(b)
    except ValueError:
        b = b[1:] #makes string start right after the negative sign at the start of the string
        b = int(b)
        b = b*-1
    try:
        c = int(c)
    except ValueError:
        c = c[1:] #makes string start right after the negative sign at the start of the string
        c = int(c)
        c = c*-1

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

#function finds the numerical greatest common factor of terms of the trinomial
def getCommonFactor(a, b, c):
    ABC = [a,b,c]
    #if statements to remove term from list if they are 0 so that common factor of trinomial is not returned as 0
    if a == 0:
        ABC.remove(a)
    if b == 0:
        ABC.remove(b)
    if c == 0:
        ABC.remove(c)

    #we need to find gcd of values if there are more than 1 values
    if len(ABC) > 1:
        #loop through ABC list and replace pairs of numbers with their gcd
        for i in range(len(ABC)-1):
            ABC.append(GCD(ABC[0], ABC[1])) #add gcd of first two items in list at the end
            ABC.remove(ABC[0]) #remove first item in list
            ABC.remove(ABC[0]) #second item becomes the first item in the list and is then removed

    #always give the positive common factor by checking if common factor is returned as negative
    if ABC[0] < 0:
        ABC[0] = ABC[0]*-1

    return ABC[0]

def getFactors(number):
    cf1 = []
    cf2 = []

    maxFactor = number
    #check if number is negative
    if number < 0:
        maxFactor = number * -1 #set max or the largest factor, which is itself, to positive so that we can loop to it

    #go through every possible factor
    for i in range(1, maxFactor):
        #if factor is divisible into number
        if number % i == 0:
            firstFactor = i
            secondFactor = number//i #use rounding division to insure secondFactor is stored as integer since we already know the remainder is 0

            cf1.append(firstFactor)
            cf2.append(secondFactor)
            #inverse of factors that also work 
            cf1.append(firstFactor*-1)
            cf2.append(secondFactor*-1)

    return [cf1, cf2] #return a list of two lists of common factors, or also known as a 2-dimensional array

#get matching pair of coefficients if a=1
def getMatchingPair1(cf1, cf2, b):
    matchingPair = [] #will be in form of [a, b] where factored trionomial is in form (x+a)(x+b)
    for i in range(len(cf1)):
        #if factors add up to b
        if cf1[i] + cf2[i] == b:
            matchingPair.append(cf1[i])
            matchingPair.append(cf2[i])
            return matchingPair #immediately stop function with matching pair since common factors contain two pairs that work which are inverse of each other
    
    return "Can't be factored" #if we never find a factor pair

#get matching pair of coefficients if a>1
def getMatchingPair2(aFactors, cFactors, b):
    matchingPair = [] #this time a 2-dimensional array in form of [[a,b],[c,d]] if the factored trionomial is in form (ax+b)(cx+d)

    for i in range(len(aFactors[0])):
        for j in range(len(cFactors[0])):
            #two possible combinations of ways aFactors and cFactors can be multiplied to become b
            if aFactors[0][i]*cFactors[0][j] + aFactors[1][i]*cFactors[1][j] == b: #used two dimensional indexing for example, aFactors[0][i] will be cf1 of aFactors and be the number at index i
                #placing aFactors and cFactors that match up to be b in different arrays
                matchingPair.append([aFactors[0][i],cFactors[1][j]]) 
                matchingPair.append([aFactors[1][i],cFactors[0][j]])
                return matchingPair
            #other possible combination of aFactors and cFactors multiplied
            elif aFactors[0][i]*cFactors[1][j] + aFactors[1][i]*cFactors[0][j] == b:
                matchingPair.append([aFactors[0][i],cFactors[0][j]])
                matchingPair.append([aFactors[1][i],cFactors[1][j]])
                return matchingPair

    return "Can't be factored"

#function to get proper addition or subtraction sign of a number
def getAdditionSign(number):
    if number > 0:
        return "+" 
    else:
        return "" #leave number since negative number already contains "-" in front

def factorTrinomial(abcValues):
    a = abcValues[0]
    b = abcValues[1]
    c = abcValues[2]

    trinomial = ""

    commonFactor = getCommonFactor(a, b, c)
    commonFactorable = False 
    #check if terms are common factorable
    if commonFactor > 1:
        trinomial = str(commonFactor) #add commonfactor to start of trinomial by assigning trionomial to it since trinomial is empty
        #reassign a, b, and c to reduced form
        a = a//commonFactor 
        b = b//commonFactor
        c = c//commonFactor 
        #if there is no c value place x outside of the brackets
        commonFactorable = True
    if c == 0: #if c is 0 then the trinomial is also factorable by x
        if a == 1:
            a = ""
        elif a < 0: #makes sure coefficient of a is never negative
            a = a*-1
            b = b*-1
            trinomial = "-" + trinomial #sets the coefficient outside of the brackets to negative
        trinomial = trinomial + "x" + '(' + str(a) + "x" + getAdditionSign(b) + str(b) + ')' #trinomial already contains commonFactor so we just add x as well as the simplified interior of the trionomial
        return trinomial #we can safely return trionomial since if it is divisible by x then it cannot be simplied anymore

    if a == 1:
        cFactors = getFactors(c)
        pairs = getMatchingPair1(cFactors[0], cFactors[1], b) #going to be in form of [a,b] 

        if pairs == "Can't be factored":
            if commonFactorable == True: 
                #addition or subtraction signs
                signA = getAdditionSign(a) #after A
                signB = getAdditionSign(b) #after B

                #set the string parts of a, b, and c 
                if a == 0: #indicates nothing should be added
                    a=""
                elif a == 1: #don't place any coefficient in front of x
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
                
                trinomial = trinomial + '(' + a + signA + b + signB + c + ')'

            else:
                return "Can't be factored"
        else:
            #gets signs of the values of b since they have their addition or subtraction sign in the factored trinomial 
            sign1 = getAdditionSign(pairs[0]) #in first bracket between the 2 terms
            sign2 = getAdditionSign(pairs[1]) #in second bracket between the 2 terms

            trinomial = trinomial + "(" + "x" + sign1 + str(pairs[0]) + ")" + "(" + "x" + sign2 + str(pairs[1]) + ")"
        
        return trinomial

    elif a > 1:
        aFactors = getFactors(a)
        cFactors = getFactors(c)
        pairs = getMatchingPair2(aFactors, cFactors, b) #going to be in form [[a,b],[c,d]]

        if pairs == "Can't be factored":
            if commonFactorable == True:
                #format parts of the trionomial into string parts
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
            #assuming trionmial is in form (ax+b)(cx+d),
            sign1 = getAdditionSign(pairs[0][1]) #between a and b
            sign2 = getAdditionSign(pairs[1][1]) #between c and d 

            #check is a = 1 so it is not added to the string as a coefficient
            #both a factors
            a1=""
            a2=""
            #checks if coefficient should be added to the a factors
            if pairs[0][0] > 1:
                a1 = str(pairs[0][0])
            if pairs[1][0] > 1:
                a2 = str(pairs[1][0])

            trinomial = trinomial + "(" + a1 + "x" + sign1 + str(pairs[0][1]) + ")" + "(" + a2 + "x" + sign2 + str(pairs[1][1]) + ")"

    return trinomial

def factorQuadratic(trinomial):
    return factorTrinomial(findABC(trinomial)) 

