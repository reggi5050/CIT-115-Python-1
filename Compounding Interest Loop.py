#Emil Stanbury

#Code for Compound Interest Loop

#Asking for Input using while loop

#applying a value to the input variable that i would need to repeat until it meets the conditions and variable type

fDepositERS = 0

#if the deposit is 0 and anything less it will repeat until the input is 1 and over. Also using the try and except function. if there is a string it will not crash the program

while fDepositERS <= 1:
    try:
#asking for input
        fDepositERS = float(input("What is the deposit (positive value): "))
#if input is anything under 1 and above it will skip to the next step
        if fDepositERS <= 0:
            print("Input must be a positive numeric value. ")
#if the input is anything other than a variable that is a int or float it will pass through and restart cycle
    except ValueError:
        print("Input must be a positive numeric value. ")

#rinse and repeat but this variable is a float
fInterestRateERS = 0
while fInterestRateERS <= 1:
    try:
        fInterestRateERS = float(input("What is the interest rate (positive value): "))
        if fInterestRateERS <= 0:
            print("Input must be a positive numeric value. ")
    except ValueError:
        print("Input must be a positive numeric value. ")

#the code worked so it is valid until anything needs to be different
iMonthERS = 0
while iMonthERS <= 1 :
    try:
        iMonthERS = int(input("What is the number of months (positive value): "))
        if iMonthERS <= 0:
            print("Input must be a positive numeric value. ")
    except ValueError:
        print("Input must be a positive numeric value. ")

#seting variable to be applicable for 0 and above instead of 1 and above
fGoalERS = -1
#anything less than 0 this part of the program will repeat until the input is 0 and above
while fGoalERS < 0:
    try:
        fGoalERS = float(input("What is the goal amount (can enter 0 but not negative): "))
# if the input for the goal is 0 and above the code will repeat
        if fGoalERS < 0:
            print("Input must be 0 or greater. ")
#if the input is anything other than an int or float the code will not crash and repeat
    except ValueError:
        print("Input must be 0 or greater. ")

#calculations for the monthly rate as a constant
fMonthlyRateERS = (fInterestRateERS / 100) / 12

#setting variable terms for the next while loop
iMonthAccruedERS = 1
#setting two terms that the loop will continue until both terms are met, one condition not being net will not stop the loop
while iMonthAccruedERS <= iMonthERS or fDepositERS <= fGoalERS:

#coding an equation to get the monthly interest and add it to the deposit over and over
    fDepositERS += (fDepositERS * fMonthlyRateERS)
#if the months accrued does not meet the condition of the input of months the user is asking for then the code will continue to run over and over until that condition is met
    if iMonthAccruedERS <= iMonthERS:
        print(f"Month: {iMonthAccruedERS} Account Balance is: $ {fDepositERS:,.2f}")
#until the condition of the total balance until the balance is equal or above the goal is met as the code continues to run with no output
    elif fDepositERS >= fGoalERS:
#when the condition meeting the goal is finally met then the program will output this statement
        print(f"It will take: {iMonthAccruedERS} Months to reach the goal of $ {fGoalERS:,.2f}")
#every time the cycle runs the program will finally add 1 more to the months accrued variable
    iMonthAccruedERS += 1

#there is still redundant code in here, im still learning :)