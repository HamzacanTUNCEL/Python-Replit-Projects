# Print a message to introduce the game
print("""Fill in the blank lyrics!
(Type in the blank lyrics and see if you are as cool as me.)""")
# Use a while loop to repeat the game until the user wants to exit
while True:
    # Initialize an empty string variable to store the user's input
    # Use another while loop to repeat the first question until the user gets it right
    while True:
        # Print the first question with a blank
        print("""Never gonna ______ you up.""")
        # Ask the user to input their answer and assign it to lyric
        lyric = input()
        # Check if the answer is "give"
        if lyric == "give":
            # If so, print the correct lyrics and reset lyric to an empty string
            print("""Never gonna give you up.""")
            lyric = ""
            # Break out of the inner loop
            break
        # Otherwise, print "try again" and continue the loop
        else:
            print("try again")
    # Use another while loop to repeat the second question until the user gets it right
    while True:
        # Print the second question with a blank
        print("""Never gonna ______ you down.""")
        # Ask the user to input their answer and assign it to lyric
        lyric = input()
        # Check if the answer is "let"
        if lyric == "let":
            # If so, print the correct lyrics and reset lyric to an empty string
            print("""Never gonna let you down.""")
            lyric = ""
            # Break out of the inner loop
            break
        # Otherwise, print "try again" and continue the loop
        else:
            print("try again")
    # Use another while loop to repeat the third question until the user gets it right
    while True:
        # Print the third question with a blank
        print("""Never gonna ______ you cry.""")
        # Ask the user to input their answer and assign it to lyric
        lyric = input()
        # Check if the answer is "make"
        if lyric == "make":
            # If so, print the correct lyrics and reset lyric to an empty string
            print("""Never gonna make you cry.""")
            lyric = ""
            # Break out of the inner loop
            break
        # Otherwise, print "try again" and continue the loop
        else:
            print("try again")
            # Ask the user if they want to exit the game
    Exit = input("Do you wanna exit? : ")
    # If they enter "yes", break out of the outer loop
    if Exit == "yes":
        break
