grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# printRotated displays the contents of the grid rotated 90 degrees clockwise


def printRotated(g):
    # Store the dimensions of the input grid
    rows = len(g)
    cols = len(g[0])

    # Iterate through cells, flopping the axes
    for i in range(0, cols):
        for j in range(0, rows):
            print(g[j][i], end="")
        print()


printRotated(grid)
