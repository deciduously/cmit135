# multiplication.py pretty prints a multiplication table

# Function to return the number of digits a number n has


def num_digits(n):
    # Converts it to a string a counts the length - the math way would work too but this is easy
    return len(str(n))


def draw_table(n):
    # calculate this outside the loop so we dont run it every iteration
    total_size = n*n
    for i in range(1, n):
        for j in range(1, n):
            # Print the product of the indices
            current_cell = i*j
            # Use the size difference betwene the max value and the current value to determine current cell padding
            padding = ' ' * (1 + num_digits(total_size) -
                             num_digits(current_cell))
            print(padding + str(i*j), end="")
        print()


# draw with 10
draw_table(10)
