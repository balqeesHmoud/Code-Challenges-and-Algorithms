# Write here the code challenge solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(node):
    # Copy the value of the next node into the current node
    node.val = node.next.val
    # Skip over the next node by updating pointers
    node.next = node.next.next
