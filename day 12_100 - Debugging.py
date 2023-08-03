# Print a title for the quiz
print("100 Days of Code QUIZ")
# Print an empty line
print()
# Print a question for the user
print("How many can you answer correctly?")
# Ask the user to enter the name of the language we are writing in
ans1 = input("What language are we writing in?")
# Check if the user's answer is python
if ans1 == "python":
    # If yes, print correct
    print("Correct")
else:
    # If no, print nope with an emoji
    print("Nope🙈")
# Ask the user to enter the lesson number as an integer
ans2 = int(input("Which lesson number is this?"))
# Check if the user's answer is greater than 12
if ans2 > 12:
    # If yes, print that we are not that far yet
    print("We're not quite that far yet")
# Check if the user's answer is equal to 12
elif ans2 == 12:
    # If yes, print that's right
    print("That's right!")
else:
    # If no, print that we have gone well past that
    print("We've gone well past that!")
