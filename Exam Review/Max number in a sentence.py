s = "Today I ate -4 bowls of lasagna.  I think. Or maybe it was -5, -6, or even -8! Tomorrow I might go for -12.  Would you believe my previous record was -3?"


def maxNumber(s):
    p = ['.', ',', '?', '!']
    for i in p:
        s = s.replace(i, '')
    words = s.split(" ")

    n = 'None'

    for i in words:
        if i.strip("-").isdigit():
            if n == 'None':
                n = int(i)
            elif int(i) > n:
                n = int(i)

    return n

print(maxNumber(s))
