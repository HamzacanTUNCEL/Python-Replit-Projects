PeopleList = []


# Function to print the list
def printList():
    print()
    for i in PeopleList:
        print(i)
    print()


# Function to add person to the list
def People(ContactPerson):
    PeopleList.append(ContactPerson)


# Infinite loop to continuously prompt for name and surname
while True:
    Name = input("Enter Name: ").strip().capitalize()
    Surname = input("Enter Surname:  ").strip().capitalize()
    Person = Name + " " + Surname

    # Check if person is already in the list
    if Person not in PeopleList:
        People(Person)
        printList()
    else:
        print("Error: Name already exists")
