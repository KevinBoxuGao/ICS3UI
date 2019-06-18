def roundPrice(price):
    onesDigit = (price*100) % 10
    difference = 0
    if onesDigit >= 7:
        difference = 10-onesDigit
    elif onesDigit >= 3:
        difference = 5-onesDigit
    else:
        difference = -1*onesDigit
    newAmount = price*100 + difference

    return newAmount/100


a = roundPrice( 5.12 )
b = roundPrice( 699.14 )
c = roundPrice( 94.10 )
d = roundPrice( 16.98 )

print(a) #5.10
print(b) #699.15
print(c) #94.10
print(d) #17.00

