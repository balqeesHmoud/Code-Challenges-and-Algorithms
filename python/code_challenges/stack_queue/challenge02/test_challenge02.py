
import pytest
from challenge02 import is_valid

def test_is_valid():
    assert is_valid("()") == True
    assert is_valid("()[]{}") == True
    assert is_valid("[({}]") == False
    assert is_valid("[(hello)()]") == True
    assert is_valid("[{(())}]") == True
    assert is_valid("") == True
    assert is_valid("(([]){})") == True
    assert is_valid("([)]") == False
    assert is_valid("{[]}") == True

if __name__ == "__main__":
    pytest.main()
