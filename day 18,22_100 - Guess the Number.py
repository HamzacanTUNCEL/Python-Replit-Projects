# Import the random module to generate random numbers
import random

# Use a while loop to repeat the game until the user wants to exit
while True:
    # Print the name of the game
    print("One-Million-To-One")
    # Generate a random number between 1 and 1 million and assign it to ENumber
    ENumber = random.randint(1, 1000000)
    # Initialize a counter variable to keep track of the number of guesses
    counter = 0
    # Use another while loop to repeat the guessing process until the user gets it right
    while True:
        # Increment the counter by 1 for each guess
        counter += 1
        # Ask the user to input their guess and assign it to number
        number = input("What is your guess?")
        # Check if the input is a string of letters
        if number.isalpha():
            # If so, print "Type number" and continue the loop
            print("Type number")
            continue
        # Otherwise, convert the input to an integer
        else:
            number = int(number)
        # Check if the input is equal to ENumber
        if number == ENumber:
            # If so, print "Correct" and the number of guesses it took
            print("Correct")
            print("It took you", counter, "guesses to get it")
            # Break out of the inner loop
            break
        # Check if the input is greater than ENumber
        elif number > ENumber:
            # If so, print "Too high"
            print("Too high")
        # Check if the input is less than ENumber
        elif number < ENumber:
            # If so, print "Too low"
            print("Too low")
    # Ask the user if they want to guess a new number
    Exit = input("Do you wanna guess a new number? (Y/N)")
    # If they enter "Y", continue the outer loop and generate a new ENumber
    if Exit == "Y":
        continue
    # Otherwise, exit the program
    else:
        exit()
