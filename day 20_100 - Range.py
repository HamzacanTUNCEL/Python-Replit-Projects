# This program asks the user for a starting point, an ending point and an increment
# and prints the values in that range
while True:  # Loop until the user wants to exit
    try:
        # Ask the user for the inputs and convert them to integers
        StartingPoint = int(input("Start at: "))
        FinalPoint = int(input("Ending Value: "))
        Increment = int(input("Increment between values: "))
    except ValueError:  # Handle the exception if the input is not a valid integer
        print("Something went wrong")
        continue  # Go back to the start of the loop
    # ---------------------------------------------------------------
    # Adjust the ending point according to the sign of the increment
    if FinalPoint < 0:
        FinalPoint -= 1
    else:
        FinalPoint += 1

    for i in range(StartingPoint, FinalPoint, Increment):  # Print the values in the range using a for loop
        print(i)
    Exit = input("Do you want to exit? (Y/N): ")  # Ask the user if they want to exit
    if Exit == "Y" or Exit == "y" or Exit == "Yes" or Exit == "YES":
        break
    else:
        continue
