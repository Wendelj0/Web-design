grade = int(input("What is your grade in this class: "))
if grade >= 90:
    letter = "an A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
elif grade >= 50:
    letter = "F"
print(f"Your grade is: {letter}")
if grade >= 70:
    print("You pass!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
if grade < 70:
    print("you failed!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")