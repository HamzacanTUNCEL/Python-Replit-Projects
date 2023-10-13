# Import the modules needed for the game
import random
import os
import time

# Print a welcome message
print("Welcome to Hangman!")
# Define a list of words to choose from
listOfWords = [
    "apple",
    "banana",
    "cherry",
    "date",
    "grape",
    "kiwi",
    "lemon",
    "mango",
    "nectarine",
    "orange",
]
# Set the number of tries the player has
TryCounter = 5
# Pick a random word from the list
word = random.choice(listOfWords)

# Create an empty list to store the letters the player has picked
LetterPicked = []
# Create an empty string to store the word with guessed and hidden letters
wordNew = ""


# Define a function to clear the screen and print the welcome message again
def Clean():
    # Wait for one second
    time.sleep(1)
    # Clear the screen (this might not work on some platforms)
    # os.system("cls")
    os.system("clear")
    # Print the welcome message again
    print("Welcome to Hangman!")


# Define a function to print the word with guessed and hidden letters
def printWord():
    # Print a blank line
    print()
    # Loop through each letter in the word
    for i in word:
        # If the letter is in the list of picked letters, print it
        if i in LetterPicked:
            print(i, end=" ")
            # Add the letter to the wordNew string
            globals()['wordNew'] += i
        # Otherwise, print an underscore
        else:
            print("_", end=" ")
            # Add a question mark to the wordNew string
            globals()['wordNew'] += "?"
    # Print another blank line
    print()


# Call the printWord function for the first time
printWord()
# Start an infinite loop for the game logic
while True:
    # Ask the player to guess a letter and convert it to lowercase
    letter = input("\nGuess a letter: \n").lower()

    # If the letter is already in the list of picked letters, print a message and continue the loop
    if letter in LetterPicked:
        print("You already tried that letter")
        continue
    # Otherwise, add the first character of the input to the list of picked letters
    LetterPicked.append(letter[0])

    # If the first character of the input is in the word, print a message
    if letter[0] in word:
        print("You guessed a letter!")
    # Otherwise, print a message, reduce the number of tries by one, and print how many tries are left
    else:
        print(f"{letter} is not in the word")
        TryCounter -= 1
        print(f"You have {TryCounter} tries left")
    # Print a blank line
    print()
    # Call the Clean function to clear the screen and print the welcome message again
    Clean()
    # Call the printWord function again to update the word with guessed and hidden letters
    printWord()
    # If the last part of wordNew is equal to the word, print a message and break out of the loop
    if wordNew[-len(word):] == word:
        print(f"You won with {TryCounter} left!")
        break
    # If the number of tries is zero, print a message and break out of the loop
    if TryCounter == 0:
        print(f"You lost! The word was {word}")
        break
