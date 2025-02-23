print("welcome to the word guessing game!")

magicword = "fast"
yourword = str(input("Choose a word: "))
counter=1
while yourword != magicword:
    counter+=1
    yourword = str(input("guess again: "))
    if yourword == magicword:
        print("you guessed it!")
        print(counter)
print("good job!")
 
