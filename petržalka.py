questions = [("How many days are in a year?", "365"),
    ("What is pi rounded to 2 decimals?", "3.14"),
    ("Is Slovakia in Europe?", "yes"),
    ("Is Taiwan a country?", "yes"),
    ("Who is the president of Slovakia?", "pele")]

def show_menu():
    print("=================="
          "\n------QUIZ-------"
          "\n==================")
    print("\n1. Start Game"
          "\n2. Exit")

def ask(q,a):
    user = input(q + " ")
    return user.strip().lower() == a.strip().lower()

def game():
    score = 0
    for q,a in questions:
        if ask(q,a):
            score += 1
            print("Correct!")

        else:
            print(f"Incorrect! The correct answer was {a}")
    print(f"You got {score} out of 5 correct.")

while True:
    show_menu()
    choice = int(input("-"))
    if choice == 1:
        game()
    elif choice == 2:
        print("Bye!")
        break
    else:
        print("Invalid option")

