speed = int(input("Input vehicle speed mph: "))
is_truck = str("Is your vehicle a truck? y/n")
if speed > 55 or speed > 40 and is_truck == "y":
    print("SLOW DOWN!!!!!!")
elif speed < 30:
    print("Thank you!")
else:
    print("speed up!!!!")
