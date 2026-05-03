# Hey Brian L. Candido, this assignment is from Emil Stanbury. Wish me luck!
#       Don't worry; I am very unfamiliar with AI. I don't even know where to start with it.
#       Yesterday I did upgrade my google storage and it seems to be an AI perc; but once again
#       I am very stubborn and I want to learn the hard way. Plus I don't have the time to get into
#       new AI systems where I just don't even know where to start.
# Temp Converter
#Reflection:I am Honestly Bummed about the calender because im trying to fit everything in as best as i can as an over the road driver,
#   i cant just skip days like i have done today, ill hear from the office later on when i get back to New York but this is what i have done all day.
#       I need to eat.


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


print ("Emil Stanbury's Temperature Converter")
print("Enter a Temperature:", fTemp)
print("Is the Temperature F for Fahrenheit or C for Celsius?", sTempCode)


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




