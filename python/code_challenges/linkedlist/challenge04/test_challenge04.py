import pytest
from challenge04 import ListNode, reverse_linked_list

def list_to_linkedlist(lst):
    """
    Convert a list to a linked list.
    
    Args:
        lst (list): A list of values.
        
    Returns:
        ListNode: The head node of the generated linked list.
    """
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linkedlist_to_list(node):
    """
    Convert a linked list to a list.
    
    Args:
        node (ListNode): The head node of the linked list.
        
    Returns:
        list: A list of values from the linked list.
    """
    result = []
    current = node
    while current:
        result.append(current.value)
        current = current.next
    return result

def test_reverse_linked_list():
    """
    Test the reverse_linked_list function with a standard linked list.
    """
    head = list_to_linkedlist([1, 2, 3, 4, 5])
    reversed_head = reverse_linked_list(head)
    assert linkedlist_to_list(reversed_head) == [5, 4, 3, 2, 1]

def test_reverse_empty_list():
    """
    Test the reverse_linked_list function with an empty linked list.
    """
    head = list_to_linkedlist([])
    reversed_head = reverse_linked_list(head)
    assert linkedlist_to_list(reversed_head) == []

def test_reverse_single_element_list():
    """
    Test the reverse_linked_list function with a single element linked list.
    """
    head = list_to_linkedlist([1])
    reversed_head = reverse_linked_list(head)
    assert linkedlist_to_list(reversed_head) == [1]
