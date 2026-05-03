#Emil Stanbury

#Code for Compound Interest Loop

#Asking for Input using while loop

#applying a value to the input variable that i would need to repeat until it meets the conditions and input type

#while the loop is activated, the True keyword would have it On until it is stopped by the break

while True:
    try:
#asking for input
        fDepositERS = float(input("What is the deposit (positive value): "))
#if input is anything under 1 and above it will skip to the next step, basically it'll keep running if the input is less than or equal to 0
        if fDepositERS <= 0:
            print("Input must be a positive numeric value. ")
        else:
#if the input is valid being that it was 1 and above; the break would actually stop the while loop that is set to True, or itll be stuck in this loop        
            break
#if the input is not able to be converted to a float , such as int (such as string) the try and except will save the loop and restart cycle knowing that it was not a float, or able to be converted to float such as an int
    except ValueError:
        print("Input must be a positive numeric value. ")

#the while loop ran, the try and except function worked and ran the loop even with the string input; so ill use the same process for the other input
#rinse and repeat for the interest rate

while True:
    try:
        fInterestRateERS = float(input("What is the interest rate (positive value): "))
        if fInterestRateERS <= 0:
            print("Input must be a positive numeric value. ")
        else:
            break
    except ValueError:
        print("Input must be a positive numeric value. ")

#rinse and repeat for the numnber of months 

while True:
    try:
        iMonthERS = int(input("What is the number of months (positive value): "))
        if iMonthERS <= 0:
            print("Input must be a positive numeric value. ")
        else:
            break
    except ValueError:
        print("Input must be a positive numeric value. ")


# thile while loop is set to on until it is set to False or broken by the break in the else statement
while True:
    try:
        fGoalERS = float(input("What is the goal amount (can enter 0 but not negative): "))
# if the input for the goal is less than 0 then the code will repeat
        if fGoalERS < 0:
            print("Input must be 0 or greater. ")
        else:
#when the input is 0 and above then it will go to the else and break the loop
            break
#if the input is anything other than an int or float the code will not crash and repeat
    except ValueError:
        print("Input must be 0 or greater. ")

#calculations for the monthly rate as a constant
fMonthlyRateERS = (fInterestRateERS / 100) / 12

#setting variable terms for the next while loop
iMonthAccruedERS = 1

fDepositAccruedERS = fDepositERS

#while the months accrued are not equal to the amount of months that the user entered the loop will run
while iMonthAccruedERS <= iMonthERS:
#the equation has the product of the interest rate added to the new deposit sum for that loop cycle
    fDepositAccruedERS += (fDepositAccruedERS * fMonthlyRateERS)
#each time the loop runs, it will pring the months and new account balance until the month loop is met
    print(f"Month: {iMonthAccruedERS} Account Balance is: $ {fDepositAccruedERS:,.2f}")
    iMonthAccruedERS += 1


#this was tricky, i was thinking, even though the goal may be 0, it shouldnt run until the goal is over the 
# deposited balance because it will stop immidiately and be a waste of cpu and ram
if fGoalERS > fDepositERS:
#setting variables for the new while loop
    iMonthAccruedERS = 0

    fDepositAccruedERS = fDepositERS
#while the deposit accrued is less than the goal balance, the loop will run until it is over or equal to the goal and stop running 
    while fDepositAccruedERS <= fGoalERS:
#same equation as before
        fDepositAccruedERS += (fDepositAccruedERS * fMonthlyRateERS)
#adding 1 to the amount of months each loop
        iMonthAccruedERS += 1
#the print is still part of the if statement but outside of the while loop and will onlt print if the if statement is met and the while loop is completed
    print(f"It will take: {iMonthAccruedERS} Months to reach the goal of $ {fGoalERS:,.2f}")
 