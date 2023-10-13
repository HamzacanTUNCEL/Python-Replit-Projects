# Import necessary libraries
import os
import platform

# Print the title of the program
print("⭐Website Rating⭐")
print()

# Start an infinite loop to continuously take user input
while True:
    # Take the website name as input from the user
    name = input("Input the website name:")
    # Take the URL as input from the user
    url = input("Input the URL:")
    # Take a description of the website as input from the user
    description = input("Input your a description: ")
    # Take a rating out of 5 as input from the user
    rating = input("Input your rating out of 5:")

    # Create a dictionary with the input data
    myDictionary = {"name": name, "URL": url, "description": description, "rating": rating}

    print()

    # Loop through the dictionary items and print them
    for name, value in myDictionary.items():
        # Print all items except 'rating' with a comma at the end
        if name != "rating":
            print(f"{name}:{value},", end=" ")
        # Print 'rating' without a comma at the end
        else:
            print(f"{name}:{value}", end=" ")
    print()
    print()
    # Check the operating system and pause the program accordingly
    if platform.system() == "Linux":
        os.system("read -r -p 'Press any key to continue...' key")
    elif platform.system() == "Windows":
        os.system("pause")
