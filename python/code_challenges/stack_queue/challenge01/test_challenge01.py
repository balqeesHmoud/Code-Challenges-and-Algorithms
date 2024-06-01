# Write your test here

import pytest
from challenge01 import MyQueue

def test_my_queue():
    """
    Test cases for MyQueue implementation.
    """
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    assert myQueue.peek() == 1, "Peek operation failed"  # Should return 1
    assert myQueue.pop() == 1, "Pop operation failed"  # Should return 1
    assert not myQueue.empty(), "Empty operation failed (should be False)"  # Should return False
    assert myQueue.pop() == 2, "Pop operation failed"  # Should return 2
    assert myQueue.empty(), "Empty operation failed (should be True)"  # Should return True

if __name__ == "__main__":
    pytest.main()
