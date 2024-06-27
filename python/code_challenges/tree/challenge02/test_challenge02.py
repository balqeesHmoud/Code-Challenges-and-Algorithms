import unittest
from collections import deque
from challenge02 import TreeNode, is_same_tree

class TestSameTree(unittest.TestCase):
    def setUp(self):
        # Helper function to create a binary tree from a list representation
        def build_tree(nodes):
            if not nodes:
                return None
            root = TreeNode(nodes[0])
            queue = deque([root])
            index = 1
            while index < len(nodes):
                node = queue.popleft()
                if nodes[index] is not None:
                    node.left = TreeNode(nodes[index])
                    queue.append(node.left)
                index += 1
                if index < len(nodes) and nodes[index] is not None:
                    node.right = TreeNode(nodes[index])
                    queue.append(node.right)
                index += 1
            return root
        
        # Example trees for testing
        self.tree1 = build_tree([1, 2, 3])
        self.tree2 = build_tree([1, 2, 3])
        self.tree3 = build_tree([1, 2, None])
        self.tree4 = build_tree([1, None, 2])
        self.tree5 = build_tree([1, 2, 1])
        self.tree6 = build_tree([1, 1, 2])

    def test_same_trees(self):
        self.assertTrue(is_same_tree(self.tree1, self.tree2))

    def test_different_structures(self):
        self.assertFalse(is_same_tree(self.tree1, self.tree3))
        self.assertFalse(is_same_tree(self.tree1, self.tree4))

    def test_different_values(self):
        self.assertFalse(is_same_tree(self.tree5, self.tree6))

    def test_empty_trees(self):
        self.assertTrue(is_same_tree(None, None))

    def test_one_tree_empty(self):
        self.assertFalse(is_same_tree(self.tree1, None))
        self.assertFalse(is_same_tree(None, self.tree2))

if __name__ == '__main__':
    unittest.main()
