class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_target(root, k):
    """
    Determine if there are two distinct elements in the BST that sum to a given value using a hashtable.

    Args:
        root (TreeNode): The root node of the BST.
        k (int): The target sum.

    Returns:
        bool: True if there are two distinct elements that sum to k, False otherwise.
    """
    def inorder(node):
        """Perform an in-order traversal and yield values."""
        if node:
            yield from inorder(node.left)
            yield node.value
            yield from inorder(node.right)
    
    seen = set()
    for value in inorder(root):
        if (k - value) in seen:
            return True
        seen.add(value)
    return False


# Example usage
if __name__ == "__main__":
    root = TreeNode(7)
    root.left = TreeNode(2)
    root.right = TreeNode(9)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(14)

    print(find_target(root, 3))  # Output: True
    print(find_target(root, 4))  # Output: False
    print(find_target(root, 10)) # Output: False
    print(find_target(root, 14)) # Output: True
