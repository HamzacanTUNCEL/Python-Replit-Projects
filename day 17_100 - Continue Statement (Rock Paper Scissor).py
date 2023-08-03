# Import the getpass module to hide the input from the screen
from getpass import getpass as input

# Print some escape sequences to change the color and background of the text
print("\033[2;32;44m")
# Print the name of the game
print("EPİC 🧱📃✂ BATTLE")
# Print an empty line
print()
# Print the instructions for the players to choose their moves
print("Select your move (R, P or S)")
# Print another empty line
print()
# Initialize two variables to keep track of the scores of each player
ScorePlayer_1 = 0
ScorePlayer_2 = 0
# Use a while loop to repeat the game until one of the players wins three times
while True:
    # Ask the first player to input their move and hide it from the screen
    Player_1 = input("Player 1> ")
    # Ask the second player to input their move and hide it from the screen
    Player_2 = input("Player 2> ")
    # Check if the first player chose scissors and the second player chose paper
    if Player_1 == "S" and Player_2 == "P":
        # If so, print that the first player won and update their score by 1
        print("Player 1 won!")
        print("Score : Player 1:", ScorePlayer_1, " Player 2", ScorePlayer_2)
        print()
        ScorePlayer_1 += 1
    # Check if the first player chose rock and the second player chose scissors
    elif Player_1 == "R" and Player_2 == "S":
        # If so, print that the first player won and update their score by 1
        print("Player 1 won!")
        print("Score : Player 1:", ScorePlayer_1, " Player 2", ScorePlayer_2)
        print()
        ScorePlayer_1 += 1
    # Check if the first player chose paper and the second player chose rock
    elif Player_1 == "P" and Player_2 == "R":
        # If so, print that the first player won and update their score by 1
        print("Player 1 won!")
        print("Score : Player 1:", ScorePlayer_1, " Player 2", ScorePlayer_2)
        print()
        ScorePlayer_1 += 1
    # Check if the second player chose scissors and the first player chose paper
    elif Player_2 == "S" and Player_1 == "P":
        # If so, print that the second player won and update their score by 1
        print("Player 2 won!")
        print("Score : Player 1:", ScorePlayer_1, " Player 2", ScorePlayer_2)
        print()
        ScorePlayer_2 += 1
    # Check if the second player chose rock and the first player chose scissors
    elif Player_2 == "R" and Player_1 == "S":
        # If so, print that the second player won and update their score by 1
        print("Player 2 won!")
        print("Score : Player 1:", ScorePlayer_1, " Player 2", ScorePlayer_2)
        print()
        ScorePlayer_2 += 1
    # Check if the second player chose paper and the first player chose rock
    elif Player_2 == "P" and Player_1 == "R":
        # If so, print that the second player won and update their score by 1
        print("Player 2 won!")
        print("Score : Player 1:", ScorePlayer_1, " Player 2", ScorePlayer_2)
        print()
        ScorePlayer_2 += 1
    # Check if both players chose paper
    elif Player_2 == "P" and Player_1 == "P":
        # If so, print that it is a draw and keep the scores unchanged
        print("DRAW!!!")
        print("Score : Player 1:", ScorePlayer_1, " Player 2", ScorePlayer_2)
        print()
    # Check if both players chose scissors
    elif Player_2 == "S" and Player_1 == "S":
        # If so, print that it is a draw and keep the scores unchanged
        print("DRAW!!!")
        print("Score : Player 1:", ScorePlayer_1, " Player 2", ScorePlayer_2)
        print()
    # Check if both players chose rock
    elif Player_2 == "R" and Player_1 == "R":
        # If so, print that it is a draw and keep the scores unchanged
        print("DRAW!!!")
        print("Score : Player 1:", ScorePlayer_1, " Player 2", ScorePlayer_2)
        print()
    # If none of the above conditions are met, print that something is wrong and keep the scores unchanged
    else:
        print("Something is wrong")
        print("Score : Player 1:", ScorePlayer_1, " Player 2", ScorePlayer_2)
        print()

    # Check if the first player has reached a score of 3
    if ScorePlayer_1 == 3:
        # If so, print that they won the game and ask them if they want to restart the game
        print()
        print("Player 1 won the game")
        a = input("Do you wanna restart the game?(Y/N) :")
        # If they enter "N", exit the program
        if a == "N":
            exit()
        # Otherwise, reset the scores to 0 and continue the outer loop
        else:
            ScorePlayer_1 = 0
            ScorePlayer_2 = 0
            continue
    # Check if the second player has reached a score of 3
    elif ScorePlayer_2 == 3:
        # If so, print that they won the game and ask them if they want to restart the game
        print()
        print("Player 2 win the game")
        a = input("Do you wanna restart the game?(Y/N) :")
        # If they enter "N", exit the program
        if a == "N":
            exit()
        # Otherwise, reset the scores to 0 and continue the outer loop
        else:
            ScorePlayer_1 = 0
            ScorePlayer_2 = 0
            continue
    # If neither player has reached a score of 3, continue the outer loop and ask for new moves
    else:
        continue

# Ask for an empty input to prevent the program from closing immediately
a = input("")
