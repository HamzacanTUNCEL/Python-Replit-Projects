print("Exam Grade Calculator")
print()
NameOfExam = input("Name of exam: ")
print()
MaxPossibleScore = int(input("Max. Possible Score: "))
print()
YourScore = int(input("Your Score: "))
print()
ScorePercentage = (YourScore / MaxPossibleScore) * 100
print(round(ScorePercentage))
print()
if 90 <= ScorePercentage <= 100:
    print("Letter grade of ", NameOfExam, "is A+")
elif 80 <= ScorePercentage < 90:
    print("Letter grade of ", NameOfExam, "is A")
elif 70 <= ScorePercentage < 80:
    print("Letter grade of ", NameOfExam, "is B")
elif 60 <= ScorePercentage < 70:
    print("Letter grade of ", NameOfExam, "is C")
elif 50 <= ScorePercentage < 60:
    print("Letter grade of ", NameOfExam, "is D")
elif ScorePercentage < 50:
    print("Letter grade of ", NameOfExam, "is U")
else:
    print("")
print("""
    Letter Grade	Percentage
              A+	90-100
               A	80-89
               B	70-79
               C	60-69
               D	50-59
               U	under 50
""")
input()
