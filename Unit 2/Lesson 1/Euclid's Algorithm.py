f = int(input("type your first number: "))
s = int(input("type your second number: "))

def algorithm(first, second):
    l = max(first, second)
    s = min(first, second)
    r = l % s
    if r == 0:
        return s
    else:
        algorithm(s,r)
    

print("The lowest common factor is", str(algorithm(f, s)))
