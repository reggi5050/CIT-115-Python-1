# Name: Emil Stanbury aka Millz
# Assignment: Planetary Weights
#Reflection: Share what you liked about this assignment?
#
#            Share what you struggled with?
#                  The Syntax with the First format code
#            Explain specifically how you used Python formatting option to align the output
#                 I told it to form everything with 20 spaces on the first input /
#                 and with the second i told it to use 10 spaces with 2 decimal spaces 
#            Share exactly three things you learned on this assignment:
#
#            1.I learned that the first format syntax is like number formats but there is no decimal after the .
#            2.I learned to simplify my coding from when i first started trying the homework a week ago, PEMDAS is like the codes,
#              It works its way to the main thing that you want it to do.
#            3.I learned that i have bad typing habits with capitalization and that i need to look at the keyboard and stop useing shift outside of my skillset


fMERCURY = 0.38
fVENUS = 0.91
fMOON = 0.165
fMARS = 0.38
fJUPITER = 2.34
fSATURN = 0.93
fURANUS = 0.92
fNEPTUNE = 1.12
fPLUTO = 0.066

#Input: Asking For Data From the User:

sNameERS = input('What is your name:')


fWeightERS = float( input ('What is your weight:'))


#Conversion:

sWeightERS = str( fWeightERS )

#Output:

print( sNameERS, "here are your weights on our Solar System's planets:")
print( '{:20}'. format ("Weight on Mercury:") + format( fMERCURY * fWeightERS,'10.2f'))
print( '{:20}'. format ("Weight on Venus:") + format( fVENUS * fWeightERS,'10.2f'))
print( '{:20}'. format ("Weight on our Moon:") + format( fMOON * fWeightERS,'10.2f'))
print( '{:20}'. format ("Weight on Mars:") + format( fMARS * fWeightERS,'10.2f'))
print( '{:20}'. format ("Weight on Jupiter:") + format( fJUPITER * fWeightERS,'10.2f'))
print( '{:20}'. format ("Weight on Saturn:") + format( fSATURN * fWeightERS,'10.2f'))
print( '{:20}'. format ("Weight on URANUS:") + format( fURANUS * fWeightERS,'10.2f'))
print( '{:20}'. format ("Weight on Neptune:") + format( fNEPTUNE * fWeightERS,'10.2f'))
print( '{:20}'. format ("Weight on Pluto:") + format( fPLUTO * fWeightERS,'10.2f'))
