class Node:
    def __init__(self, value=0, left=None, right=None):
        """
        Initializes a binary tree node.

        :param value: The value of the node.
        :param left: The left child node.
        :param right: The right child node.
        """
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def buildTree(self, preorder, inorder):
        """
        Constructs a binary tree from preorder and inorder traversal arrays.

        :param preorder: List of integers representing preorder traversal.
        :param inorder: List of integers representing inorder traversal.
        :return: The root node of the constructed binary tree.
        """
        def helper(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            
            # The first element in preorder is the root node
            root_value = preorder[pre_left]
            root = Node(root_value)
            
            # Root index in inorder array
            in_root_index = inorder_index_map[root_value]
            
            # Number of elements in the left subtree
            left_subtree_size = in_root_index - in_left
            
            # Recursively construct the left and right subtree
            root.left = helper(pre_left + 1, pre_left + left_subtree_size, in_left, in_root_index - 1)
            root.right = helper(pre_left + left_subtree_size + 1, pre_right, in_root_index + 1, in_right)
            
            return root
        
        # Build a hashmap to store value -> its index relations for inorder traversal
        inorder_index_map = {value: index for index, value in enumerate(inorder)}
        
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)

class Main:
    def run_tests(self):
        """
        Runs the tree construction tests and prints the results.
        """
        # Example 1
        preorder1 = [3, 9, 20, 15, 7]
        inorder1 = [9, 3, 15, 20, 7]
        expected_output1 = [3, 9, 20, None, None, 15, 7]
        root1 = Tree().buildTree(preorder1, inorder1)
        result1 = self.treeToList(root1)
        print("Example 1:")
        self.print_comparison(result1, expected_output1)
        print()

        # Example 2
        preorder2 = [-1]
        inorder2 = [-1]
        expected_output2 = [-1]
        root2 = Tree().buildTree(preorder2, inorder2)
        result2 = self.treeToList(root2)
        print("Example 2:")
        self.print_comparison(result2, expected_output2)
        print()

        # Test empty tree
        preorder3 = []
        inorder3 = []
        expected_output3 = []
        root3 = Tree().buildTree(preorder3, inorder3)
        result3 = self.treeToList(root3)
        print("Empty Tree Test:")
        self.print_comparison(result3, expected_output3)
        print()

        # Test single node tree
        preorder4 = [1]
        inorder4 = [1]
        expected_output4 = [1]
        root4 = Tree().buildTree(preorder4, inorder4)
        result4 = self.treeToList(root4)
        print("Single Node Tree Test:")
        self.print_comparison(result4, expected_output4)
        print()

        # Test complex tree
        preorder5 = [1, 2, 4, 5, 3, 6, 7]
        inorder5 = [4, 2, 5, 1, 6, 3, 7]
        expected_output5 = [1, 2, 3, 4, 5, 6, 7]
        root5 = Tree().buildTree(preorder5, inorder5)
        result5 = self.treeToList(root5)
        print("Complex Tree Test:")
        self.print_comparison(result5, expected_output5)
        print()

    def treeToList(self, root):
        """
        Converts a binary tree to a list for easy comparison.

        :param root: The root node of the binary tree.
        :return: List representation of the binary tree.
        """
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.value)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        # Trim trailing None values
        while result and result[-1] is None:
            result.pop()

        return result

    def print_comparison(self, result, expected):
        """
        Prints the comparison between result and expected output.

        :param result: The actual result from the treeToList method.
        :param expected: The expected output.
        """
        print("Expected:", expected)
        print("Result:", result)
        if result == expected:
            print("Pass")
        else:
            print("Fail")

if __name__ == "__main__":
    main = Main()
    main.run_tests()
