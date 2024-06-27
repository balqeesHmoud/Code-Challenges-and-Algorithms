# challenge01.py

class ListNode:
    def __init__(self, val=0, next=None):
        """
        ListNode class for a singly linked list node.

        Args:
        - val (int): Value of the node.
        - next (ListNode): Reference to the next node in the linked list.
        """
        self.val = val
        self.next = next

def deleteNode(node):
    """
    Deletes a node from a singly linked list by copying the value of the next node into the current node
    and skipping over the next node.

    Args:
    - node (ListNode): Node to be deleted. It is assumed that the node is not the tail node.

    """
    # Copy the value of the next node into the current node
    node.val = node.next.val
    # Skip over the next node by updating pointers
    node.next = node.next.next
