def getTestScores(sPrompt):
    iTest = -1
    while iTest < 0:
        try:
            iTest = int( input(sPrompt) )
        except:
            print("Enter a Valid Number ")
    return iTest

def printDashes():
    print ("--------------------------------")

    
fTest1 = getTestScores(" Enter Test 1: ")
fTest2 = getTestScores(" Enter Test 2: ")
fTest3 = getTestScores(" Enter Test 3: ")
fTest4 = getTestScores(" Enter Test 4: ")
fTest5 = getTestScores(" Enter Test 5: ")

fAvg = (fTest1 + fTest2 + fTest3 + fTest4 + fTest5 ) / 5


printDashes()
print(f"Average is {fAvg}")
printDashes()
