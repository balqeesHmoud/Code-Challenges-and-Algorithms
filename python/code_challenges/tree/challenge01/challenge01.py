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

def levelOrderTraversal(root):
    """
    Performs level-order traversal of the binary tree.

    :param root: The root node of the binary tree.
    :return: List of node values in level-order.
    """
    if not root:
        return []
    
    queue = [root]
    result = []

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.value)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    while result and result[-1] is None:
        result.pop()
    
    return result

# Usage example
if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    tree = Tree()
    root = tree.buildTree(preorder, inorder)
    result = levelOrderTraversal(root)
    print(f'Input: Preorder: {preorder} / Inorder: {inorder} \nOutput: {result}')
