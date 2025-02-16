print("Choose your own advenure...")
print("You find yourself in a forest hungry in search for food and shelter")
first = input("you come across two paths one on the RIGHT and one on the LEFT or you can go STRAIGHT into the forest. Where do you go: ")
if first.lower() == "right":
    print("you walk along the right path and come upon a farm")
elif first.lower() == "left":
    print("you walk along the left path for some time and find nothing you are hungry")
elif first.lower() == "straight":
    print("you walk straight in the trees and come accross a bear it kills you.")
    print("You Die!")
else : print("Invalid entry try again")

second = input("you find a pig what do you BEFRIEND or COOK it: ")
if second.lower() == "befriend":
    print("the pig accepts you as his master. You give him the name Gill")
    print("You and Gill start being friendly and getting used to each other. Suddenly you realize it's night out")
    third_1 = input("Do you CONTINUE into the night or STAY and rest: ")
    
    if third_1.lower() == "continue":
        print("You continue on the journey in the dark. you come accross a castle with no lights on")
        fourth_2 = input("do you EXPLORE the castle or GO past it: ")
        if fourth_2.lower() == "explore":
            print("you enter into the castle with your trusty pig side kick and are crowned king")
            print("The End!")
        elif fourth_2.lower() == "go":
            print("as you wonder past the castle in the night a pack of wolves comes up and eats you.")
            print("The End!")
        else : print("Invalid entry try again")
   
    elif third_1.lower() == "stay":
        print("you build a fire for the night to stay warm.")
        fourth_3 = input("the light attracts a spirit who opens a portal do you ENTER or RUN: ")
        if fourth_3.lower() == "enter":
            print("you are sucked into the portal it spits you at a castle where you are crowned king with your trusty pig by your side.")
            print("The End!")
        elif fourth_3.lower() == "run":
            print("as you are running you trip and fall into a pit full of snakes and die.")
            print("The End!")
        else : print("Invalid entry try again")

elif second.lower() == "cook":
    print("you cook the pig after a while you fall impatient and eat it early causing you to get sick and die.")
    print("The End!")
else : print("Invalid entry try again")