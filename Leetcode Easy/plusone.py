
def plusOne(digits):
        
    strdigits = map(str, digits)
    stringg =""
    for num in strdigits:
        stringg+=num
    
    numstring = int(stringg)
    plusone= numstring +1
    backtostring = str(plusone)

    finalist = []
    for char in backtostring:
        finalist.append(char)
    
    result = map(int, finalist)

    return result