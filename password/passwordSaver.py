import argparse
import csv
import sys


# The password list - We start with it populated for testing purposes
passwords = [["yahoo", "XqffoZeo"], ["google", "CoIushujSetu"]]


# The password file name to store the passwords to
passwordFileName = "samplePasswordFile"

# The encryption key for the caesar cypher
encryptionKey = 16

# Caesar Cypher Encryption


def passwordEncrypt(unencryptedMessage, key):

    # We will start with an empty string as our encryptedMessage
    encryptedMessage = ''

    # For each symbol in the unencryptedMessage we will add an encrypted symbol into the encryptedMessage
    for symbol in unencryptedMessage:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            encryptedMessage += chr(num)
        else:
            encryptedMessage += symbol

    return encryptedMessage


def loadPasswordFile(fileName):

    with open(fileName, newline='') as csvfile:
        passwordreader = csv.reader(csvfile)
        passwordList = list(passwordreader)

    return passwordList


def savePasswordFile(passwordList, fileName):

    with open(fileName, 'w+', newline='') as csvfile:
        passwordwriter = csv.writer(csvfile)
        passwordwriter.writerows(passwordList)

# pulled each option out of the loop to use with argument parser


def openPasswordFile():
    # don't create a shadowed `passwords` in local scope
    global passwords
    passwords = loadPasswordFile(passwordFileName)


def savePasswords():
    savePasswordFile(passwords, passwordFileName)


def lookupPassword():
    print("Which website do you want to lookup the password for?")
    for keyvalue in passwords:
        print(keyvalue[0])
    passwordToLookup = input()
    ####### YOUR CODE HERE ######
    # You will need to find the password that matches the website
    # You will then need to decrypt the password
    #
    # 1. Create a loop that goes through each item in the password list
    #  You can consult the reading on lists in Week 5 for ways to loop through a list
    #
    # 2. Check if the name is found.  To index a list of lists you use 2 square backet sets
    #   So passwords[0][1] would mean for the first item in the list get it's 2nd item (remember, lists start at 0)
    #   So this would be 'XqffoZeo' in the password list given what is predefined at the top of the page.
    #   If you created a loop using the syntax described in step 1, then i is your 'iterator' in the list so you
    #   will want to use i in your first set of brackets.
    #
    # 3. If the name is found then decrypt it.  Decrypting is that exact reverse operation from encrypting.  Take a look at the
    # caesar cypher lecture as a reference.  You do not need to write your own decryption function, you can reuse passwordEncrypt
    #
    #  Write the above one step at a time.  By this I mean, write step 1...  but in your loop print out every item in the list
    #  for testing purposes.  Then write step 2, and print out the password but not decrypted.  Then write step 3.  This way
    #  you can test easily along the way.
    #
    #  initialize result
    found = None
    # Search for requested record
    for i in range(0, len(passwords)):
        # check if the first element is our lookup
        if passwords[i][0] == passwordToLookup:
            # store the second element as our found password
            found = passwords[i][1]
            break
    # Either display the decrypted password or fail with an error message
    if found == None:
        print("No such password in storage")
    else:
        # To decrypt, subtract the encryptionKey from 26 - the Ceaser cipher can always be undone this way
        print("Decrypted password: " +
              passwordEncrypt(found, 26-encryptionKey))
    ####### YOUR CODE HERE ######


def addPassword():
    print("What website is this password for?")
    website = input()
    print("What is the password?")
    decryptedPassword = input()

    ####### YOUR CODE HERE ######
    # You will need to encrypt the password and store it in the list of passwords

    # The encryption function is already written for you
    # Step 1: You can say encryptedPassword = passwordEncrypt(decryptedPassword,encryptionKey)]
    # the encryptionKey variable is defined already as 16, don't change this
    # Step 2: create a list of size 2, first item the website name and the second item the password.
    # Step 3: append the list from Step 2 to the password list

    # Encrypt the password
    encryptedPassword = passwordEncrypt(decryptedPassword, encryptionKey)

    # Store the entry in the in-memory list
    entry = [website, encryptedPassword]
    passwords.append(entry)

    ####### YOUR CODE HERE ######


def removePassword():
    print("Which website would you like to remove?")
    websiteToRemove = input()
    # iterate until we find it
    # If it's not found, nothing happens
    for i in range(0, len(passwords)):
        currentEntry = passwords[i]
        if currentEntry[0] == websiteToRemove:
            # We found it, remove from storage
            print("Site found.  Removing " + websiteToRemove)
            del passwords[i]
            break  # this will only remove the first instance


def printPasswords():
    for keyvalue in passwords:
        print(', '.join(keyvalue))


def interactiveMode():
    while True:
        print("What would you like to do:")
        print(" 1. Open password file")
        print(" 2. Lookup a password")
        print(" 3. Add a password")
        print(" 4. Remove a password")
        print(" 5. Save password file")
        print(" 6. Print the encrypted password list (for testing)")
        print(" 7. Quit program")
        print("Please enter a number (1-7)")
        choice = input()

        if(choice == '1'):  # Load the password list from a file
            openPasswordFile()

        if(choice == '2'):  # Lookup at password
            lookupPassword()

        if(choice == '3'):
            addPassword()

        ### EXTRA CREDIT ###
        if(choice == '4'):  # Remove a password
            removePassword()
        ### END EXTRA CREDIT ###

        if(choice == '5'):  # Save the passwords to a file
            savePasswords()

        if(choice == '6'):  # print out the password list
            printPasswords()

        if(choice == '7'):  # quit our program
            sys.exit()

        print()
        print()


# extra extra credit
# refactored to use argparse
# run with no arguments for old behavior
# otherwise `$ python passwordSaver.py -h` for usage

parser = argparse.ArgumentParser(description="Manage your passwords.")
parser.add_argument(
    "-a", "--action", help="One of: Lookup | Add | Remove | Print (case insensitive)")
parser.add_argument(
    "-o", "--open", help="Specify the password file.  Note - must be set in order to us \"add\" action")
args = parser.parse_args()

# when nothing is passed, just go interactive
if not args.action:
    interactiveMode()

# if we have one, pull it out for convenience
action = args.action

# otherwise the hardcoded defaults wil be used
if args.open:
    openPasswordFile()

# match on the verb
if action.lower() == "Lookup".lower():
    lookupPassword()
elif action.lower() == "Add".lower():
    addPassword()
elif action.lower() == "Remove".lower():
    removePassword()
elif action.lower() == "Print".lower():
    printPasswords()
else:
    # if we didn't understand the action, drop to interactive (with a mildly haughty tone)
    print("Didn't understand that action, maybe interactive mode is more your speed")
    interactiveMode()

# if we opened a file, make sure to save it
if args.open:
    savePasswords()

# end extra extra credit
