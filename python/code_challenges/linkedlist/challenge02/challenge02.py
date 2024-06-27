class ListNode:
    """
    Node class to represent a single node in the linked list
    """
    def __init__(self, val=0, next=None):
        """
        Initializes a ListNode with a value and optional next node reference.

        Args:
            val (int): Value of the node.
            next (ListNode, optional): Reference to the next ListNode. Defaults to None.
        """
        self.val = val
        self.next = next

class Solution:
    """
    Solution class with methods related to linked list operations.
    """
    def middleNode(self, head: ListNode) -> ListNode:
        """
        Finds the middle node of a linked list using the slow and fast pointers approach.

        Args:
            head (ListNode): Head of the linked list.

        Returns:
            ListNode: Middle node of the linked list.
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
