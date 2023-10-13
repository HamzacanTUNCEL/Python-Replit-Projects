import os
import platform
import random

# Initialize the bingo card with 'BINGO' in the center
bingoCard = [[None, None, None],
             [None, "BINGO", None],
             [None, None, None]]

NumberList = []


# Function to sort the numbers in the bingo card
def sort_numbers():
    # Create a list to hold the numbers from the bingo card
    numbers = []
    # Loop through each cell in the bingo card
    for a in range(3):
        for b in range(3):
            # If the cell is not 'BINGO' (i.e., it's a number), add it to the list
            if bingoCard[a][b] != "BINGO":
                numbers.append(bingoCard[a][b])
    # Sort the list of numbers
    numbers.sort()
    # Replace the numbers in the bingo card with the sorted numbers
    index = 0
    for x in range(3):
        for y in range(3):
            if bingoCard[x][y] != "BINGO":
                bingoCard[x][y] = numbers[index]
                index += 1


# Function to generate a random number not already in NumberList
def random_number():
    number = random.randint(0, 90)
    while number in NumberList:
        number = random.randint(0, 90)
    NumberList.append(number)
    return number


# Function to print the bingo card
def print_bingo():
    print("+-----+------+------+")
    for k in range(3):
        for m in range(3):
            # If the cell is 'BINGO', print 'BINGO'
            if bingoCard[k][m] == "BINGO":
                print(f"|{'BINGO':^5}|", end="")
            # Otherwise, print the number
            else:
                print(f"|{bingoCard[k][m]:^5}|", end="")
        print("\n+-----+------+------+")


# Fill the bingo card with random numbers
for i in range(3):
    for j in range(3):
        if bingoCard[i][j] is None:
            bingoCard[i][j] = random_number()

# Sort the numbers in the bingo card
sort_numbers()

# Print the bingo card
print_bingo()

# Check the operating system and pause the program accordingly
if platform.system() == "Linux":
    os.system("read -r -p 'Press any key to continue...' key")
    os.system("clear")
elif platform.system() == "Windows":
    os.system("pause")
    os.system("cls")
