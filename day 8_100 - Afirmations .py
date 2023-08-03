# Print a title for the program
print("Wholesome Positivity Machine")
# Print an empty line
print("")
# Ask the user to enter their name
name = input("""Who are you?
""")
# Ask the user to enter the day of the week
day = input("""what day is it today?
""")
# Check if the user's input is a valid weekday using if-else statements
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday" or day == "Sunday":
    # If yes, print a confirmation message with the day
    print("Oh yeah,today is", day)
else:
    # If no, print an error message
    print("There is no week day like that")
    # Print an empty line
    print()
# Check the user's input for each weekday using if-elif-else statements and print a corresponding motivational message
if day == "Monday" or day == "monday":
    print(
        "May this week bring you new opportunities and fresh beginnings. You have the strength and determination to overcome any challenges that come your way. Believe in yourself and embrace the possibilities ahead"
    )
elif day == "Tuesday" or day == "tuesday":
    print(
        "You are capable and resourceful. Each day is a chance for you to showcase your talents and make a positive impact. Stay focused, stay motivated, and watch as you achieve great things."
    )
elif day == "Wednesday" or day == "wednesday":
    print(
        "Embrace the middle of the week with a positive mindset. You have accomplished so much already, and there's still more to come. Trust in your abilities, stay resilient, and let your light shine."
    )
elif day == "Thursday" or day == "thursday":
    print(
        "You radiate confidence and positivity. Embrace this day with a sense of excitement and openness. Believe in your dreams and know that you have the power to turn them into reality. Keep going, and success will follow."
    )
elif day == "Friday" or day == "friday":
    print(
        "You've reached the end of the week, and you've done an incredible job. Take a moment to appreciate your hard work and achievements. You deserve to relax and recharge, knowing that you've given your best."
    )
elif day == "Saturday" or day == "saturday":
    print(
        "Enjoy the weekend to its fullest. Take time for yourself, indulge in activities that bring you joy, and replenish your energy. You deserve this moment of rest and rejuvenation. Embrace the beauty of the present."
    )
elif day == "Sunday" or day == "sunday":
    print(
        "As a new week approaches, take this day to reflect, recharge, and set intentions for the days ahead. Believe in your abilities, stay focused on your goals, and approach the coming week with a calm and confident spirit."
    )
# Ask the user to enter what they want to achieve
achievement = input("""What do you want to achieve?
""")

# Ask the user to rate their mood on a scale of 1-10
scaleFeeling = input("""On a scale of 1-10 how do you feel today?
""")
# Check the user's input for each number using if-elif-else statements and print a corresponding supportive message
if scaleFeeling == "1":
    print(
        name,
        " I understand you're feeling discouraged, but remember that tomorrow is a new opportunity."
    )
elif scaleFeeling == "2":
    print("Hey", name,
          ", I see you're having a rough day, but keep pushing forward.")
elif scaleFeeling == "3":
    print(
        "Hi", name,
        ", I know you're feeling down, but remember that tough times don't last forever."
    )
elif scaleFeeling == "4":
    print(name,
          " I can sense you're not at your best today, but hang in there.")
elif scaleFeeling == "5":
    print(
        name,
        " you're in a decent mood today, and that's a step in the right direction."
    )
elif scaleFeeling == "6":
    print(
        "Hi", name,
        ", it seems like you're doing okay, but I know you have the potential for greatness."
    )
elif scaleFeeling == "7":
    print("Hey", name,
          ", I sense a positive energy from you today, keep it up!.")
elif scaleFeeling == "8":
    print(name,
          "your enthusiasm is infectious. You're definitely in a good mood!")
elif scaleFeeling == "9":
    print("Hi", name,
          ", you're radiating positivity today, and it's refreshing.")
elif scaleFeeling == "10":
    print(name,
          " you're absolutely killing it! Your upbeat attitude is unmatched.")
else:
    # If any other input is given, print a playful message
    print("Come on!")
# Ask the user to press any key to exit the program
a = input()
