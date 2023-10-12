import os  # Importing os module
import time  # Importing time module

toDoList = []  # Initializing an empty list for the to-do items
print("To Do List Manager \n")  # Printing a message


# Function to print the to-do list
def printList():
  print()  # Print a new line
  for item in toDoList:
    print(item)  # Print each item in the list
  print()  # Print a new line


# Function to clear the console
def cleanConsole():
  os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console


# Function to pause the program for a specified number of seconds
def sleep(seconds):
  time.sleep(seconds)  # Sleep for the specified number of seconds


# Function to edit a to-do item
def edit(item):
  if item in toDoList:
    newItem = input(
      f"Enter new object for {item}: ")  # Prompt the user to enter a new item
    toDoList[toDoList.index(
      item)] = newItem  # Replace the existing item with the new item
  cleanConsole()  # Clear the console


# Function to delete a to-do item
def delete(item):
  if item in toDoList:
    toDoList.remove(item)  # Remove the item from the list
  else:
    print(f"{item} was not in the list \n"
          )  # Print a message if the item was not found
  cleanConsole()  # Clear the console


# Main loop to manage the to-do list
while True:
  menu = input("Do you want to view, add, or edit your to do list? \n"
               )  # Prompt the user for menu options
  if menu == "add":
    item = input("What you want to add to your to do list? \n"
                 )  # Prompt the user to enter a new item
    toDoList.append(item)  # Add the item to the list
    cleanConsole()  # Clear the console
  elif menu == "edit":
    menu1 = input("Do you wanna edit or delete an object from the list? \n"
                  )  # Prompt the user for edit options
    if menu1 == "delete":
      item = input("Which object you wanna delete? \n"
                   )  # Prompt the user for the item to delete
      delete(item)  # Delete the item
      cleanConsole()  # Clear the console
    elif menu1 == "edit":
      item = input("Which object you wanna change? \n"
                   )  # Prompt the user for the item to edit
      edit(item)  # Edit the item
      cleanConsole()  # Clear the console
  elif menu == "view":
    printList()  # Print the to-do list
    sleep(5)  # Pause for 5 seconds
    cleanConsole()  # Clear the console
