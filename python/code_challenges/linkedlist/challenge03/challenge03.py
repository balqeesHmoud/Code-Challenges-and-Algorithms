# Write here the code challenge solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    """
    Remove the nth node from the end of the linked list and return its head.

    Args:
        head (ListNode): The head of the linked list.
        n (int): The position of the node to remove from the end of the list.

    Returns:
        ListNode: The head of the modified linked list.
    """
    dummy = ListNode(0, head)
    first = dummy
    second = dummy

    # Move first n+1 steps ahead
    for _ in range(n + 1):
        first = first.next

    # Move first to the end, maintaining the gap
    while first:
        first = first.next
        second = second.next

    # Skip the nth node
    second.next = second.next.next

    return dummy.next
