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


TitleFirst = f"{Color('red', '=')}={Color('blue', '=')}{Color('yellow', ' Music App ')}{Color('red', '=')}={Color('blue', '=')}"
print(f"{TitleFirst:^85}\n")
print("🔥▶\tRadio Gaga")
print(f"\t{Color('yellow', 'Queen')}")
print("\n")
print(f"PREV\n{Color('green', 'NEXT'):^30}\n{Color('purple', 'PAUSE'):>30}\n")
