# Emil Stanbury
# Grade Analyzer
# I Liked that this was testing my logical statements
#   I Struggled with knowing how to enter the grading system and where to enter it into the logical statements
#   I Figure that I could just use everything for when they didn't want to drop it and just subtract the lowest score when they wanted to
# 1 I learned that im not so good at coding without hints from the classes
# 2 My class assignments are more ahead of the class meetings
# 3 Coding can easily take all day

# Asking for Students name
sStudentNameERS = input ('Name of person that we are calculating the grades for:')

# Asking For Grades

iTestOneERS = int(input ('Test 1: '))
iTestTwoERS = int(input ('Test 2: '))
iTestThreeERS = int(input ('Test 3: '))
iTestFourERS = int(input ('Test 4: '))

# Checking to see if any grade is less than 0

if iTestOneERS <= 0 or iTestTwoERS <= 0 or iTestThreeERS <= 0 or iTestFourERS <= 0:
    print("Test scores must be greater than 0")
    raise SystemExit
# Prompt user if the lowest grade should be dropped

sLowestGradeERS = input("Do you wish to drop the lowest grade Y or N? ")

iLowestScoreERS = 0

# Logical process when Y or N is applied

if sLowestGradeERS == "y" or sLowestGradeERS == "Y":
    iDivisor = 3
    if iTestOneERS <= iTestTwoERS and iTestOneERS <= iTestThreeERS and iTestOneERS <= iTestFourERS:
            iLowestScoreERS = iTestOneERS

    elif iTestTwoERS <= iTestThreeERS and iTestTwoERS <= iTestFourERS:
            iLowestScoreERS = iTestTwoERS

    elif  iTestThreeERS <= iTestFourERS:
            iLowestScoreERS = iTestThreeERS

    else:
            iLowestScoreERS = iTestFourERS

elif sLowestGradeERS == "n" or sLowestGradeERS == "N":
    iDivisor = 4
        
else:
    raise SystemExit

# Averages of 4 Grades
fAverageERS = (iTestOneERS + iTestTwoERS + iTestThreeERS + iTestFourERS - iLowestScoreERS) / iDivisor

if fAverageERS >= 97.0:
            sGradeERS = "A+"
elif fAverageERS >= 94.0:
            sGradeERS = "A"
elif fAverageERS >= 90.0:
            sGradeERS = "A-"
elif fAverageERS >= 87.0:
            sGradeERS = "B+"
elif fAverageERS >= 84.0:
            sGradeERS = "B"
elif fAverageERS >= 80.0:
            sGradeERS = "B-"
elif fAverageERS >= 77.0:
            sGradeERS = "C+"
elif fAverageERS >= 74.0:
            sGradeERS = "C"
elif fAverageERS >= 70.0:
            sGradeERS = "C-"
elif fAverageERS >= 67.0:
            sGradeERS = "D+"
elif fAverageERS >= 64.0:
            sGradeERS = "D"
elif fAverageERS >= 60.0:
            sGradeERS = "D-"
else:
            sGradeERS = "F" 

# Results

print(f"{sStudentNameERS}'s test average is: {fAverageERS:.1f}")
print("Letter Grade For the Test is:", sGradeERS)