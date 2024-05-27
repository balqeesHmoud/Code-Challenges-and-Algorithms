class ListNode:
    """
    Class representing a node in a singly linked list.

    Attributes:
        value (int): The value stored in the node.
        next (ListNode): The reference to the next node in the list, defaults to None.
    """
    def __init__(self, value=0, next=None):
        """
        Initializes a ListNode with a specified value and next node reference.

        Args:
            value (int): The value to be stored in the node.
            next (ListNode, optional): The next node in the list. Defaults to None.
        """
        self.value = value
        self.next = next

def insert_after(node, new_node):
    """
    Inserts a new node after a given node in a singly linked list.

    Args:
        node (ListNode): The node after which the new node will be inserted.
        new_node (ListNode): The new node to insert into the list.

    Returns:
        None
    """
    if node is None:
        return
    new_node.next = node.next
    node.next = new_node
