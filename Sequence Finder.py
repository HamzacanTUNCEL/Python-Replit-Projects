print()
myString = input("Type something: ")
while True:
    print()
    myNumber = input("Type a number: ")
    x = myNumber[0]
    y = myNumber[1]
    z = myNumber[2]
    print()
    counter = 0
    for letter in myString:
        if counter + 2 < len(myString) and letter == x and myString[counter + 1] == y and myString[counter + 2] == z:
            print('\033[33m', end='')
            print(letter, end='')
            print('\033[0m', end='')
            counter += 1
        elif counter + 1 < len(myString) and letter == y and myString[counter - 1] == x and myString[counter + 1] == z:
            print('\033[33m', end='')
            print(letter, end='')
            print('\033[0m', end='')
            counter += 1
        elif letter == z and myString[counter - 1] == y and myString[counter - 2] == x:
            print('\033[33m', end='')
            print(letter, end='')
            print('\033[0m', end='')
            counter += 1
        else:
            print(letter, end='')
            counter += 1
