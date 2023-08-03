import random  # import the random module to generate random numbers


def infDice(Sides):  # define a function named infDice that takes one parameter Sides
    numRolled = random.randint(1, Sides)  # generate a random integer between 1 and Sides and assign it to numRolled
    print("You rolled", numRolled)  # print "You rolled" followed by the value of numRolled


print("Infinite Dice 🎲")  # print "Infinite Dice 🎲"
try:  # try to execute the following block of code
    side = int(input("How many sides?: "))  # get user input and convert it to an integer and assign it to side
except:  # if an exception occurs (such as a ValueError if the input is not a valid integer)
    print("Something went wrong!")  # print "Something went wrong!"
else:  # if no exception occurs
    input()  # get user input and ignore it (this is not necessary)
while True:  # start an infinite loop
    infDice(side)  # call the infDice function with the value of side as the argument
    Exit = input("Roll again? ")  # get user input and assign it to Exit
    if Exit == "No" or Exit == "N" or Exit == "no" or Exit == "n":  # if Exit is one of these strings
        break  # break out of the while loop
    else:  # else (Exit is not one of these strings)
        continue  # continue the while loop (this is not necessary since the loop will continue anyway)
