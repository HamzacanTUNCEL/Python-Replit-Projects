import os  # Import the modules random, time and os
import random
import time


def characterHealth():  # Define a function to calculate the character's health based on random numbers
    a = random.randint(1, 6)  # Generate a random integer between 1 and 6 and assign it to a
    b = random.randint(1, 12)  # Generate a random integer between 1 and 12 and assign it to b
    c = (a * b) / 2  # Multiply a and b and divide by 2, then assign the result to c
    hp = c + 10  # Add 10 to c and assign the result to hp, which is the character's health
    return hp  # Return the value of hp


def characterStrength():  # Define a function to calculate the character's strength based on random numbers
    a = random.randint(1, 6)  # Generate a random integer between 1 and 6 and assign it to a
    b = random.randint(1, 12)  # Generate a random integer between 1 and 12 and assign it to b
    c = (a * b) / 2  # Multiply a and b and divide by 2, then assign the result to c
    characterStr = c + 12  # Add 12 to c and assign the result to characterStr, which is the character's strength
    return characterStr  # Return the value of characterStr


while True:  # Start an infinite loop
    print("⚔🏹 CHARACTER BUILDER 🏹⚔")  # Print a title for the program
    time.sleep(1)  # Pause for one second
    os.system("clear")  # Clear the screen
    Name = input(
        "Name your Legendary Character :")  # Ask the user to input the name of the character and assign it to Name
    time.sleep(1)  # Pause for one second
    os.system("clear")  # Clear the screen
    Type = input(
        "Character Type (Human,Elf,Wizard,Orc) :")  # Ask the user to input the type of the character and assign it
    # to Type
    time.sleep(1)  # Pause for one second
    os.system("clear")  # Clear the screen
    print(Type, Name)  # Print the type and name of the character
    print("HEALTH: ", characterHealth())  # Print the health of the character by calling the characterHealth function
    print("STRENGTH: ",
          characterStrength())  # Print the strength of the character by calling the characterStrength function
    print()  # Print an empty line
    print("May your name go down in Legend...")  # Print a message to congratulate the user for creating a character
    Exit = input("Again? :")  # Ask the user if they want to create another character and assign their answer to Exit
    if Exit == "Yes" or Exit == "Y" or Exit == "yes" or Exit == "y":  # If Exit is "Yes", "Y", "yes" or "y", then
        # continue the loop
        time.sleep(1)  # Pause for one second
        os.system("clear")  # Clear the screen
        continue  # Go back to the beginning of the loop
    else:
        break  # Otherwise, break out of the loop
