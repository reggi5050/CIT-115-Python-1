# Emil Stanbury
# Real Estate with Lists
# I liked that I was able to get it done in efficient time. I had to debug so many things and I overloaded the program and crashed it. But I was able to solve it.
# I guess ou should not call a list after a logical operation. The list is already part of the function and defined already.
# I struggled with debugging and the median. I was very difficult because in the operations it needed to be an integer and I had to use integer division and not float division.
# The list index is not based of float type data. only integer.
# A list is an object that contains multiple items. The elements are separated by commas and defined almost like a function but with square brackets. []
# A tuple is almost exactly like a list but it acts like a constant, and it is encased by regular parentheses ()
# In the grade analyzer code I could have gathered the information in a list and called them together in a FOR or WHILE loop

# Post Script, alot of the information was looking for a Float only a couple needed an integer. I almost got tripped up on that part.

# Defining a function to get input and convert it to a float
def getFloatInput(sPrompt):
    fValue = -1
    while fValue <= 0:
        try:
            fValue = float( input(sPrompt) )
        except:
            print("Enter a valid number greater than 0. ")
    return fValue

#Defining a median Process
def getMedian(iEntries, sList):
    iRemainder = iEntries % 2
# I used a Modulus to see if there was a remainder from an even number to see if the List of entries was even or odd

# If the entries were even then the remainder would be 0
    if iRemainder == 0:
        iMiddleEntryERS = iEntries // 2
        # There is two middle number so I had to access both entries and to the math on the information in the correct entry placement to do the average of those Entries
        iMedianERS = (sList[(iMiddleEntryERS - 1)] + sList[iMiddleEntryERS] ) / 2
# If the remainder was to be one or more than the number is most likely odd
    else:
        iRemainder >= 1
        # I had to use integer division to match the needs of the index being an integer with not decimals to access the list
        iMiddleEntryERS = iEntries // 2
        # Using the math to determine the index, i used the entry placement number to access the proper list entry
        iMedianERS = sList[iMiddleEntryERS]

    return iMedianERS

# the main function that would access, and ask for all the needed information to process for the desired results.
def main():
    # defining a name for the list
    festate_ValuesERS = []
    # staging the while loop to start
    sAgain = 'Y'
    # as long as the input isn't "no" then the loop would continue
    while sAgain != 'N':
        if sAgain == 'Y':
            fSalesPriceERS = getFloatInput('Enter property sales value: ')
            festate_ValuesERS.append(fSalesPriceERS)
            sAgain = input('Enter another value Y or N: ').upper()
    # if the input is anything other than "Y" or "N" then the loop will continue until the one that gets information or cuts the loop
        else:
            sAgain = input('Enter another value Y or N: ').upper()
    #sorting the information because the place-holder is very important for math procedures and calling the right entries.
    festate_ValuesERS.sort()
    # the number of entries in the list
    iEntriesERS = len(festate_ValuesERS)
    # the minium numer or festate_ValuesERS[0] having that the list is sorted lowest to highest and not .reversed()
    fMinERS = festate_ValuesERS[0]
    # the maximum number or festate_ValuesERS[-1] having that the list is sorted lowest to highest and not .reversed()
    fMaxERS = festate_ValuesERS[-1]
    # the sum of the list
    fSumERS = sum(festate_ValuesERS)
    # the average of the sum of the list divided by the entries
    fAvgERS = (fSumERS / len(festate_ValuesERS))
    # the median function which uses the entries and list as parameters
    fMedERS = getMedian(iEntriesERS, festate_ValuesERS)
    # the commission of .03 for the real estate agent
    fComERS = fSumERS * .03

    # setting the parameter to 0 also to match the entry numbers of the list placement
    ivalueERS = 0
    # while the place-holder value is less that the list of entries it will run the loop until it is above the list entries then it will not run another around
    while ivalueERS < len(festate_ValuesERS):
        # nice formatting to make it nice and organized
        print(f"{'Property'} {(ivalueERS + 1)}{'':4s} $ {festate_ValuesERS[ivalueERS]:11,.2f}")
        # adding a round to the ivalueERS integer to match the list entry
        ivalueERS += 1

        # printing and nice formatting 15 spaces for the string and a dollar sign and 11 spaces and 2 decimals for the float. under a fast string
    print(f"{'Minimum: ':15s}$ {fMinERS:11,.2f}")
    print(f"{'Maximum: ':15s}$ {fMaxERS:11,.2f}")
    print(f"{'Total: ':15s}$ {fSumERS:11,.2f}")
    print(f"{'Average: ':15s}$ {fAvgERS:11,.2f}")
    print(f"{'Median: ':15s}$ {fMedERS:11,.2f}")
    print(f"{'Commission: ':15s}$ {fComERS:11,.2f}")


# calling the main function
main()