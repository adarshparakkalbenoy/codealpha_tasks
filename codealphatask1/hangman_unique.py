import os
import random

WORDS = ["python", "hangman", "string", "random", "console"]
MAX_WRONG = 6
TRACK_FILENAME = "used_words.txt"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRACK_FILE = os.path.join(BASE_DIR, TRACK_FILENAME)

HANGMAN_STAGES = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]


def get_word():
    used = set()

    if os.path.exists(TRACK_FILE):
        with open(TRACK_FILE, "r", encoding="utf-8") as f:
            used = {line.strip() for line in f if line.strip()}

    available = [word for word in WORDS if word not in used]

    if not available:
        available = WORDS[:]
        with open(TRACK_FILE, "w", encoding="utf-8"):
            pass

    word = random.choice(available)

    with open(TRACK_FILE, "a", encoding="utf-8") as f:
        f.write(word + "\n")

    return word


def display_state(word, guessed_letters, wrong_guesses):
    print(HANGMAN_STAGES[min(wrong_guesses, MAX_WRONG)])
    progress = " ".join(letter if letter in guessed_letters else "_" for letter in word)
    print("\nWord:", progress)
    print("Guessed letters:", " ".join(sorted(guessed_letters)) if guessed_letters else "None")
    print("Wrong guesses left:", MAX_WRONG - wrong_guesses)


def prompt_guess():
    return input("Enter a letter (or type QUIT to exit): ").strip().lower()


def play_game():
    word = get_word()
    guessed_letters = set()
    wrong_guesses = 0

    print("\n=== HANGMAN ===")
    print("Guess the word one letter at a time.")
    print("Maximum incorrect guesses:", MAX_WRONG)

    while True:
        display_state(word, guessed_letters, wrong_guesses)

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You found the word:", word)
            return

        if wrong_guesses >= MAX_WRONG:
            print("Game Over! The word was:", word)
            return

        guess = prompt_guess()

        if guess == "quit":
            print("Thanks for playing.")
            raise SystemExit

        if len(guess) != 1 or not guess.isalpha():
            print("Enter exactly one alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!")
        else:
            wrong_guesses += 1
            print("Incorrect!")


def main():
    while True:
        try:
            play_game()
        except SystemExit:
            break

        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again not in ("y", "yes"):
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
