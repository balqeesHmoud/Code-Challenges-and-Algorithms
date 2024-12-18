import pytest
from challenge04 import TreeNode, find_max_in_tree

def test_find_max_in_tree():
    # Example case
    root = TreeNode(1000)
    root.left = TreeNode(500)
    root.right = TreeNode(2000)
    root.left.left = TreeNode(250)
    root.left.right = TreeNode(600)
    root.right.right = TreeNode(12000)
    assert find_max_in_tree(root) == 12000

    # Test with all negative values
    root = TreeNode(-10)
    root.left = TreeNode(-20)
    root.right = TreeNode(-30)
    root.left.left = TreeNode(-40)
    root.left.right = TreeNode(-50)
    assert find_max_in_tree(root) == -10

    # Test with single node
    root = TreeNode(42)
    assert find_max_in_tree(root) == 42

    # Test with empty tree
    root = None
    assert find_max_in_tree(root) == float('-inf')

    # Test with mixed values
    root = TreeNode(1)
    root.left = TreeNode(-1)
    root.right = TreeNode(3)
    root.left.left = TreeNode(-2)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(4)
    assert find_max_in_tree(root) == 4

pytest.main()
