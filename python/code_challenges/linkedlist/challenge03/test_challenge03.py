# Write your test here
import pytest
from challenge03 import *

def list_to_array(head):
    """
    Helper function to convert linked list to an array.
    """
    array = []
    while head:
        array.append(head.val)
        head = head.next
    return array

def array_to_list(array):
    """
    Helper function to convert array to linked list.
    """
    dummy = ListNode()
    current = dummy
    for value in array:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

def test_remove_nth_from_end():
    test_cases = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1])
    ]
    
    for arr, n, expected in test_cases:
        head = array_to_list(arr)
        modified_head = remove_nth_from_end(head, n)
        result = list_to_array(modified_head)
        assert result == expected

if __name__ == "__main__":
    pytest.main()
