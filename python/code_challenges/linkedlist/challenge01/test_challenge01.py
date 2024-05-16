# Write your test here
from challenge01 import ListNode, deleteNode

def create_linked_list(values):
    # Helper function to create a linked list from a list of values
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_values(head):
    # Helper function to get the values of a linked list as a list
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values

def test_delete_node():
    # Test case 1: Delete node with value 5 from linked list [4, 5, 1, 9]
    head1 = create_linked_list([4, 5, 1, 9])
    node1 = head1.next  # Node with value 5
    deleteNode(node1)
    assert linked_list_values(head1) == [4, 1, 9]

    # Test case 2: Delete node with value 1 from linked list [4, 5, 1, 9]
    head2 = create_linked_list([4, 5, 1, 9])
    node2 = head2.next.next  # Node with value 1
    deleteNode(node2)
    assert linked_list_values(head2) == [4, 5, 9]


