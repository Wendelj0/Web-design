print("please enter the baseball palyer's information")
name = input("player name: ")
age = int(input("player age: "))
batting_avg = float(input("Player's batting average: "))

print("----------------------------")
print("Player summary")
print(f"Name: {name.title()}")
print(f"Age: {age}")
print(f"Batting average: {batting_avg}")
print("----------------------------")