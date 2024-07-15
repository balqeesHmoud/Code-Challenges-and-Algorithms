from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    """
    Convert a sorted array to a height-balanced binary search tree (BST).

    Args:
        nums (List[int]): A sorted list of integers.

    Returns:
        Optional[TreeNode]: The root node of the height-balanced BST.

    Example:
        >>> nums = [0, -3, -10, 5, 9]
        >>> root = sortedArrayToBST(nums)
        >>> print_tree(root)
        Root: 0
            L--- -3
                L--- -10
                R--- None
            R--- 9
                L--- 5
                R--- None
    """
    if not nums:
        return None

    def helper(left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None
        
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = helper(left, mid - 1)
        node.right = helper(mid + 1, right)
        return node
    
    return helper(0, len(nums) - 1)

def print_tree(root: TreeNode, level=0, prefix="Root: "):
    """
    Helper function to print the binary tree structure.

    Args:
        root (TreeNode): The root node of the tree.
        level (int): The current level in the tree (used for indentation).
        prefix (str): The prefix string for the current node.
    """
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            if root.left:
                print_tree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")

if __name__ == "__main__":
    nums = [0, -3, -10, 5, 9]
    bst_root = sortedArrayToBST(nums)
    print_tree(bst_root)
