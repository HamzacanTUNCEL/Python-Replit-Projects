# Initialize a variable to store the user's choice to exit or not
Exit = ""
# Loop until the user chooses to exit
while Exit != "yes":
    # Ask the user to enter an animal name
    animal = input("What animal do you want?")
    # Check if the animal is a cow
    if animal == "cow":
        # Print the sound of a cow
        print("A cow goes moo.")
    # Check if the animal is a lemur
    elif animal == "lemur":
        # Print a funny sound for a lemur
        print("Ummm...the Lesser Spotter Lemur goes awooga.")
    # Otherwise, print that the animal sound is unknown
    else:
        print("I dont know that animal's sound")
    # Ask the user if they want to exit the loop
    Exit = input("Do you wanna exit? : ")
