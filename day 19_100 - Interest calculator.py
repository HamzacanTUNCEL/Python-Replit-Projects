# Print the message "Loan Calculator" to introduce the program
print("Loan Calculator")

# Use a while loop to repeat the program until the user wants to exit
while True:
    # Use a try-except block to handle any errors
    # that might occur when the user inputs the loan amount and the interest rate
    try:
        # Ask the user to input the loan amount and convert it to a float
        initial_loan = float(input("Loan you take : "))
        # Ask the user to input the interest rate and convert it to a float
        interest_rate = float(input("Interest rate you take % : "))
        # Set the current_loan to be equal to initial_loan
        current_loan = initial_loan
    # If the input is not a valid number, print "Something is wrong" and continue the loop
    except ValueError:
        print("Something is wrong")
        continue
    # Use a for loop to iterate over 12 years
    for year in range(12):
        # Update the current_loan by adding the interest amount,
        # which is calculated by multiplying the current_loan by the interest_rate divided by 100
        current_loan += (current_loan * interest_rate) / 100
        # Print the year number and the current_loan value rounded to two decimal places
        print("Year", year + 1, " is ", round(current_loan, 2))
    # Print the total interest amount paid,
    # which is the difference between the current_loan and the initial_loan, rounded to two decimal places
    print("You paid ", round(current_loan - initial_loan, 2), "in interest!")
    # Ask the user if they want to exit the program
    Exit = input("Do you wanna exit? (Y/N):")
    # If they enter "Y" or "y", break out of the while loop
    if Exit == "Y" or Exit == "y":
        break
    # Otherwise, continue the loop and ask for new input values
    else:
        continue
