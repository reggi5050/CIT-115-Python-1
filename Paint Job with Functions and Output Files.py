# Emil Stanbury
# Paint Estimator
# I liked that i have come to an understanding that i could write files and complete a task with multiple instructions.
# I struggle with the time constraint thati have driving trucks all day and the class going over the material with only a day or two before the deadline. They couldnt cover the material untiltheir class was at a good point and their deadlines are not in sync with this class. 
# I struggled with many things like defining my variables after running functions and decided that ill make my own functions to practice. 
# a funtion is a set of instructions for the program to execute to to get desired results from the programmer. To use one i have to set parameters that match, the functions process, to be processed to get a returned or voided result. 
# I should code a function to be able to minimize redundant coding.
# I could be able to use a certain process easily to setup variables, run mathematical equations, and run logical functions with a simple call of the funtion needed.

# defining a main function that i could easily call later.
def main():
    #setting a fail safe for asking for input to reviece a float 
    def getFloatInput (sPrompt):
        while True:
            try:
                fNbrERS = float ( input (sPrompt) )
                break
            except:
                print ("Input must be a numeric value greater than 0: ")
        return fNbrERS
    
    # calling on the float saftey function to get desired input without fail 

    fWallSquaredERS = getFloatInput ("Enter wall space in square feet: ")
    fPaintPriceERS = getFloatInput ("Enter paint price per gallon: ")
    fFeetPerGallonERS = getFloatInput ("Enter feet per gallon: ")
    fHoursPerGallonERS = getFloatInput ("How many labor hours per gallon: ")
    fCostPerHourERS = getFloatInput ("Labor charge per hour: ")
    sStateERS = input ("State Job is in: ").upper()
    sLastNameERS = input ("Customer Last Name: ")

    # multiplying the wall squared by the amount of feet that can be covered by each gallon
    def getGallonsOfPaint(fNbr1, fNbr2):
        iGallonsERS = int ( fNbr1 / fNbr2) + 1
        return iGallonsERS
    iGallonsOfPaintERS = getGallonsOfPaint(fWallSquaredERS, fFeetPerGallonERS)

    # determining the hours itll take bu multiplying the hours itll take per gallon by the amount of gallons needed
    def getLaborHours (fNbr1, fNbr2):
        fHoursERS = fNbr1 * fNbr2 
        return fHoursERS
    fHoursOfLaborERS = getLaborHours (fHoursPerGallonERS, iGallonsOfPaintERS)

    # multiplying the hours of labor by the cost per hour 
    def getLaborCost(fNbr1, fNbr2):
        fLaborERS = fNbr1 * fNbr2
        return fLaborERS
    fLaborChargesERS = getLaborCost(fHoursOfLaborERS, fCostPerHourERS)

    # multiplying the gallos of paint by the price of paint 
    def getPaintCost(fNbr1, fNbr2):
        fPChargesERS = fNbr1 * fNbr2
        return fPChargesERS
    fPaintChargesERS = getPaintCost(iGallonsOfPaintERS, fPaintPriceERS)

    # heres a logical function to figure out what the tax rate will be when the state variables input is entered and called 
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
    fTaxRateERS = getSalesTaxRate(sStateERS)

    def showCostEstimate(Nber1 , Nber2 , Nber3 , Nber4 , Nber5 , Nber6 , Nber7 ):
    # opening a new file "(filde descrptior path)", "(in writing (w) mode)" with a with statement "as" refered to as file 
        with open(f"{Nber7}_PaintJobOutput.txt", "w") as file:
            file.write(f"Gallons of paint: {Nber1} \n")
            file.write(f"Hours of Labor: {Nber2:.1f} \n") 
            file.write(f"Paint charges: ${Nber4:,.2f} \n") 
            file.write(f"Labor charges: ${Nber3:,.2f} \n") 
            file.write(f"Tax: ${Nber5:,.2f} \n")
            file.write(f"Total cost: ${Nber6:,.2f} \n") 
 

    # printing all the files here as well as to the file 
        print(f"Gallons of paint: {Nber1}")
        print(f"Hours of Labor: {Nber2:.1f}")
        print(f"Paint charges: ${Nber4:,.2f}")
        print(f"Labor charges: ${Nber3:,.2f}")
        print(f"Tax: ${Nber5:,.2f}")
        print(f"Total cost: ${Nber6:,.2f}")
        print(f"File: {Nber7}_PaintJobOutput.txt was created. ")
        
    # i was having trouble with the main function and realized that i have to have everything undermain, but in my frustation i made functions for my total equations because i could not figure out how to get it into the mainn as parameters with out defining them first, 
    # i didnt need to make a funtion for the total and taxes but it was good practice iwould take it out or write it in a comment to make things known that i could do it. 
    # fTaxERS = (fLaborChargesERS + fPaintChargesERS) * fTaxRateERS

    def computeTax(Nber1, Nber2, Nber3):
        fTotalERS = ((Nber1 + Nber2) * Nber3)
        return fTotalERS
    fTaxERS = computeTax(fLaborChargesERS, fPaintChargesERS, fTaxRateERS)

    # Total could easily be 
    # fTotalCostERS = fPaintChargesERS + fLaborChargesERS + fTaxERS
    def computeTotal(Nber1, Nber2, Nber3):
        totalERS = Nber1 + Nber2 + Nber3
        return totalERS
    fTotalCostERS = computeTotal(fPaintChargesERS, fLaborChargesERS, fTaxERS)

    # I need to get all my parameters in order to the ones set in the cost estimator function to print and write the reciept to a file 
    showCostEstimate(iGallonsOfPaintERS, fHoursOfLaborERS, fLaborChargesERS, fPaintChargesERS, fTaxERS, fTotalCostERS, sLastNameERS)

main()