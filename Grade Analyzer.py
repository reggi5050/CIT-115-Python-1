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

fTestOneERS = int (input ('Test 1:'))
fTestTwoERS = int (input ('Test 2:'))
fTestThreeERS = int (input ('Test 3:'))
fTestFourERS = int (input ('Test 4:'))

# Checking to see if any grade is less than 0

if fTestOneERS > 0 and fTestTwoERS > 0 and fTestThreeERS > 0 and fTestFourERS > 0:

    # Prompt user if the lowest grade should be dropped

    sLowestGradeERS = input("Do you wish to drop the lowest grade Y or N?")

    # Finding Lowest Average Nested Logic

    if sLowestGradeERS == "y" or sLowestGradeERS == "Y":

        if fTestOneERS < fTestTwoERS and fTestOneERS < fTestThreeERS and fTestOneERS < fTestFourERS:
            iLowestScoreERS = fTestOneERS
            fAverageERS = (fTestTwoERS + fTestThreeERS + fTestFourERS) / 3

        elif fTestTwoERS < fTestOneERS and fTestTwoERS < fTestThreeERS and fTestTwoERS < fTestFourERS:
            fLowestScoreERS = fTestTwoERS
            fAverageERS = (fTestOneERS + fTestThreeERS + fTestFourERS) / 3

        elif fTestThreeERS < fTestTwoERS and fTestThreeERS < fTestOneERS and fTestThreeERS < fTestFourERS:
            fLowestScoreERS = fTestThreeERS
            fAverageERS = (fTestOneERS + fTestTwoERS + fTestFourERS) / 3

        elif fTestFourERS < fTestOneERS and fTestFourERS < fTestTwoERS and fTestFourERS < fTestThreeERS:
            fLowestScoreERS = fTestFourERS

            #Average When the lowest score is calculated and dropped

            fAverageERS = (fTestOneERS + fTestTwoERS + fTestThreeERS) / 3

            if fAverageERS >= 97.0:
                sGradeERS = "A+"
            elif fAverageERS > 93.9:
                sGradeERS = "A"
            elif fAverageERS > 89.9:
                sGradeERS = "A-"
            elif fAverageERS > 86.9:
                sGradeERS = "B+"
            elif fAverageERS > 83.9:
                sGradeERS = "B"
            elif fAverageERS > 79.9:
                sGradeERS = "B-"
            elif fAverageERS > 76.9:
                sGradeERS = "C+"
            elif fAverageERS > 73.9:
                sGradeERS = "C"
            elif fAverageERS > 69.9:
                sGradeERS = "C-"
            elif fAverageERS > 66.9:
                sGradeERS = "D+"
            elif fAverageERS > 63.9:
                sGradeERS = "D"
            elif fAverageERS > 59.9:
                sGradeERS = "D-"
            else:
                sGradeERS = "F"

    elif sLowestGradeERS == "n" or sLowestGradeERS == "N":

        # Averages of 4 Grades

        fAverageERS = (fTestOneERS + fTestTwoERS + fTestThreeERS + fTestFourERS) / 4

        if fAverageERS >= 97.0:
            sGradeERS = "A+"
        elif fAverageERS > 93.9:
            sGradeERS = "A"
        elif fAverageERS > 89.9:
            sGradeERS = "A-"
        elif fAverageERS > 86.9:
            sGradeERS = "B+"
        elif fAverageERS > 83.9:
            sGradeERS = "B"
        elif fAverageERS > 79.9:
            sGradeERS = "B-"
        elif fAverageERS > 76.9:
            sGradeERS = "C+"
        elif fAverageERS > 73.9:
            sGradeERS = "C"
        elif fAverageERS > 69.9:
            sGradeERS = "C-"
        elif fAverageERS > 66.9:
            sGradeERS = "D+"
        elif fAverageERS > 63.9:
            sGradeERS = "D"
        elif fAverageERS > 59.9:
            sGradeERS = "D-"
        else:
            sGradeERS = "F"
    else:
        raise SystemExit
else:
    print("Test scores must be greater than 0")
    raise SystemExit

# Results

print(f"{sStudentNameERS}'s test average is: {fAverageERS:.1f}")
print("Letter Grade For the Test is:", sGradeERS)