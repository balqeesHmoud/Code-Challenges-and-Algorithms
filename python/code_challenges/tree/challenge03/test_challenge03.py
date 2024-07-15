import pytest
from challenge03 import sortedArrayToBST, TreeNode, print_tree

def inorder_traversal(root: TreeNode) -> list:
    """
    Helper function to perform inorder traversal of the binary tree.
    
    Args:
        root (TreeNode): The root node of the tree.
    
    Returns:
        list: List of node values in inorder.
    """
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

def test_sortedArrayToBST():
    """
    Test cases for the sortedArrayToBST function.
    """
    # Test case 1
    nums1 = [0, -3, -10, 5, 9]
    root1 = sortedArrayToBST(nums1)
    print("Tree for nums1:")
    print_tree(root1)
    assert inorder_traversal(root1) == sorted(nums1)

    # Test case 2
    nums2 = [3, 1]
    root2 = sortedArrayToBST(nums2)
    print("Tree for nums2:")
    print_tree(root2)
    assert inorder_traversal(root2) == sorted(nums2)

    # Test case 3
    nums3 = []
    root3 = sortedArrayToBST(nums3)
    assert root3 is None

    # Test case 4
    nums4 = [1]
    root4 = sortedArrayToBST(nums4)
    print("Tree for nums4:")
    print_tree(root4)
    assert inorder_traversal(root4) == sorted(nums4)

if __name__ == "__main__":
    pytest.main()
