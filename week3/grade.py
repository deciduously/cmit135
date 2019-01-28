# grade.py assigns a letter grade to a number

import sys

# Function to get input and close the program if it's not an integer


def getInt():
    raw = input()
    try:
        return int(raw)
    except:
        print('Must be an integer!')
        sys.exit()


# Get input
print('Enter grade percentage:')
grade = getInt()

# Output based on number
if grade > 100:
    print('Outstanding!  You got over 100%!')
elif grade < 100 and grade >= 98:
    print('A+')
elif grade < 98 and grade >= 93:
    print('A')
elif grade < 93 and grade >= 90:
    print('A-')
elif grade < 90 and grade >= 87:
    print('B+')
elif grade < 87 and grade >= 83:
    print('B')
elif grade < 83 and grade >= 80:
    print('B-')
elif grade < 80 and grade >= 77:
    print('C+')
elif grade < 77 and grade >= 73:
    print('C')
elif grade < 73 and grade >= 70:
    print('C-')
elif grade < 70 and grade >= 67:
    print('D+')
elif grade < 67 and grade >= 63:
    print('D')
elif grade < 63 and grade >= 60:
    print('D-')
elif grade < 60 and grade >= 0:
    print('F')
else:
    print('Negative grade?!  Get it together!')
