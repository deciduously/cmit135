# adder.py adds two numbers and outputs the total if less than 100, otherwise just a warning

import sys

# Function to get input and close the program if it's not an integer


def getInt():
    raw = input()
    try:
        return int(raw)
    except:
        print('Must be an integer!')
        sys.exit()


# Gather input, ensuring they're numbers
print('First number:')
numOne = getInt()

print('Second number:')
numTwo = getInt()

# Add them up
sum = numOne + numTwo

# Output based on sum

if sum > 100:
    print('They add up to a big number')
else:
    print('They add up to ' + str(sum))
