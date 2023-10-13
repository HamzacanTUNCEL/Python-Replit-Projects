# Print "STAR WARS NAME GENERATOR"
print("STARWARS NAME GENERATOR")

while True:
    # Prompt user to enter Name, Surname, Mother's Name, and City of Birth, and strip and capitalize the inputs
    Name = input("Enter Name: ").strip().capitalize()
    Surname = input("Enter Surname: ").strip().capitalize()
    MotherName = input("Enter Mother's Name: ").strip().capitalize()
    CityBorn = input("Enter City Where You Born: ").strip().capitalize()

    print()

    # Generate Star Wars name based on provided inputs
    print(
        f"{Name[0:3].capitalize()}{Surname[0:2].lower()} {MotherName[0:2].capitalize()}{CityBorn[-3:].lower()}"
    )

    print()

    # Prompt user to enter first name, last name, Mother's name, and City of birth all at once, split the input into a list
    StarwarsName = input(
        "Enter your first name, last name, Mother's name and the City you were born in: "
    ).split()

    print()

    # Generate Star Wars name based on the split input
    print(
        f"{StarwarsName[0][0:3].capitalize()}{StarwarsName[1][0:2].lower()} {StarwarsName[2][0:2].capitalize()}{StarwarsName[3][-3:].lower()}"
    )
