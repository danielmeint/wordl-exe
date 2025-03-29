# Terminal Wordle

A Wordle clone that runs in the terminal, featuring color-coded feedback for your guesses.

## Setup

1. Make sure you have Python 3.6+ installed
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Play

Run the game:
```bash
python wordle.py
```

- You have 6 attempts to guess a 5-letter word
- After each guess, you'll get color-coded feedback:
  - 🟩 Green: Correct letter in correct position
  - 🟨 Yellow: Correct letter in wrong position
  - ⬜ White: Letter not in the word
- Enter your guesses in uppercase or lowercase
- The game will validate your guesses against a list of valid words

## Features

- Color-coded feedback using ANSI escape codes
- Word validation
- Play again option
- Cross-platform support (Windows, macOS, Linux)

## Future Improvements

- Load words from external file
- Daily word mode
- Statistics tracking
- Hard mode