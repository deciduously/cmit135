# guessing_game_2.py asks the user to guess its random number between 0 and 100 in a loop, informing them which direction they were off

# Select winning number
from random import randint
randomNum = randint(1, 100)

# Function to get input and loop if it's not an integer


def getInt():
    userInput = 0
    # use while True to loop infinitely until we break manually
    while True:
        try:
            userInput = int(input())
        except ValueError:
            print("Must be an integer!")
            continue
        else:
            # Success!
            break
    return userInput


# set initial guess outside the range to be sure to fail - we always want to execute once
guess = 0
# Gather input
while (guess != randomNum):
    print('Guess a number between 1 and 100')
    guess = getInt()

    # defined separately so we can take the length
    fail_string = 'Sorry!  Your guess does not match the winning number'

    # If they guessed something it couldn't possibly be, let them know
    if (guess > 100 or guess < 1):
        print('That\'s outside the range!')
    # All other wrong guesses, inform whether low or high
    elif (guess != randomNum):
        print(fail_string)
        if (guess > randomNum):
            print('You were too high.')
        else:
            print('You were too low.')

    # draw a litle banner to separate guesses
    print('*' * len(fail_string))

# If we've left the loop, we've won!
print('You win!  Congratulations.')
