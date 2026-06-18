# Hangman Unique

A simple Python command-line Hangman game that selects a random word and tracks used words between sessions.

## Features

- Random word selection from a predefined list
- Prevents reuse of a word until all words have been used
- Displays hangman progress art for wrong guesses
- Tracks guessed letters and shows game progress
- Supports replaying the game after each round
- Allows quitting mid-game by typing `QUIT`

## Files

- `hangman_unique.py` - Main game script


## Requirements

- Python 3.6 or higher

## Usage

1. Open a terminal in the project folder.
2. Run the game:

```bash
python hangman_unique.py
```

3. Enter a single alphabetic letter when prompted.
4. Type `QUIT` to exit the game early.
5. After a game ends, choose `y` or `n` to play again.

## Notes

- The word list is defined inside `hangman_unique.py` and can be updated as needed.
