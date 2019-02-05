# countdown.py counts down from 10 in a while loop and then a for loop

print('while(x >= 0):\n\tprint(x)\n\tx -= 1\n')

# Set initial counter
x = 10
while(x >= 0):
    print(x)
    # Decrement counter
    x -= 1

print('\n\nfor x in range(10, -1, -1):\n\tprint(x)')

# Use range [10,9,8,7,6,5,4,3,2,1,0]
for x in range(10, -1, -1):
    print(x)
