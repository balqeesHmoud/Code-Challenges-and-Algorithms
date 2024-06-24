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
    def run(self):
        """
        Runs the tree construction examples and prints the results.
        """
        # Example 1
        preorder1 = [3, 9, 20, 15, 7]
        inorder1 = [9, 3, 15, 20, 7]
        tree1 = Tree()
        root1 = tree1.buildTree(preorder1, inorder1)
        print("Example 1:")
        self.printTree(root1)
        
        # Example 2
        preorder2 = [-1]
        inorder2 = [-1]
        tree2 = Tree()
        root2 = tree2.buildTree(preorder2, inorder2)
        print("Example 2:")
        self.printTree(root2)

    def treeToList(self, root):
        """
        Converts a binary tree to a list for easy comparison in tests.

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
        
        # Trim the trailing None values
        while result and result[-1] is None:
            result.pop()
        
        return result
    
    def printTree(self, root):
        """
        Prints the binary tree in a level order format.

        :param root: The root node of the binary tree.
        """
        if not root:
            print("Tree is empty")
            return
        
        result = []
        queue = [root]
        
        while queue:
            level_size = len(queue)
            level_nodes = []
            for _ in range(level_size):
                node = queue.pop(0)
                if node:
                    level_nodes.append(node.value)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    level_nodes.append(None)
            result.append(level_nodes)
        
        for level in result:
            print(level)

# Running the solution
if __name__ == "__main__":
    main = Main()
    main.run()
