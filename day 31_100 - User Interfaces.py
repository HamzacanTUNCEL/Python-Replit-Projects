def Color(color, word):
    if color == "red":
        return "\033[31m" + word + "\033[0m"
    elif color == "green":
        return "\033[32m" + word + "\033[0m"
    elif color == "yellow":
        return "\033[33m" + word + "\033[0m"
    elif color == "blue":
        return "\033[34m" + word + "\033[0m"
    elif color == "purple":
        return "\033[35m" + word + "\033[0m"
    else:
        return "\033[0m" + word + "\033[0m"


Title = "WELCOME TO"
subTitle = "--   ARM-BOOK  --"
subTitle = Color("blue", subTitle)
print(f"{Title:^25}\n{subTitle:^32}\n", end="")

print()

myText = Color("yellow", "Definitely not a rip off of")
myText1 = Color("yellow", "a certain other social")
myText2 = Color("yellow", "networking site.")
myText3 = Color("red", "Honest.")
print(f"{myText:>50}\n{myText1:>50}\n{myText2:>50}\n", end="")
print(f"{myText3:^33}")

print()

Username = input(f"{'Username: ':^25}\n")
Password = input(f"{'Password: ':^25}\n")
