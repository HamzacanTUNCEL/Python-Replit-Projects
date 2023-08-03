# Define a variable to store the number of seconds in a minute
OneMin = 60
# Define a variable to store the number of minutes in an hour
OneHour = 60
# Define a variable to store the number of hours in a day
OneDay = 24
# Calculate the number of seconds in a day by multiplying the previous variables
SecondsInADay = OneMin * OneHour * OneDay
# Print the result with a message
print("Total seconds in a day is ", SecondsInADay)
# Ask the user to enter the number of days in a year as an integer
OneYear = int(input("How many days in a year? "))
# Check if the user's answer is 365
if OneYear == 365:
    # Uncomment the next line if you want to add 6 hours to the year
    # plus6Hour=6*OneHour*OneMin
    # Calculate the number of seconds in a year by multiplying the seconds in a day by 365
    SecondsInAYear = SecondsInADay * OneYear  # +plus6Hour
    # Print the result with a message
    print("Total seconds in a year is", SecondsInAYear)
# Check if the user's answer is 366
elif OneYear == 366:
    # Print that it is a leap year
    print("It's a leap year.")
    # Calculate the number of seconds in a year by multiplying the seconds in a day by 366
    SecondsInAYear = SecondsInADay * OneYear
    # Print the result with a message
    print("Total seconds in a year is", SecondsInAYear)
else:
    # If any other input is given, print that something is wrong
    print("Something is wrong")
# Ask the user to press any key to exit the program
a = input()
