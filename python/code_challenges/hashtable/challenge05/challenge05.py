import pytest
from challenge05 import array_intersection

def test_array_intersection():
    assert array_intersection([1, 2, 2, 1], [2, 2]) == [2]
    assert array_intersection([4, 9, 5], [9, 4, 9, 8, 4]) == [9, 4] or array_intersection([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9]
    assert array_intersection([], [1, 2, 3]) == []
    assert array_intersection([1, 2, 3], []) == []
    assert array_intersection([1, 2, 2, 1], [2, 2, 3, 4]) == [2]
    assert array_intersection([1, 2, 3], [4, 5, 6]) == []

if __name__ == "__main__":
    pytest.main()
