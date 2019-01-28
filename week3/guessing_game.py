# guessing_game.py asks the user to guess its random nmber between 0 and 9

import sys

# Select winning number
from random import randint
randomNum = randint(0, 9)

# Function to get input and close the program if it's not an integer


def getInt():
    raw = input()
    try:
        return int(raw)
    except:
        print('Must be an integer!')
        sys.exit()


# Gather input
print('Enter your guess')
guess = getInt()

# Output either a win or a loss
if guess == randomNum:
    print('You win!  The number was ' + str(randomNum))
else:
    print('Sorry!  Your guess of ' + str(guess) +
          ' does not match the winning number ' + str(randomNum))
