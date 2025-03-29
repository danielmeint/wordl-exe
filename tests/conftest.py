import pytest
import os

@pytest.fixture(autouse=True)
def ensure_word_files():
    """Ensure word files exist before running tests."""
    required_files = ["words.txt", "solutions.txt"]
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        pytest.skip(f"Missing required word files: {', '.join(missing_files)}") 