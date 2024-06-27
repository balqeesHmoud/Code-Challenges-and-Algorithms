# test_challenge01.py

from challenge01 import ListNode, deleteNode

def create_linked_list(values):
    """
    Helper function to create a singly linked list from a list of values.

    Args:
    - values (list): List of integer values to be inserted into the linked list.

    Returns:
    - ListNode: Head node of the created linked list.
    """
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_values(head):
    """
    Helper function to get the values of a singly linked list as a list.

    Args:
    - head (ListNode): Head node of the linked list.

    Returns:
    - list: List of integer values present in the linked list.
    """
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values

def test_delete_node():
    """
    Test function for deleteNode function.

    Tests deletion of nodes from singly linked lists and prints the linked list values before and after deletion.
    """
    # Test case 1: Delete node with value 5 from linked list [4, 5, 1, 9]
    head1 = create_linked_list([4, 5, 1, 9])
    node1 = head1.next  # Node with value 5
    print(f"Linked list before deleting node with value 5: {linked_list_values(head1)}")
    deleteNode(node1)
    result1 = linked_list_values(head1)
    print(f"Linked list after deleting node with value 5: {result1}")
    assert result1 == [4, 1, 9]

    # Test case 2: Delete node with value 1 from linked list [4, 5, 1, 9]
    head2 = create_linked_list([4, 5, 1, 9])
    node2 = head2.next.next  # Node with value 1
    print(f"Linked list before deleting node with value 1: {linked_list_values(head2)}")
    deleteNode(node2)
    result2 = linked_list_values(head2)
    print(f"Linked list after deleting node with value 1: {result2}")
    assert result2 == [4, 5, 9]

test_delete_node()
