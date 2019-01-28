# voting.py verifies whether the user input is above or below 18

import sys

# Function to get input and close the program if it's not an integer


def getInt():
    raw = input()
    try:
        return int(raw)
    except:
        print('Must be an integer!')
        sys.exit()


# Prompt for input
print('Enter your age')
age = getInt()

# Output based on input
if age >= 18:
    print('You are of voting age')
else:
    print('You must be 18 to vote')
