#import random

#magic_number = random.randint(1, 10)

#guess = -1
#while guess != magic_number:
    #guess = int(input("What is your guess? "))

  #  if guess < magic_number:
   #     print("Higher")
 #   elif guess > magic_number:
  
#      print("Lower")
 #   else:
#        print("You guessed it!")

import random
 
play_again = "Y"
while play_again.upper() == "Y":
    magicnumber = random.randint(1,10)
    yournumber = int(input("Choose a number from 1-10: "))
    counter=1
    while yournumber != magicnumber:
        counter+=1
        if yournumber > magicnumber:
            print("Your number is too high!")
        if yournumber < magicnumber:
            print ("Your number is too low")
        yournumber= int(input("Choose a new number: "))
 
    if counter == 1:
        amount = "try"
    else:
        amount = "tries"
    print(f"You guessed it! The magic number was {magicnumber}. It took you {counter} {amount}! YIPPEE!!!")
    play_again= input("Do you want to play again? y/n: ")
 