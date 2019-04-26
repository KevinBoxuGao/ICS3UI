from FactoringToolbox import *

#input of trinomial should be in form ax^2+bx+c
#use function factor() on trinomial string
Cases = [
"x^2+18x+32", 
"x^2+17x+32", 
"x^2–16x+63", 
"x^2+5x–24", 
"x^2–5x–24", 
"x^2–9", 
"x^2–10", 
"x^2+9", 
"2x^2+11x+5", 
"12x^2–7x-10", 
"87x^2–29x+143", 
"9x^2–100", 
"9x^2+1", 
"3x^2+12x+6",
"2x^2+10x+8",
"5x^2–500",
"x^2+7x",
"-10x^2+5x",
]

testCases = [[1,18,32],[1,17,32],[1,-16,63],[1,5,-24],[1,-5,-24],[1,0,-9],[1,0,-10],[1,0,9],[2,11,5],[12,-7,-10],[87,-29,143],[9,0,-100],[9,0,1],[3,12,6],[2,10,8],[5,0,-500],[1,7,0], [-10,5,0]]

for i in testCases:
    print(str(i), "=", factorTrinomial(i))

