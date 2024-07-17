class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_max_in_tree(root):
    """
    Finds the maximum value in a binary tree using in-order traversal.

    Args:
    root (TreeNode): The root node of the binary tree.

    Returns:
    int: The maximum value in the tree. Returns float('-inf') if the tree is empty.

    Example:
    >>> root = TreeNode(1000)
    >>> root.left = TreeNode(500)
    >>> root.right = TreeNode(2000)
    >>> root.left.left = TreeNode(250)
    >>> root.left.right = TreeNode(600)
    >>> root.right.right = TreeNode(12000)
    >>> find_max_in_tree(root)
    12000
    """
    if root is None:
        return float('-inf')
    
    left_max = find_max_in_tree(root.left)
    right_max = find_max_in_tree(root.right)
    
    return max(root.value, left_max, right_max)

# Usage Example
if __name__ == "__main__":
    root = TreeNode(1000)
    root.left = TreeNode(500)
    root.right = TreeNode(2000)
    root.left.left = TreeNode(250)
    root.left.right = TreeNode(600)
    root.right.right = TreeNode(12000)
    
    print("Maximum value in the tree:", find_max_in_tree(root))
