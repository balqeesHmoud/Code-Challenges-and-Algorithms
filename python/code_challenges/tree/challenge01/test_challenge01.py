import unittest
from challenge01 import Tree, Main

class TestTreeConstruction(unittest.TestCase):
    def setUp(self):
        """
        Sets up the test cases.
        """
        self.tree = Tree()

    def test_example_1(self):
        """
        Tests tree construction with the first example.
        """
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        expected_output = [3, 9, 20, None, None, 15, 7]
        root = self.tree.buildTree(preorder, inorder)
        result = Main().treeToList(root)
        self.assertEqual(result, expected_output)

    def test_example_2(self):
        """
        Tests tree construction with the second example.
        """
        preorder = [-1]
        inorder = [-1]
        expected_output = [-1]
        root = self.tree.buildTree(preorder, inorder)
        result = Main().treeToList(root)
        self.assertEqual(result, expected_output)

    def test_empty_tree(self):
        """
        Tests tree construction with empty inputs.
        """
        preorder = []
        inorder = []
        expected_output = []
        root = self.tree.buildTree(preorder, inorder)
        result = Main().treeToList(root)
        self.assertEqual(result, expected_output)

    def test_single_node_tree(self):
        """
        Tests tree construction with a single node.
        """
        preorder = [1]
        inorder = [1]
        expected_output = [1]
        root = self.tree.buildTree(preorder, inorder)
        result = Main().treeToList(root)
        self.assertEqual(result, expected_output)

    def test_complex_tree(self):
        """
        Tests tree construction with a more complex example.
        """
        preorder = [1, 2, 4, 5, 3, 6, 7]
        inorder = [4, 2, 5, 1, 6, 3, 7]
        expected_output = [1, 2, 3, 4, 5, 6, 7]
        root = self.tree.buildTree(preorder, inorder)
        result = Main().treeToList(root)
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()

