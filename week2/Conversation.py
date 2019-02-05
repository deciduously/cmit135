# A program that has a simple conversation with the user

# First, greet the user and prompt for a name
print('Hello there!  I\'m the Computer.  What\'s your name?')
userName = input()

# Next, display the given name and ask for the temperature
print('Marvelous!  It\'s great to meet you, ' + userName + '.  Now tell me: what\'s the current temperature outside?')
currentTemp = input()

# Ask for a favorite temp
print('And what\'s your favorite temperature?')
favoriteTemp = input()

# Ask the user to clarify their temperature scale
print('Wow!  Of course, that doesn\'t mean a whole lot without context.  Is that (C)elcius or (F)arenheit?')
tempScale = input()

# Set up predicates to test the users temp scale input
def isCelcius(s):
    return s == 'c' or s == 'C'
def isFarenheit(s):
    return s == 'f' or s == 'F'

# Ensure we have a temperature scale that makes sense
# If we don't, ask for a new one until we do
while not(isCelcius(tempScale) or isFarenheit(tempScale)):
    print('Hm, I don\'t know that one.  Just give me a \'c\' or an \'f\', please, in either lower or upper case.  Try again:')
    tempScale = input()

#  Set the freezing point based on the user's answer for time scale
# If they indicated Celcius, it's at 0, and otherwise we know from the loop they indicated Farenheit
freezing = 0 if isCelcius(tempScale) else 32

# Set the long name of the degree scale for display
tempScaleStr = 'Celcius' if isCelcius(tempScale) else 'Farenheit'

# Get the distances from freezing and their desired temp
currentTempInt = int(currentTemp)
deltaFreezing = currentTempInt - freezing
deltaFavorite = currentTempInt - int(favoriteTemp)

# Show the user the differences between their current temp, favorite temp, and freezing temp
print('According to Weather Station You, it\'s currently ' + str(currentTemp) + ' degrees ' + tempScaleStr)
if deltaFreezing >= 0:
    print('That\'s ' + str(deltaFreezing) + ' degrees above freezing!')
else:
    print('That\'s ' + str(abs(deltaFreezing)) + ' degrees below freezing!')

if deltaFavorite >= 0:
    print('A bit balmy for your tastes... fully ' + str(deltaFavorite) + ' degrees higher than your comfort zone.')
else:
    print('Too bad it\'s so frigid... a full ' + str(abs(deltaFavorite)) + ' degrees below your comfort zone.')

# Say goodbye
print('It\'s been a real pleasure talking to you about the weather.  Ta!')
