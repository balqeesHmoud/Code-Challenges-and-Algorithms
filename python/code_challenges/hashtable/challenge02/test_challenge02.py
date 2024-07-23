import pytest
from challenge02 import first_repeated_word

def test_first_repeated_word():
    assert first_repeated_word("ASAC is a department at LTUC. ASAC teaches programming in LTUC.") == "asac"
    assert first_repeated_word("I am learning programming at ASAC.") == "No Repetition"
    assert first_repeated_word("This is a test. This test is simple.") == "this"
    assert first_repeated_word("No repetition here.") == "No Repetition"
    assert first_repeated_word("Word. Word, word!") == "word"

if __name__ == "__main__":
    pytest.main()
