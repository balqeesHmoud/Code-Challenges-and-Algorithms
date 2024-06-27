class ListNode:
    """
    Definition for a singly linked list node.
    
    Attributes:
        value (int): The value of the node.
        next (ListNode): The next node in the linked list.
    """
    def __init__(self, value=0, next=None):
        """
        Initialize a new ListNode.
        
        Args:
            value (int): The value of the node.
            next (ListNode, optional): The next node in the linked list. Defaults to None.
        """
        self.value = value
        self.next = next

def reverse_linked_list(head: ListNode) -> ListNode:
    """
    Reverse a singly linked list.
    
    Args:
        head (ListNode): The head node of the linked list to be reversed.
        
    Returns:
        ListNode: The new head node of the reversed linked list.
    """
    prev = None
    current = head
    
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev

# Usage example
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> None
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    # Print the original linked list
    print("Original Linked List:")
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

    # Reverse the linked list
    new_head = reverse_linked_list(head)

    # Print the reversed linked list
    print("\nReversed Linked List:")
    current = new_head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
