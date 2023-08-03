# Start an infinite loop
while True:
    # Print the title of the game
    print("Math Game!")
    # Try to get the user input for the name of multiples
    try:
        NameOfMultiples = int(input("Name of multiples: "))
    # If the input is not a valid integer, go back to the start of the loop
    except ValueError:
        continue
    # Initialize a variable to store the score
    point = 0
    # Loop through the numbers from 1 to 10
    for i in range(1, 11, 1):
        # Print the multiplication question
        print(i, "x", NameOfMultiples, "=")
        # Try to get the user input for the answer
        try:
            answer = int(input())
        # If the input is not a valid integer, go back to the start of the loop
        except ValueError:
            print("The answer was", i * NameOfMultiples)
            continue
        # Check if the answer is correct
        if answer == i * NameOfMultiples:
            # Print a positive feedback and increment the score
            print("Great Work! 🎉")
            point += 1
        else:
            # Print a negative feedback and show the correct answer
            print("Nope! 😭 The answer was", i * NameOfMultiples)
    # Print the final score
    print("You scored", point, "out of 10!")
    # Ask the user if they want to exit the game
    Exit = input("Do you want to exit? (Y/N): ")
    # If the user input is one of the possible exit options, break out of the loop
    if Exit == "Y" or Exit == "y" or Exit == "Yes" or Exit == "YES":
        break
    # Otherwise, continue the loop
    else:
        continue
