import pytest
from challenge03 import HashTable 
def test_sum_of_unique_elements():
    # Create an instance of HashTable
    ht = HashTable()
    
    # Test case 1: Normal case with unique and non-unique elements
    nums1 = [1, 2, 3, 2]
    expected_output1 = 4  # 1 + 3
    assert ht.sum_of_unique_elements(nums1) == expected_output1
    
    # Test case 2: All elements are unique
    nums2 = [1, 2, 3, 4, 5]
    expected_output2 = 15  # 1 + 2 + 3 + 4 + 5
    assert ht.sum_of_unique_elements(nums2) == expected_output2
    
    # Test case 3: All elements are the same
    nums3 = [2, 2, 2, 2]
    expected_output3 = 0  # No unique elements
    assert ht.sum_of_unique_elements(nums3) == expected_output3
    
    # Test case 4: Empty list
    nums4 = []
    expected_output4 = 0  # No elements
    assert ht.sum_of_unique_elements(nums4) == expected_output4
    
    # Test case 5: List with one unique element and one duplicate
    nums5 = [5, 5, 7]
    expected_output5 = 7  # Only 7 is unique
    assert ht.sum_of_unique_elements(nums5) == expected_output5
    
    # Test case 6: List with multiple unique elements and duplicates
    nums6 = [10, 20, 10, 30, 30, 40]
    expected_output6 = 60  # 20 + 40
    assert ht.sum_of_unique_elements(nums6) == expected_output6

if __name__ == "__main__":
    pytest.main()
