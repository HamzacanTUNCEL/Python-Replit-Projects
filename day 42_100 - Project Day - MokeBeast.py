# Import necessary libraries
import os
import platform

# Start an infinite loop to continuously take user input
while True:
    # Print the title of the program
    print("👾Gotta Catch 'Em All....👾")
    print()

    # Initialize a dictionary with None values
    myMokeBeast = {"name": None, "type": None, "special move": None, "hp": None, "mp": None}

    # Loop through the dictionary items and take user input for each item
    for name, value in myMokeBeast.items():
        myMokeBeast[name] = input("Enter the " + name + " of your mokebeast: ").strip().capitalize()

    print()
    print("Here is your mokebeast:")
    print()

    # Check the type of the mokebeast and print the details in corresponding color
    if myMokeBeast["type"].lower() == "fire":
        for name, value in myMokeBeast.items():
            print("\033[31m" + name.capitalize() + ": " + value + "\033[0m")
            print()

    elif myMokeBeast["type"].lower() == "water":
        for name, value in myMokeBeast.items():
            print("\033[34m" + name.capitalize() + ": " + value + "\033[0m")
            print()

    elif myMokeBeast["type"].lower() == "earth":
        for name, value in myMokeBeast.items():
            print("\033[90m" + name.capitalize() + ": " + value + "\033[0m")
            print()

    elif myMokeBeast["type"].lower() == "air":
        for name, value in myMokeBeast.items():
            print("\033[94m" + name.capitalize() + ": " + value + "\033[0m")
            print()

    elif myMokeBeast["type"].lower() == "electric":
        for name, value in myMokeBeast.items():
            print("\033[33m" + name.capitalize() + ": " + value + "\033[0m")
            print()

    else:
        print("\033[91m" + "Invalid type!" + "\033[0m")
    print()

    # Check the operating system and pause the program accordingly
    if platform.system() == "Linux":
        os.system("read -r -p 'Press any key to continue...' key")
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("pause")
        os.system("cls")
