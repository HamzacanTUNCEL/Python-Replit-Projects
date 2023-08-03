import os
import random
import time


def rollDice(side):
    result = random.randint(1, side)
    return result


def health():
    healthStat = ((rollDice(6) * rollDice(12)) / 2) + 10
    return healthStat


def strength():
    strengthStat = ((rollDice(6) * rollDice(8)) / 2) + 12
    return strengthStat


print("⚔️ CHARACTER BUILDER ⚔️")
print()
c1name = input("Name your Legend:\n")
c1type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(c1name)
c1Health = health()
c1Strength = strength()
print("HEALTH:", c1Health)
print("STRENGTH:", c1Strength)
print()
print("Who are they battling?")
print()

c2name = input("Name your Legend:\n")
c2type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(c2name)
c2Health = health()
c2Strength = strength()
print("HEALTH:", c2Health)
print("STRENGTH:", c2Strength)
print()

round = 1
winner = None

while True:

    time.sleep(1)
    os.system("cls")
    print("⚔️ BATTLE TIME ⚔️")
    print()
    print("The battle begins!")

    c1Dice = rollDice(6)
    c2Dice = rollDice(6)

    difference = abs(c1Strength - c2Strength) + 1

    if c1Dice > c2Dice:
        c2Health -= difference
        if round == 1:
            print(c1name, "wins the first blow")
        else:
            print(c1name, "wins round", round)
    elif c2Dice > c1Dice:
        c1Health -= difference
        if round == 1:
            print(c2name, "wins the first blow")
        else:
            print(c2name, "wins round", round)
    else:
        print("Their swords clash and they draw round", round)

    print()
    print(c1name)
    print("HEALTH:", c1Health)
    print()
    print(c2name)
    print("HEALTH:", c2Health)
    print()

    if c1Health <= 0:
        print(c1name, "has died")
        winner = c2name
        break
    elif c2Health <= 0:
        print(c1name, "has died")
        winner = c1name
        break
    else:
        print("And they're both standing for the next round")
        round += 1
time.sleep(1)
os.system("cls")
print("⚔️ BATTLE TIME ⚔️")
print()
print(winner, "has won in", round, "rounds")
input()
