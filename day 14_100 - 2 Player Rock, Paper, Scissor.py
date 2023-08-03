# Import the getpass module and rename the getpass function as input
from getpass import getpass as input

# Print a title for the game
print("EPİC 🧱📃✂ BATTLE")
# Print an empty line
print()
# Print the instructions for the players
print("Select your move (R, P or S)")
# Print another empty line
print()
# Ask player 1 to enter their move and hide their input
Player_1 = input("Player 1> ")
# Ask player 2 to enter their move and hide their input
Player_2 = input("Player 2> ")
# Check the possible outcomes of the game using if-elif-else statements
if Player_1 == "S" and Player_2 == "P":
    # If player 1 chooses scissors and player 2 chooses paper, player 1 wins
    print("Player 1 won!")
elif Player_1 == "R" and Player_2 == "S":
    # If player 1 chooses rock and player 2 chooses scissors, player 1 wins
    print("Player 1 won!")
elif Player_1 == "P" and Player_2 == "R":
    # If player 1 chooses paper and player 2 chooses rock, player 1 wins
    print("Player 1 won!")
elif Player_2 == "S" and Player_1 == "P":
    # If player 2 chooses scissors and player 1 chooses paper, player 2 wins
    print("Player 2 won!")
elif Player_2 == "R" and Player_1 == "S":
    # If player 2 chooses rock and player 1 chooses scissors, player 2 wins
    print("Player 2 won!")
elif Player_2 == "P" and Player_1 == "R":
    # If player 2 chooses paper and player 1 chooses rock, player 2 wins
    print("Player 2 won!")
elif Player_2 == "P" and Player_1 == "P":
    # If both players choose paper, it is a draw
    print("DRAW!!!")
elif Player_2 == "S" and Player_1 == "S":
    # If both players choose scissors, it is a draw
    print("DRAW!!!")
elif Player_2 == "R" and Player_1 == "R":
    # If both players choose rock, it is a draw
    print("DRAW!!!")
else:
    # If any other input is given, something is wrong
    print("Something is wrong")
# Ask the user to press any key to exit the program
a = input("")
