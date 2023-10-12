# Print a question for the user
print("What generation are you a part of?")
# Print an empty line
print()
# Ask the user to enter the year they were born as an integer
year = int(input("Which year were you born? "))
# Print another empty line
print()
# Check the possible generation names based on the year using if-elif-else statements
if 1996 <= year <= 2015:
    # If the year is between 1996 and 2015, print Generation Z
    print("Generation Z")
elif 1982 <= year < 1996:
    # If the year is between 1982 and 1995, print Millennial
    print("Millennial")
elif 1965 <= year < 1982:
    # If the year is between 1965 and 1981, print Generation X
    print("Generation X")
elif 1947 <= year < 1965:
    # If the year is between 1947 and 1964, print Baby Boomers
    print("Baby Boomers")
elif 1925 <= year < 1947:
    # If the year is between 1925 and 1946, print Traditionalists
    print("Traditionalists")
else:
    # If any other input is given, print that something is wrong
    print("Did you write correctly? Dude 👀")
# Ask the user to press any key to exit the program and hide their input
a = input()
