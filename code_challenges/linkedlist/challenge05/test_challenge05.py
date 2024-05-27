from challenge05 import ListNode, insert_after

def linked_list_to_list(head):
    """
    Converts a linked list to a Python list for easy comparison.

    Args:
        head (ListNode): The head node of the linked list.

    Returns:
        list: A list containing the values of the linked list nodes.
    """
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result

def test_insert_after():
    """
    Tests the insert_after function to ensure the new node is inserted correctly.
    """
    # Creating linked list 1 -> 2 -> 4 -> 5 -> 6
    node1 = ListNode(1)
    node2 = ListNode(2)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node1.next = node2
    node2.next = node4
    node4.next = node5
    node5.next = node6

    # New node to insert
    new_node = ListNode(3)

    # Insert new_node after node2
    insert_after(node2, new_node)

    # Convert linked list to list for easy comparison
    result = linked_list_to_list(node1)
    expected = [1, 2, 3, 4, 5, 6]

    assert result == expected
