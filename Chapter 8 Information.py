num = "Ja'Nyus R. Stanbury".upper()
print (num)

num = "Ja'Nyus R. Stanbury".lower()
print (num)

num = "Ja'Nyus R. Stanbury".capitalize()
print (num)

num = "Ja'Nyus R. Stanbury".title()
print (num)

num = "Ja'Nyus R. Stanbury".swapcase()
print (num)

num = "Ja'Nyus R. Stanbury".center(50, "=")
print (num)




sChar = input ("Enter a letter A-Z: ").lower()

sSentence = "the quick brown fox jumps over the lazy dog"

iLocation = sSentence.find(sChar)
    #.index() would need a try: and except: if the index isnt found

if iLocation != -1:
    print (f"The letter {sChar.upper()} appears at position {iLocation}.")

else:
    print(f"{sChar} does not appear in the sentence.")

sUserInput = input("Enter anything you want: ")
sUserInputFiler = sUserInput.replace(" ","")
# having spaces cases an issue where nothing trips any if: statemets
#replace has two parameters , 1 = the issue, 2 the replacement
if sUserInputFiler.isalnum():
    print("sUserInput has either leter Or numbers")

    if sUserInputFiler.isalpha():
        print("sUserInput only contains letters")

    if sUserInputFiler.isnumeric(): 
        print("sUserInput only contains numbers")
        # .isdecimal() r .isdigit() also finds numeric input

if sUserInputFiler.isspace():
    print("sUserInput only contains blankspace")

if sUserInputFiler == "":
    print("sUserInput is empty")


'''
if sUserInput.isalnum():
    print("sUserInput has either leter Or numbers")

    if sUserInput.isalpha():
        print("sUserInput only contains letters")

    if sUserInput.isnumeric(): 
        print("sUserInput only contains numbers")
        # .isdecimal() r .isdigit() also finds numeric input

if sUserInput.isspace():
    print("sUserInput only contains blankspace")

if sUserInput == "":
    print("sUserInput is empty")
'''
