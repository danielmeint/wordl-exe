import pytest
from wordle import load_words, is_valid_word, print_colored_guess

def test_load_words():
    """Test that word loading works correctly."""
    words = load_words("words.txt")
    assert len(words) > 0
    assert all(len(word) == 5 for word in words)
    assert all(word.isupper() for word in words)

def test_is_valid_word():
    """Test word validation."""
    # Test with valid words
    assert is_valid_word("APPLE")
    assert is_valid_word("BEACH")
    
    # Test with invalid words
    assert not is_valid_word("INVALID")
    assert not is_valid_word("TOOLONG")
    assert not is_valid_word("XXXXX")  # Using a definitely invalid word

def test_print_colored_guess(capsys):
    """Test the colored output of guesses."""
    # Test correct letter in correct position
    print_colored_guess("APPLE", "APPLE")
    captured = capsys.readouterr()
    assert "A" in captured.out
    assert "P" in captured.out
    assert "L" in captured.out
    assert "E" in captured.out

    # Test correct letter in wrong position
    print_colored_guess("APPLE", "PAPER")
    captured = capsys.readouterr()
    assert "A" in captured.out
    assert "P" in captured.out
    assert "L" in captured.out
    assert "E" in captured.out

    # Test letter not in word
    print_colored_guess("APPLE", "STORM")
    captured = capsys.readouterr()
    assert "A" in captured.out
    assert "P" in captured.out
    assert "L" in captured.out
    assert "E" in captured.out 