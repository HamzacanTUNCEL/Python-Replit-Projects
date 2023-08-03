print("⚔ Character Stat Generator ⚔")  # print "⚔ Character Stat Generator ⚔"


def randomHP():  # define a function named randomHP that takes no parameters
    import random  # import the random module to generate random numbers
    health1 = random.randint(1, 8)  # generate a random integer between 1 and 8 and assign it to health1
    health2 = random.randint(1, 6)  # generate a random integer between 1 and 6 and assign it to health2
    return health1 * health2  # return the product of health1 and health2


while True:  # start an infinite loop
    characterName = input("Name your warrior:")  # get user input and assign it to characterName
    print("Their health is",
          randomHP())  # print "Their health is" followed by the value returned by the randomHP function
