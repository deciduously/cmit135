listToPrint = []
while True:
    newWord = input(
        "Enter a word to add to the list (press return to stop adding words) > ")
    if newWord == "":
        break
    else:
        listToPrint.append(newWord)

# listPrinter pretty-prints a list


def listPrinter(l):
    # store the length of the input list
    listLength = len(l)
    if listLength == 0:
        # Special case for empty lists
        print("Empty list!")
    elif listLength == 1:
        # Special case for single-element lists
        print(l[0])
    else:
        # otherwise print the multi-element list
        # using i to index list l instead of syntax like `for item in list` in order to check current index
        for i in range(0, listLength):
            if i == listLength - 2:
                # special case for second to last entry
                print(l[i], end=", and ")
            elif i == listLength - 1:
                # special case for last entry, includes terminating newline
                print(l[i])
            else:
                # all other elements
                print(l[i], end=", ")


listPrinter(listToPrint)
