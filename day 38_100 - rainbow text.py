# Set the color based on the provided color parameter
def Color(color, letterToColor):
    if color == "red":
        print("\033[31m" + letterToColor, end="")
    elif color == "green":
        print("\033[32m" + letterToColor, end="")
    elif color == "yellow":
        print("\033[33m" + letterToColor, end="")
    elif color == "blue":
        print("\033[34m" + letterToColor, end="")
    elif color == "purple":
        print("\033[35m" + letterToColor, end="")
    elif color == "white":
        print("\033[0m" + letterToColor, end="")


while True:
    # Get input sentence from the user and split it into words
    myString = input("What sentence do you want rainbow-ising?\n").split()

    for sentence in myString:
        for letter in sentence:
            # Check each letter in the word and apply color based on its value
            if letter.lower() == "b":
                Color("blue", letter)
            elif letter.lower() == "r":
                Color("red", letter)
            elif letter.lower() == "g":
                Color("green", letter)
            elif letter.lower() == "y":
                Color("yellow", letter)
            elif letter.lower() == "p":
                Color("purple", letter)
            else:
                # If the letter doesn't match any color, print it as is
                print(letter, end='')

        # Add a space after each word
        Color("white", " ")

    # Add a newline after each sentence
    Color("white", "\n")
