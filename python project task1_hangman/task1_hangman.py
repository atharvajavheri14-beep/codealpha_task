import random

WORDS = ["python", "developer", "hangman", "keyboard", "monitor"]

HANGMAN_STAGES = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """,
]


def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def hangman():
    word = random.choice(WORDS)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman!")
    print("=" * 30)

    while incorrect_guesses < max_incorrect:
        print(HANGMAN_STAGES[incorrect_guesses])
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break

        guess = input("\nEnter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Wrong! '{guess}' is not in the word.")
    else:
        print(HANGMAN_STAGES[max_incorrect])
        print(f"\nGame over! The word was: {word}")


if __name__ == "__main__":
    hangman()
