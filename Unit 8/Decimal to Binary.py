def convertToDecimal(binary):
    num = 0
    for i in range(len(binary)-1,-1,-1):
        num = num + int(binary[len(binary)-i-1])*(2**i)
    return num
print(convertToDecimal("11110000"))
