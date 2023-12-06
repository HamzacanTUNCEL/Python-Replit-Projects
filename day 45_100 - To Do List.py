import os
import time
import platform

toDoList = []

def Pause():
    print("Press Enter to continue...")
    input()

def Clear():
    time.sleep(1)
    if platform.system() == "Linux":
        os.system('clear')
    elif platform.system() == "Windows":
        os.system('cls')

def addItem():
    Name = input("Enter the name of the item: ")
    Date = input("Enter the due date of the item: ")
    Priority = input("Enter the priority of the item: ")
    row = {"Name": Name, "Date": Date, "Priority": Priority}
    toDoList.append(row)

def viewList():
    option = input(
        "Press 1 to view all items\nPress 2 to view items with a specific priority\n"
    )
    if option == "1":
        print()
        for row in toDoList:
            counter = 0
            for key, value in row.items():
                if counter < 2:
                    print(key, value.capitalize(), sep=": ", end=" ")
                    counter += 1
                else:
                    print(key, value.capitalize(), sep=": ", end="\n")

        print()
        Pause()
    elif option == "2":
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

def removeItem():
    priority = input("Enter item's priority to remove: ")
    item_found = False

    for row in toDoList:
        for key, value in row.items():
            if row["Priority"] == priority:
                toDoList.remove(row)
                print("Item removed from list")
                item_found = True
                Pause()
                break
            else:
                continue
            break
    if not item_found:
        print("Item not found in any row")

def editItem():
    option = input(
        "Press 1 to change item in a row\nPress 2 to change all items in a row\n")
    if option == "1":
        option_alt = input("Press 1 to change name\nPress 2 to change date\nPress 3 to change priority\n")
        if option_alt == "1":
            edit("Name")
        elif option_alt == "2":
            edit("Date")
        elif option_alt == "3":
            edit("Priority")
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

def edit(name):
    item = input("Enter item to edit: ")
    for row in toDoList:
        if row[name] == item:
            row[name] = input(f"Enter new {name}: ")

while True:
    menu = input("1. Add item\n2. View list\n3. Remove item\n4. Edit item\n")
    if menu == "1":
        Clear()
        addItem()
        Clear()
    elif menu == "2":
        Clear()
        viewList()
        Clear()
    elif menu == "3":
        Clear()
        removeItem()
        Clear()
    elif menu == "4":
        Clear()
        editItem()
        Clear()
    else:
        print("Invalid option")
    Clear()
