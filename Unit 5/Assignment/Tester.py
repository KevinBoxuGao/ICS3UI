from FactoringToolbox import *

#input of trinomial should be in form ax^2+bx+c
#use function factorQuadratic() on trinomial string
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

for i in Cases:
   print(str(i), "=", factorQuadratic(i))
