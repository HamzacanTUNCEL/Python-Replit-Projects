# Import necessary libraries
import os
import platform

# Start an infinite loop to continuously take user input
while True:

    # Print the title of the program
    print("⭐Website Rating⭐")
    print()

    # Initialize a dictionary with None values
    myDictionary = {"name": None, "URL": None, "description": None, "rating": None}

    # Loop through the dictionary items and take user input for each item
    for name, value in myDictionary.items():
        # Capitalize the input for all items except 'URL'
        if name != "URL":
            myDictionary[name] = input(f"Enter {name}: ").strip().capitalize()
        # Convert 'URL' input to lowercase
        else:
            myDictionary[name] = input(f"Enter {name}: ").strip().lower()

    print()

    # Loop through the dictionary items and print them
    for name, value in myDictionary.items():
        # Print all items except 'rating' with a comma at the end
        if name != "rating":
            print(f"{name.capitalize()}:{value},", end=" ")
        # Print 'rating' without a comma at the end
        else:
            print(f"{name.capitalize()}:{value}", end=" ")
    print()
    print()

    # Check the operating system and pause the program accordingly
    if platform.system() == "Linux":
        os.system("read -r -p 'Press any key to continue...' key")
        # Clear the console after pausing
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("pause")
        # Clear the console after pausing
        os.system("cls")
