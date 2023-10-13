import os
import platform
import random

# Initialize the bingo card with 'BINGO' in the center
bingo_card = [[None,    None,   None],
              [None,   "BINGO", None],
              [None,    None,   None]]

generated_numbers = []


# Function to wait for user input
def wait_for_input():
    if platform.system() == "Linux":
        os.system("read -r -p 'Press any key to continue...' key")
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("pause")
        os.system("cls")


# Function to sort the numbers in the bingo card
def sort_bingo_numbers():
    card_numbers = []
    for a in range(3):
        for b in range(3):
            if bingo_card[a][b] != "BINGO":
                if bingo_card[a][b] != "X":
                    card_numbers.append(bingo_card[a][b])
    card_numbers.sort()
    sorted_index = 0
    for a in range(3):
        for b in range(3):
            if bingo_card[a][b] != "BINGO":
                if bingo_card[a][b] != "X":
                    bingo_card[a][b] = card_numbers[sorted_index]
                    sorted_index += 1


# Function to generate a random number not already in generated_numbers
def generate_random_number():
    random_number = random.randint(0, 90)
    while random_number in generated_numbers:
        random_number = random.randint(0, 90)
    generated_numbers.append(random_number)
    return random_number


# Function to print the bingo card
def print_bingo_card():
    print("+-----+------+------+")
    for a in range(3):
        for b in range(3):
            if bingo_card[a][b] == "BINGO":
                print(f"|{'BINGO':^5}|", end="")
            elif bingo_card[a][b] == "X":
                print(f"|{'X':^5}|", end="")
            else:
                print(f"|{bingo_card[a][b]:^5}|", end="")
        print("\n+-----+------+------+")


# Fill the bingo card with random numbers
def fill_bingo_card():
    for a in range(3):
        for b in range(3):
            if bingo_card[a][b] is None:
                bingo_card[a][b] = generate_random_number()
    sort_bingo_numbers()


# Check if the user's number is in the card
def check_number_in_card(user_number_input):
    for a in range(3):
        for b in range(3):
            if bingo_card[a][b] == user_number_input:
                bingo_card[a][b] = "X"


# Check if there's a bingo
def check_for_bingo():
    global cross_count
    cross_count = 0
    for a in range(3):
        for b in range(3):
            if bingo_card[a][b] == "X":
                cross_count += 1


# Fill the bingo card
fill_bingo_card()
while True:
    user_number = int(input("Enter a number: "))
    check_number_in_card(user_number)
    check_for_bingo()
    print(cross_count)
    wait_for_input()
    if cross_count == 8:
        print("BINGO!!!")
        if platform.system() == "Linux":
            os.system("read -r -p 'Press any key to continue...' key")
        elif platform.system() == "Windows":
            os.system("pause")
        break

print_bingo_card()
wait_for_input()
