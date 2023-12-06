import os
import time
import platform

# Create an empty list to store the to-do list items.
toDoList = []

# Function that allows the user to pause execution.
def Pause():
    """Function that allows the user to pause."""
    if platform.system() == "Windows":
        os.system("pause")  # Pauses execution on Windows systems.
    else:
        input('Press Enter to continue...')  # Pauses execution on non-Windows systems.

# Function that clears the screen with a slight delay.
def Clear():
    """Clears the screen with a short delay."""
    time.sleep(1)  # 1 second delay.
    if platform.system() == "Linux":
        os.system('clear')  # Clears the terminal screen on Linux.
    elif platform.system() == "Windows":
        os.system('cls')  # Clears the command prompt on Windows.

# Function used to add a new item to the to-do list.
def addItem():
    """Adds a new item to the to-do list."""
    Name = input("Enter the name of the item: ").strip().capitalize()
    Date = input("Enter the due date of the item: ").strip().capitalize()
    Priority = input("Enter the priority of the item: ").strip().capitalize()
    row = {"Name": Name, "Date": Date, "Priority": Priority}  # Create a dictionary for the new item.
    toDoList.append(row)  # Add the new item to the todo list.

# Function used to view items in the to-do list.
def viewList():
    """Displays the to-do list or items with a specific priority."""
    option = input(
        "Press 1 to view all items\nPress 2 to view items with a specific priority\n"
    )
    if option == "1":
        # Displays all items in the to-do list.
        print()
        for row in toDoList:
            counter = 0
            for key, value in row.items():
                if counter < 2:
                    print(key, value, sep=": ", end=" \t")
                    counter += 1
                else:
                    print(key, value, sep=": ", end="\n")
        print()
        Pause()
    elif option == "2":
        # Displays items with a specific priority.
        priority = input("Enter the priority of the item: ")
        for row in toDoList:
            counter = 0
            for key, value in row.items():
                if row["Priority"] == priority:
                    if counter < 2:
                        print(key, value.capitalize(), sep=": ", end=" ")
                        counter += 1
                    else:
                        print(key, value.capitalize(), sep=": ", end="\n")
        Pause()

# Function used to remove an item from the to-do list based on priority.
def removeItem():
    """Removes an item from the to-do list based on priority."""
    priority = input("Enter item's priority to remove: ")
    item_found = False  # Flag to track if the item is found or not.

    for row in toDoList:
        for key, value in row.items():
            if row["Priority"] == priority:
                toDoList.remove(row)  # Removing the item from the list.
                print("Item removed from list")
                item_found = True
                Pause()
                break
            else:
                continue
            break
    if not item_found:
        print("Item not found in any row")

# Function used to edit items in the to-do list.
def editItem():
    """Edits items in the to-do list."""
    option = input(
        "Press 1 to change item in a row\nPress 2 to change all items in a row\n")
    if option == "1":
        option_alt = input("Press 1 to change name\nPress 2 to change date\nPress 3 to change priority\n")
        if option_alt == "1":
            edit("Name")  # Editing the name of an item.
        elif option_alt == "2":
            edit("Date")  # Editing the date of an item.
        elif option_alt == "3":
            edit("Priority")  # Editing the priority of an item.
    elif option == "2":
        item = input("Enter item's Priority to edit: ")
        for row in toDoList:
            for key, value in row.items():
                if row["Priority"] == item:
                    for key in row:
                        row[key] = input(f"Enter new {key}: ")
                else:
                    continue
                break    

# Function used to edit a specific field (name, date, priority) of an item.
def edit(name):
    """Edits a specific field (name, date, priority) of an item."""
    item = input(f"Enter item to edit: ")
    for row in toDoList:
        if row[name] == item:
            row[name] = input(f"Enter new {name}: ").strip().capitalize()

# Main loop that displays the menu and performs actions based on user input.
while True:
    menu = input("1. Add item\n2. View list\n3. Remove item\n4. Edit item\n")
    if menu == "1":
        Clear()
        addItem()  # Calling the function to add an item.
        Clear()
    elif menu == "2":
        Clear()
        viewList()  # Calling the function to view the list.
        Clear()
    elif menu == "3":
        Clear()
        removeItem()  # Calling the function to remove an item.
        Clear()
    elif menu == "4":
        Clear()
        editItem()  # Calling the function to edit an item.
        Clear()
    else:
        print("Invalid option")
    Clear()