def getFloatInput():
    fValue = -1
    while fValue < 0:
        try:
            fValue = float( input(sPrompt) )
        except:
            print("Enter a valid number")
    return fValue

def getIntegerInput():
    iValue = -1
    while iValue < 0:
        try:
            iValue = int( input(sPrompt) )
        except:
            print("Enter a valid number")
    return iValue
