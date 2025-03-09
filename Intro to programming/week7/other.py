def generate_hint(secret_word, guess):
    hint = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint.append(guess[i].upper()) 
        elif guess[i] in secret_word:
            hint.append(guess[i].lower()) 
        else:
            hint.append('_') 
    return " ".join(hint)

def word_guessing_game(secret_word):
    secret_word = secret_word.lower()
    num_guesses = 0
    print("Welcome to the best WORDLE ever!")
    print("_ " * len(secret_word))  
    while True:
        
        guess = input("What is your guess? ").lower()
        if len(guess) != len(secret_word):
            print("Sorry, invalid geuss.")
            continue
        num_guesses += 1
        if guess == secret_word:
            print(f"Yeah Buddy!!!!!!! You got it")
            print(f"It only took you {num_guesses} guesses.")
            break
        else:
            print("Your hint is:", generate_hint(secret_word, guess))

word_guessing_game("Guild")
