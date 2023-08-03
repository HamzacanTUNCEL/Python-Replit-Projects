# Ask the user to enter the bill amount as a float
myBill = float(input("What was the bill?: "))
# Ask the user to enter the tip percentage as an integer
myTipPerc = int(input("what percentage do you want to tip? "))
# Calculate the tip amount by multiplying the bill by the tip percentage and dividing by 100
myTip = (myBill * myTipPerc) / 100
# Ask the user to enter the number of people as an integer
numberOfPeople = int(input("How many people?: "))
# Calculate the total bill by adding the bill and the tip
totalBill = myBill + myTip
# Calculate the amount each person owes by dividing the total bill by the number of people
answer = totalBill / numberOfPeople
# Round the answer to two decimal places
answer = round(answer, 2)
# Print the result with a message
print("You all owe", answer)
# Ask the user to press any key to exit the program
a = input()
