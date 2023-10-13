import os  # Import the os module
import time  # Import the time module

toDoList = []  # Initialize an empty list to store to-do items


def Sleep():  # Define a function named Sleep
    time.sleep(1)  # Sleep for 1 second


def Clear():  # Define a function named Clear
    os.system("cls")  # Clear the console


def Pause():  # Define a function named Pause
    input("Press Enter to Continue...")  # Wait for user input


def add():  # Define a function named add
    item = input("What would you like to add to your list? "
                 )  # Prompt user for a to-do item
    toDoList.append(item)  # Add the item to the to-do list


def view():  # Define a function named view
    if len(toDoList) > 0:  # Check if the to-do list is not empty
        counter = 1  # Initialize a counter variable
        for item in toDoList:  # Iterate over each item in the to-do list
            print(
                f"{counter}) {item}")  # Print the item with its corresponding number
            counter += 1  # Increment the counter
        Pause()  # Wait for user input
    else:  # If the to-do list is empty
        print("There are no items in your list.")  # Display a message


def delete(Name):  # Define a function named delete that takes an argument Name
    toDoList.remove(Name)  # Remove the specified item from the to-do list


def Change(Name):  # Define a function named Change that takes an argument Name
    if Name in toDoList:  # Check if the item exists in the to-do list
        item = input(
            "What would you like to change to? ")  # Prompt user for a new value
        index = toDoList.index(Name)  # Get the index of the item
        toDoList[index] = item  # Replace the item with the new value
        Pause()  # Wait for user input
        Clear()  # Clear the console
    else:  # If the item does not exist in the to-do list
        print("Item not found in the list.")  # Display a message
        Pause()  # Wait for user input
        Clear()  # Clear the console


while True:  # Run an infinite loop
    print("To Do List Manager:")  # Display a message
    menu = input(
        """Do you want to view, add, edit, or remove an item from the to do list?

  1) View
  2) Add
  3) Delete
  4) Change
  5) Exit

  """)  # Prompt user for their choice
    Sleep()  # Call the Sleep function
    Clear()  # Call the Clear function

    if menu == "1":  # If the user chooses to view
        view()  # Call the view function
        Sleep()  # Call the Sleep function
        Clear()  # Call the Clear function

    elif menu == "2":  # If the user chooses to add
        add()  # Call the add function
        Sleep()  # Call the Sleep function
        Clear()  # Call the Clear function

    elif menu == "3":  # If the user chooses to delete
        objectName = input("Enter the name of the item you want to delete: \n"
                           )  # Prompt user for the item name
        s = input(f"Are you sure you want to delete {objectName}? (y/n) \n").lower(
        )  # Prompt user for confirmation
        Sleep()  # Call the Sleep function
        Clear()  # Call the Clear function
        if s[0] == "y":  # If the user confirms the deletion
            if objectName in toDoList:  # If the item exists in the to-do list
                delete(objectName)  # Call the delete function
                Sleep()  # Call the Sleep function
                Clear()  # Call the Clear function
            else:  # If the item does not exist in the to-do list
                print("Item not found in the list.")  # Display a message
                Pause()  # Wait for user input
                Clear()  # Call the Clear function
        else:  # If the user cancels the deletion
            pass  # Do nothing
            Sleep()  # Call the Sleep function
            Clear()  # Call the Clear function

    elif menu == "4":  # If the user chooses to change
        ChangeObject = input("Enter the name of the item you want to change: \n"
                             )  # Prompt user for the item name
        Sleep()  # Call the Sleep function
        Clear()  # Call the Clear function
        Change(ChangeObject)  # Call the Change function

    elif menu == "5":  # If the user chooses to exit
        print("Goodbye!")  # Display a farewell message
        Sleep()  # Call the Sleep function
        Clear()  # Call the Clear function
        break  # Exit the loop
