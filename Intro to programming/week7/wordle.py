def word_guessing_game(secret_word):
    secret_word = secret_word.lower()
    num_guesses = 0

    print("Welcome to the best WORDLE ever!!!!!")
    print("_ " * len(secret_word))
    while True:
        guess = input("What is your guess? ").lower().strip()
        if len(guess) != len(secret_word):
            print("make sure your guess is the same length as the hint ;) ")
            continue

        num_guesses += 1
        if guess == secret_word:
            print(f"Yeah Buddy!!!!!!!!! You guessed it!")
            print(f"It took you {num_guesses} guesses.")
            break
        hint = ""

        for i in range(len(secret_word)):
            if guess[i] == secret_word[i]:
                hint += guess[i].upper()
            elif guess[i] in secret_word:
                hint += guess[i].lower()
            else:
                hint += "_"
        print("Your hint is:", " ".join(hint))
word_guessing_game("diety")
