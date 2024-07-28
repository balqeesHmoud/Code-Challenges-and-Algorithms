import pytest
from challenge04 import HashTable

def test_sort_people():
    # Test Case 1: Typical case
    names = ["Alice", "Bob", "Bob"]
    heights = [155, 185, 150]
    expected = ["Bob", "Alice", "Bob"]
    assert HashTable.sort_people(names, heights) == expected

    # Test Case 2: All same heights
    names = ["Tom", "Jerry", "Spike"]
    heights = [170, 170, 170]
    expected = ["Tom", "Jerry", "Spike"]  # Order of names doesn't change
    assert HashTable.sort_people(names, heights) == expected

    # Test Case 3: Single person
    names = ["Alice"]
    heights = [155]
    expected = ["Alice"]
    assert HashTable.sort_people(names, heights) == expected

    # Test Case 4: Two people, one taller
    names = ["John", "Jane"]
    heights = [160, 180]
    expected = ["Jane", "John"]
    assert HashTable.sort_people(names, heights) == expected

    # Test Case 5: Empty lists
    names = []
    heights = []
    expected = []
    assert HashTable.sort_people(names, heights) == expected

    # Test Case 6: Multiple people with the same height but different names
    names = ["Anna", "Ella", "Mia"]
    heights = [165, 165, 165]
    expected = ["Anna", "Ella", "Mia"]  # Order of names doesn't change
    assert HashTable.sort_people(names, heights) == expected

if __name__ == "__main__":
    pytest.main()
