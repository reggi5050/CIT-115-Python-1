# Hey Brian L. Candido, this assignment is from Emil Stanbury. Wish me luck!
#       Don't worry; I am very unfamiliar with AI. I don't even know where to start with it.
#       Yesterday I did upgrade my google storage and it seems to be an AI perc; but once again
#       I am very stubborn and I want to learn the hard way. Plus I don't have the time to get into
#       new AI systems where I just don't even know where to start.
# Temp Converter
#Reflection:
# I liked that i was able to make the program function off certain inputs.
# I Struggled with the matter that i am ahead of the classes that i attend. I wasnt ready haha.
# if/else is when one thing does not go as plan then theres only one other option and thats to cut the cord basically.
#       basically if this one logic isnt correct than your time here is finished, like a spin of the wheel at a carnival.
#       If you lose, then heres the results if option one does not go as planned.
# if/elif/else is if one thing does not cooperate then theres another option but if all fails then its a no go.
#       basically if this option isnt correct than theres another way in, but after your two possible outcomes are not correct then
#       you must pay again to play again.
#1. I learned about or statements
#2. I learned about if/else logic
#3. I learned that i took on a class that is fast and im not dropping the ball.

#Prompt for Temperature

fTemp = float( input ('What is the Temperature:') )

#Prompt If Temperature is F or f for Hahrenheit or C or c for Celsius:

sTempCode = input ('Is the temperature Fahrenheit "F" or Celsius "C":')

#If user entered somethings other than F or C "Enter a F or C" should Print and end the program.

#Constants

C_TO_FAHRENHEITERS = ((9.0/5.0) * fTemp)+32

F_TO_CELSIUSERS = (5.0/9) * (fTemp-32)

#Conversions


fFCelsius = float(F_TO_CELSIUSERS)

fCFahrenheit = float(C_TO_FAHRENHEITERS)

sX = sTempCode

#Output 

print ("Emil Stanbury's Temperature Converter")
print ("Enter a Temperature:", fTemp)
print ("Is the Temperature F for Fahrenheit or C for Celsius?", sTempCode)


#Logical Coding

if sTempCode == 'F' or sTempCode == 'f':
    if fTemp >= 212:
        print('The temp can not be > 212 ')
    elif fTemp <= 212:
        print(f'The Celsius equivalent is {fFCelsius:.1f}')

elif sTempCode == 'C' or sTempCode == 'c':
    if fTemp >= 100:
        print("Temp can not be > 100")
    elif fTemp <= 100:
        print(f'The Fahrenheit equivalent is {fCFahrenheit:.1f}')

else:
    print('Enter a F or C')




