from wordle import load_words, is_valid_word, print_colored_guess
from colorama import Fore, Style


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
    # Test all correct (all green)
    print_colored_guess("APPLE", "APPLE")
    captured = capsys.readouterr()
    expected = (
        f"{Fore.GREEN}A {Fore.GREEN}P {Fore.GREEN}P {Fore.GREEN}L {Fore.GREEN}E "
        f"{Style.RESET_ALL}\n"
    )
    assert captured.out == expected

    # Test mixed positions with repeated letters
    # PAPER has two P's, so both P's in APPLE should be marked:
    # - First P: yellow (exists but wrong position)
    # - Second P: green (correct position)
    print_colored_guess("APPLE", "PAPER")
    captured = capsys.readouterr()
    expected = (
        f"{Fore.YELLOW}A {Fore.YELLOW}P {Fore.GREEN}P {Fore.WHITE}L {Fore.YELLOW}E "
        f"{Style.RESET_ALL}\n"
    )
    assert captured.out == expected

    # Test no matches (all white)
    print_colored_guess("APPLE", "STORM")
    captured = capsys.readouterr()
    expected = (
        f"{Fore.WHITE}A {Fore.WHITE}P {Fore.WHITE}P {Fore.WHITE}L {Fore.WHITE}E "
        f"{Style.RESET_ALL}\n"
    )
    assert captured.out == expected
