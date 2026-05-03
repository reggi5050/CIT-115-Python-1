# Emil Stanbury
# Compound Interest
# What You Liked about this assignment?
#      This assignment was faily easy but it was a bit to learn on the spot 
#
# Share what you struggled with?
#      Format coding was very annoying to deal with
#
# Why did you have to use () on the formula to calculate FV?
# I had to do different equations in the formula and the needed to be separated by the () /
#      to be done correctly. The exponent was an equation it self so it needed its own ()
# Share exactly 3 things you learned on this assignment:
# 1. Format is different in ever situation dealing with numbers left and right situations/
#      along with the differences of variables and strings.
# 2. I touched up on my math skills a bit.
# 3. I got better with knowing how to make a simplified variable instead of a multiple stage process /
#      to get the information right

# Principal amount to be invested

fPrincipal_Investment = float(input('Enter the starting principal: '))

# Annual Intest Rate

sRate =  float (input( 'Enter the annual interest rate: '))

fRate = sRate / 100

# The Number of Times Compounding occurs per period

fMonths = float( input( 'How many times per year is the interest compounded? '))

# Amount of expected years 

fYears = float(input('For how many years will the account earn interest? '))


#Calculate the amount needed to deposit

fFuture_Value = fPrincipal_Investment * (1.0 + fRate / fMonths ) ** (fMonths * fYears)

#Output

print('At the end of 2 years you will have $', format(fFuture_Value, "8,.2f" ) )
