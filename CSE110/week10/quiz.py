questions = ["Red Robin or Chilis?", "Subway or Jimmy Johns?", "Cafe Rio or Costa Vida?"]
answers = ["Red Robin", "Subway", "Cafe Rio"]
for i, question in enumerate(questions):
    print(question)
    youre_anwswer = input("Your answer: ")
    if youre_anwswer.title() == answers[i]:
        print("good work")
    else:
        print("you suck!")
    
