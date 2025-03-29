#!/usr/bin/env python3
import random
from colorama import init, Fore, Style

# Initialize colorama for cross-platform color support
init()


def load_words(filename):
    """Load words from a file and convert to uppercase."""
    try:
        with open(filename, "r") as file:
            return [
                word.strip().upper()
                for word in file
                if word.strip() and len(word.strip()) == 5
            ]
    except FileNotFoundError:
        print(f"{Fore.RED}Error: {filename} not found!{Style.RESET_ALL}")
        exit(1)


# Load both word lists
VALID_WORDS = set(load_words("words.txt"))  # All valid guesses
SOLUTION_WORDS = load_words("solutions.txt")  # Words that can be solutions


def print_colored_guess(guess, target):
    """Print the guess with color-coded feedback."""
    # Convert to lists for easier manipulation
    guess_chars = list(guess)
    target_chars = list(target)
    colors = [None] * len(guess)

    # First pass: mark exact matches
    for i, (g, t) in enumerate(zip(guess_chars, target_chars)):
        if g == t:
            colors[i] = Fore.GREEN
            target_chars[i] = None  # Mark as used

    # Second pass: mark yellow and white
    for i, g in enumerate(guess_chars):
        if colors[i] is not None:
            continue

        # Check if the letter exists in remaining positions
        if g in target_chars:
            colors[i] = Fore.YELLOW
            target_chars[target_chars.index(g)] = None  # Mark as used
        else:
            colors[i] = Fore.WHITE

    # Print the colored guess
    for color, letter in zip(colors, guess):
        print(f"{color}{letter}", end=" ")
    print(Style.RESET_ALL)


def is_valid_word(word):
    """Check if the word is in our valid words list."""
    return word.upper() in VALID_WORDS


def play_wordle():
    """Main game loop."""
    target = random.choice(SOLUTION_WORDS)
    max_guesses = 6
    guesses = 0

    print("\nWelcome to Terminal Wordle!")
    print("Guess the 5-letter word. You have 6 attempts.")
    print(
        "Colors: Green = correct position, "
        "Yellow = wrong position, White = not in word\n"
    )

    while guesses < max_guesses:
        guess = input(f"Enter guess #{guesses + 1}: ").strip().upper()

        if len(guess) != 5:
            print("Please enter a 5-letter word!")
            continue

        if not is_valid_word(guess):
            print("Not a valid word! Try again.")
            continue

        print_colored_guess(guess, target)
        guesses += 1

        if guess == target:
            print(
                f"\n{Fore.GREEN}Congratulations! "
                f"You won in {guesses} guesses!{Style.RESET_ALL}"
            )
            return True

    print(f"\n{Fore.RED}Game Over! The word was: {target}{Style.RESET_ALL}")
    return False


if __name__ == "__main__":
    while True:
        play_wordle()
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again != "y":
            break
    print("\nThanks for playing!")
