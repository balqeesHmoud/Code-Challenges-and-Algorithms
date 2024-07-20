# Write here the code challenge solution
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def max_height_of_tree(root):
    """
    Calculate the maximum height of a binary tree.

    Args:
        root (TreeNode): The root node of the tree.

    Returns:
        int: The maximum height of the tree.

    Example:
        >>> root = TreeNode(10)
        >>> root.left = TreeNode(20)
        >>> root.right = TreeNode(30)
        >>> root.left.left = TreeNode(40)
        >>> root.left.right = TreeNode(28)
        >>> root.right.left = TreeNode(27)
        >>> root.right.right = TreeNode(50)
        >>> root.left.right.left = TreeNode(29)
        >>> max_height_of_tree(root)
        4
    """
    if not root:
        return 0
    left_height = max_height_of_tree(root.left)
    right_height = max_height_of_tree(root.right)
    return max(left_height, right_height) + 1

# Example usage
if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(20)
    root.right = TreeNode(30)
    root.left.left = TreeNode(40)
    root.left.right = TreeNode(28)
    root.right.left = TreeNode(27)
    root.right.right = TreeNode(50)
    root.left.right.left = TreeNode(29)

    print(max_height_of_tree(root))  # Output: 4
