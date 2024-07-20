import pytest
from challenge01 import TreeNode, find_target

def test_find_target():
    # Create the test BST
    root = TreeNode(7)
    root.left = TreeNode(2)
    root.right = TreeNode(9)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(14)

    # Test case 1: Should return True because 2 + 1 = 3
    assert find_target(root, 3) == True
    
    # Test case 2: Should return False because no combination sums to 4
    assert find_target(root, 4) == False

    # Test case 3: Should return True because 5 + 9 = 14
    assert find_target(root, 14) == True

    # Test case 4: Should return False because no pair sums to 0
    assert find_target(root, 0) == False

    # Test case 5: Should return False because no pair sums to 15
    assert find_target(root, 15) == False

pytest.main()
