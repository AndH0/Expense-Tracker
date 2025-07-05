import random

print("""
---------------------------
Welcome to the HANGMAN game
---------------------------

1. 2 players
2. 1 player
""")

players = int(input("Choose mode (1 or 2): "))

if players == 2:
    print("2-player mode is not yet implemented. Try single-player mode!")
elif players == 1:
    guessed = []
    words = ["apple", "orange", "banana", "coconut"]
    word = random.choice(words)  # Choose a random word
    attempts = 6  # Set a maximum number of incorrect guesses

    print("\nWelcome to Single-Player Mode!")
    print(f"The word has {len(word)} letters. You have {attempts} attempts to guess it.")

    while attempts > 0:
        # Display the word with guessed letters
        display_word = ''.join([letter if letter in guessed else '_' for letter in word])
        print("\nWord:", display_word)

        # Check if the player has guessed the word
        if '_' not in display_word:
            print("Congratulations! You've guessed the word!")
            break

        # Ask for a guess
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed:
            print(f"You already guessed '{guess}'. Try another letter.")
        elif guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            guessed.append(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            guessed.append(guess)
            attempts -= 1
            print(f"Remaining attempts: {attempts}")

    if attempts == 0:
        print(f"Game Over! The word was '{word}'. Better luck next time!")




