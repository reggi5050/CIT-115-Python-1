# Emil Stanbury
# Paint Estimator
# I liked that i have come to an understanding that i could write files and complete a task with multiple instructions.
# I struggle with the time constraint thati have driving trucks all day and the class going over the material with only a day or two before the deadline. They couldnt cover the material untiltheir class was at a good point and their deadlines are not in sync with this class. 
# I struggled with many things like defining my variables after running functions and decided that ill make my own functions to practice. 
# a funtion is a set of instructions for the program to execute to to get desired results from the programmer. To use one i have to set parameters that match, the functions process, to be processed to get a returned or voided result. 
# I should code a function to be able to minimize redundant coding.
# I could be able to use a certain process easily to setup variables, run mathematical equations, and run logical functions with a simple call of the funtion needed.

# defining the main function to process all the other funtions and input into a final outcome
def main():
    #ask for wall space
    fWallSquaredERS = getFloatInput ("Enter wall space in square feet: ")
    #ask for paint price
    fPaintPriceERS = getFloatInput ("Enter paint price per gallon: ")
    #ask for feet coverd per gallon
    fFeetPerGallonERS = getFloatInput ("Enter feet per gallon: ")
    #asking for how many hours would be needed per gallon
    fHoursPerGallonERS = getFloatInput ("How many labor hours per gallon: ")
    #asking for the charge rate per hour
    fCostPerHourERS = getFloatInput ("Labor charge per hour: ")
    #asking for the state that the tax is in
    sStateERS = input ("State Job is in: ").upper()
    #asking for the customers last name
    sLastNameERS = input ("Customer Last Name: ")
    #processing the gallons of paint needed useing the wall space and feet covered per gallon
    iGallonsOfPaintERS = getGallonsOfPaint(fWallSquaredERS, fFeetPerGallonERS)
    #processing the hours of labor needed using the hours per gallon and the amount of gallons needed
    fHoursOfLaborERS = getLaborHours (fHoursPerGallonERS, iGallonsOfPaintERS)
    #processing the labor charge from the hours of labor needed per gallon and the price of labor per hour
    fLaborChargesERS = getLaborCost(fHoursOfLaborERS, fCostPerHourERS)
    #processing the cost of paint from the gallons of paint needed for the price per gallon
    fPaintChargesERS = getPaintCost(iGallonsOfPaintERS, fPaintPriceERS)
    #determining the tax rate from the state entered by the customer
    fTaxRateERS = getSalesTaxRate(sStateERS)
    #processing the state taxes from the labor charges and paint charges by the tax rate
    fTaxERS = computeTax(fLaborChargesERS, fPaintChargesERS, fTaxRateERS)
    # fTotalERS = ((fLaborChargesERS + fPaintChargesERS) * fTaxRateERS)
    #processing the total cost adding the cost of paint and labor and taxes
    fTotalCostERS = computeTotal(fPaintChargesERS, fLaborChargesERS, fTaxERS)
    # totalERS = fPaintChargesERS + fLaborChargesERS + fTaxERS
    #writing the processed input to the determined file and printing to the screen
    showCostEstimate(iGallonsOfPaintERS, fHoursOfLaborERS, fLaborChargesERS, fPaintChargesERS, fTaxERS, fTotalCostERS, sLastNameERS)

#defining function to get numeric input
def getFloatInput (sPrompt):
    while True:
        try:
            fNbrERS = float ( input (sPrompt) )
            break
        except:
            print ("Input must be a numeric value greater than 0: ")
    return fNbrERS

#defining the gallons of paint needed useing the wall space and feet covered per gallon
def getGallonsOfPaint(fNbr1, fNbr2):
    iGallonsERS = int ( fNbr1 / fNbr2) + 1
    return iGallonsERS

#processing the hours of labor needed using the hours per gallon and the amount of gallons needed
def getLaborHours (fNbr1, fNbr2):
    fHoursERS = fNbr1 * fNbr2 
    return fHoursERS

#processing the labor charge from the hours of labor needed per gallon and the price of labor per hour
def getLaborCost(fNbr1, fNbr2):
    fLaborERS = fNbr1 * fNbr2
    return fLaborERS

#processing the cost of paint from the gallons of paint needed for the price per gallon
def getPaintCost(fNbr1, fNbr2):
    fPChargesERS = fNbr1 * fNbr2
    return fPChargesERS
    
#determining the tax rate from the state entered by the customer
def getSalesTaxRate(sResult):
    if sResult == "CT" or sResult == "VT":
        NberERS = 0.06
    elif sResult == "MA":
        NberERS = 0.0625
    elif sResult == "ME":
        NberERS = 0.085
    elif sResult == "RI":
        NberERS = 0.07
    else:
        NberERS = 0.0
    return NberERS
    
#defining the code needed to the determined file name and write the parameters needed from the processed input, and printing the same information to the screen
def showCostEstimate(Nber1 , Nber2 , Nber3 , Nber4 , Nber5 , Nber6 , Nber7 ):

    with open(f"{Nber7}_PaintJobOutput.txt", "w") as file:
        file.write(f"Gallons of paint: {Nber1} \n")
        file.write(f"Hours of Labor: {Nber2:.1f} \n") 
        file.write(f"Paint charges: ${Nber4:,.2f} \n") 
        file.write(f"Labor charges: ${Nber3:,.2f} \n") 
        file.write(f"Tax: ${Nber5:,.2f} \n")
        file.write(f"Total cost: ${Nber6:,.2f} \n") 

    print(f"Gallons of paint: {Nber1}")
    print(f"Hours of Labor: {Nber2:.1f}")
    print(f"Paint charges: ${Nber4:,.2f}")
    print(f"Labor charges: ${Nber3:,.2f}")
    print(f"Tax: ${Nber5:,.2f}")
    print(f"Total cost: ${Nber6:,.2f}")
    print(f"File: {Nber7}_PaintJobOutput.txt was created. ")
    
#processing the state taxes from the labor charges and paint charges by the tax rate
#this was supposed to be in main but i thought i could code it for excercise purposes
def computeTax(Nber1, Nber2, Nber3):
    fTotalERS = ((Nber1 + Nber2) * Nber3)
    return fTotalERS

#processing the total cost adding the cost of paint and labor and taxes
#this was supposed to be in main but i thought i could code it for excercise purposes
def computeTotal(Nber1, Nber2, Nber3):
    totalERS = Nber1 + Nber2 + Nber3
    return totalERS

# The issue i had was getting all the items to go in order and having the ability to call the function and have the variables ready. Here is it right. I only thought about it because i had more time to look at it under less time constraint.

#running code
main()