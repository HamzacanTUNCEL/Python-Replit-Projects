# Define a function named Color that takes two parameters: color and word
def Color(color, word):
    # If the color parameter is "red", print the word parameter in red color
    if color == "red":
        print("\033[31m", word, sep="", end="")
    # If the color parameter is "green", print the word parameter in green color
    elif color == "green":
        print("\033[32m", word, sep="", end="")
    # If the color parameter is "yellow", print the word parameter in yellow color
    elif color == "yellow":
        print("\033[33m", word, sep="", end="")
    # If the color parameter is "blue", print the word parameter in blue color
    elif color == "blue":
        print("\033[34m", word, sep="", end="")
    # If the color parameter is "purple", print the word parameter in purple color
    elif color == "purple":
        print("\033[35m", word, sep="", end="")
    # If the color parameter is anything else, print the word parameter in default color
    else:
        print("\033[0m", word, sep="", end="")


# Print "Ali" in default color
print("Ali", end=" ")
# Call the Color function with "blue" and "Ayşe" as arguments
Color("blue", "Ayşe")
# Reset the color to default
Color("reset", "")
