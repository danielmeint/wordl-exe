#!/usr/bin/env python3

def load_words(filename):
    """Load words from a file and convert to uppercase."""
    with open(filename, 'r') as file:
        return [word.strip().upper() for word in file 
               if word.strip() and len(word.strip()) == 5]

# Load both word lists
valid_words = set(load_words('words.txt'))
solutions = load_words('solutions.txt')

# Sort solutions alphabetically
solutions.sort()

# Find solutions that aren't in valid_words
invalid_solutions = [word for word in solutions if word not in valid_words]

if invalid_solutions:
    print(f"Found {len(invalid_solutions)} solutions that are not in the valid words list.")
    print("Adding them to valid words list...")
    
    # Add missing solutions to valid_words
    valid_words.update(invalid_solutions)
    
    # Convert back to sorted list and write to file
    valid_words_list = sorted(list(valid_words))
    with open('words.txt', 'w') as file:
        for word in valid_words_list:
            file.write(f"{word}\n")
    print("Updated words.txt with missing solutions")
else:
    print("All solutions are valid words!")

# Write sorted solutions back to file
with open('solutions.txt', 'w') as file:
    for word in solutions:
        file.write(f"{word}\n")

print(f"\nTotal solutions: {len(solutions)}")
print(f"Total valid words: {len(valid_words)}") 