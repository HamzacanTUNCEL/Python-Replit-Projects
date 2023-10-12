# Importing necessary modules
import os
import time

# Initializing an empty list for emails
listOfEmail = []


# Function to sleep for 1 second and clear the console
def sleepAndClear():
    time.sleep(1)
    os.system("cls")


# Function to display the list of emails in a formatted way
def prettyPrint():
    os.system("cls")
    print("list Of Email")
    print()
    for index in range(len(listOfEmail)):
        print(f"{index + 1}: {listOfEmail[index]}")
    time.sleep(1)


# Function to send spam emails
def spam(max):
    for i in range(max):
        if i in range(len(listOfEmail)):
            # Printing the spam email content
            print(f"""Sent email to 
    {listOfEmail[i]} {i + 1}

    Dear {listOfEmail[i]}
    It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

    Love and hugs,
    Ian Spammington III
    """)
            # Calling the sleepAndClear function
            sleepAndClear()
        else:
            # printing the number of missing email
            # print(f"There was {len(listOfEmail)} email")
            print(f"There was {i} email")
            # Calling the sleepAndClear function
            sleepAndClear()
            break
        i += 1


# Main loop
while True:
    print("SPAMMER Inc.")
    menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
    if menu == "1":
        email = input("Email > ")
        listOfEmail.append(email)
    elif menu == "2":
        email = input("Email > ")
        if email in listOfEmail:
            listOfEmail.remove(email)
    elif menu == "3":
        # Calling the prettyPrint function
        prettyPrint()
    elif menu == "4":
        maxEmail = 10
        # Calling the spam function
        spam(maxEmail)
    # Calling the sleepAndClear function
    sleepAndClear()
