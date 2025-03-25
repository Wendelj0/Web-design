age1 = int(input("What is the age of the first rider? "))
height1 = int(input("What is the height of the first rider? "))
second = input("Is there a second rider (y/n)? ")
 
if second == "y":
    age2 = int(input("What is the age of the second rider? "))
    height2 = int(input("What is the height of the second rider? "))
 
    if height1 < 36 or height2 < 36:
        print("You shall not ride!!")
    elif age1 >= 18 or age2 >= 18:
        print("You may jump on the ride")
    else:
        print("You shall not ride!!")
 
elif height1 >= 62 and age1 >= 18:
    print("You may jump on the ride")
else:
    print("You shall not ride!!")