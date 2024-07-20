# Write your test here
import pytest
from challenge05 import TreeNode, max_height_of_tree

def test_max_height_of_tree():
    root = TreeNode(10)
    root.left = TreeNode(20)
    root.right = TreeNode(30)
    root.left.left = TreeNode(40)
    root.left.right = TreeNode(28)
    root.right.left = TreeNode(27)
    root.right.right = TreeNode(50)
    root.left.right.left = TreeNode(29)

    assert max_height_of_tree(root) == 4

    assert max_height_of_tree(TreeNode(1)) == 1

    assert max_height_of_tree(None) == 0

if __name__ == "__main__":
    pytest.main()
