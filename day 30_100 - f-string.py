# Print a message to ask the user what they thought of the challenge
print("30 Days down - What did you think?")

# Use a for loop to iterate over the 30 days
for i in range(1, 31):
    # Use the input function to get the user's response for each day
    response = input(f"Day {i}:\n")
    # Print an empty line for spacing
    print()
    # Assign a string to a variable called myText
    myText = f"You thought Day {i} was"
    # Assign the user's response to a variable called myText2
    myText2 = f"{response}"
    # Print the variables myText and myText2 in a formatted way using center alignment
    print(f"{myText:^30}\n{myText2:^30}", end=" ")
    # Print an empty line for spacing
    print()
