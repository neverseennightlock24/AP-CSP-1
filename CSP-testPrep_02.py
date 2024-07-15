import random

contestantPref = {}
# This is a dictionary because we want to assign each contestant's name to its key-pair (favourite donut flavour)
# and then save that data elsewhere, which is not possible using a list or a tuple.
fullName = []
# This is a list because we want to be able to edit, merge, and save the values of each contestant's FULL name
# BEFORE they're input into the dictionary.
firstName = ("Bob", "Joe", "Anna", "Sarah", "Frank", "Rissa")
lastName = ("Smith", "Murphy", "Baker", "LaRusso", "Jackson", "Liu")
donutFlavour = ("chocolate", "birthday cake", "glazed", "plain", "cream-filled", "strawberry")
# These three variables above are tuples because we don't want to be able to change or edit any of their assigned values
# UNTIL they've been paired randomly and put into the dictionary.

while True:
    try:
        numPeople = int(input("How many contestants are there? (must be between 1 and 7) "))
        if 1 <= numPeople <= 7:
            break
        else:
            print("Please enter a number between 1 and 7.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

for i in range(numPeople):
    fullName.append(firstName[random.randrange(len(firstName))] + " " + lastName[random.randrange(len(lastName))])
for i in range(len(fullName)):
    contestantPref[fullName[i]] = donutFlavour[random.randrange(len(donutFlavour))]

# EXTRA METHOD ATTEMPT: randName = firstName[random.randint(0, 4)], lastName[random.randint(0, 4)]
# EXTRA METHOD ATTEMPT: contestantPref[randName] = (donutFlavour[random.randint(0, 4)])

print("The contestants and their favourite doughnuts are:")
for contestant, donut in contestantPref.items():
    print(f"{contestant}: {donut}")

while True:
    userInput = input("\nPick an option:\n"
                      "1. Add a name/donut\n"
                      "2. Update a name/donut\n"
                      "3. Inquire about a contestant's favourite donut\n"
                      "4. Remove a contestant\n"
                      "5. Print contestant list\n"
                      "6. Exit Program\n")

    if userInput == "1":
        # Add a donut
        print("Your choice is 1")
        contestantName = input("Input the first and last name of the contestant you want to add: ")
        donutName = input("Input the name of their favourite donut: ")
        contestantPref[contestantName] = donutName
        # This line of code adds a donut with the key being represented by the variable "contestantName" and its key-pair being represented by the variable "donutName" to the dictionary contestantPref.
        # Both are variables are inputs from user. This line of code's purpose in terms of the entire program is that it runs the 1st option of our menu, that being adding a name/donut to our dictionary.
        print(contestantPref)
        
    elif userInput == "2":
        # Update a name/donut
        print("Your choice is 2")
        contestantName = input("Input the name of the contestant whose preference you'd like to update: ")
        if contestantName in contestantPref:
            newChoice = input("What would you like their new favourite donut to be? ")
            contestantPref[contestantName] = newChoice
            print(contestantPref)
        else:
            print("Sorry, that name is not available.")
        
    elif userInput == "3":
        # Inquire about a contestant's favourite donut
        print("Your choice is 3")
        contestantName = input("Input the name of the contestant whose favourite donut you'd like to inquire about: ")
        if contestantName in contestantPref:
            print(f"{contestantName}'s favourite donut is {contestantPref[contestantName]}.")
        else:
            print("Sorry, that name is not available.")
        
    elif userInput == "4":
        # Remove a contestant
        print("Your choice is 4")
        contestantName = input("Input the name of the contestant you want to remove: ")
        if contestantName in contestantPref:
            del contestantPref[contestantName]
            print("Contestant removed!")
        else:
            print("Sorry, that name is not available.")
        
    elif userInput == "5":
        # Print contestant list
        print("Your choice is 5")
        if contestantPref:
            print("Contestant list:")
            for contestant in contestantPref.keys():
                print(contestant)
        else:
            print("No contestants available.")
        
    elif userInput == "6":
        # Exit program
        print("Your choice is 6")
        print("Exiting program...")
        break
        
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
