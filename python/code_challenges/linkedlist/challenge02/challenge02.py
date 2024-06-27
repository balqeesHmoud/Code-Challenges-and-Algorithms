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
# Usage example
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Initialize the Solution class
    solution = Solution()

    # Find the middle node
    middle_node = solution.middleNode(head)

    # Print the value of the middle node
    if middle_node:
        print(f"The middle node value is: {middle_node.val}")
    else:
        print("The linked list is empty.")