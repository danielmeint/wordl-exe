# Terminal Wordle

[![Lint](https://github.com/danielmeint/wordl-exe/actions/workflows/lint.yml/badge.svg)](https://github.com/danielmeint/wordl-exe/actions/workflows/lint.yml)
[![Test](https://github.com/danielmeint/wordl-exe/actions/workflows/test.yml/badge.svg)](https://github.com/danielmeint/wordl-exe/actions/workflows/test.yml)
[![Validate Words](https://github.com/danielmeint/wordl-exe/actions/workflows/validate_words.yml/badge.svg)](https://github.com/danielmeint/wordl-exe/actions/workflows/validate_words.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python-based Wordle clone that runs in the terminal, featuring color-coded feedback for your guesses.

## Features

- 🎯 Full Wordle gameplay with 6 attempts to guess a 5-letter word
- 🎨 Color-coded feedback using ANSI colors:
  - 🟩 Green: Correct letter in correct position
  - 🟨 Yellow: Correct letter in wrong position
  - ⬜ White: Letter not in word
- 📚 Two-tier word system:
  - ~15,000 valid words for guessing
  - ~5,700 common words used as solutions
- ✅ Input validation
- 🔄 Play again option
- 🖥️ Cross-platform support (Windows, macOS, Linux)

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

- Type your 5-letter word guess and press Enter
- The game will show color-coded feedback for each letter
- You have 6 attempts to guess the word
- Only valid English 5-letter words are accepted
- The solution will always be a common 5-letter word

## Word Lists

The game uses two word lists:
- `words.txt`: All valid 5-letter words that can be used as guesses (~15k words)
- `solutions.txt`: Common 5-letter words that can be chosen as solutions (~5.7k words)

## Development

### Code Style

This project uses:
- `black` for code formatting
- `flake8` for linting
- `pytest` for testing

To format code:
```bash
black .
```

To run linting:
```bash
flake8
```

To run tests:
```bash
pytest
```

### CI/CD

GitHub Actions workflows are set up for:
- Code linting and formatting checks
- Running tests
- Validating word lists

These checks run automatically on:
- Push to main branch
- Pull requests

## Future Improvements

- [ ] Daily word mode (same word for everyone on a given day)
- [ ] Statistics tracking (wins, streak, guess distribution)
- [ ] Hard mode (must use revealed hints in subsequent guesses)
- [ ] Save game state