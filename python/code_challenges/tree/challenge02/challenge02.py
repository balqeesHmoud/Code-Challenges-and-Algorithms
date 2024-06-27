from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    """
    Check if two binary trees are structurally identical and have the same node values using breadth-first traversal.

    Args:
        p (TreeNode): Root node of the first binary tree.
        q (TreeNode): Root node of the second binary tree.

    Returns:
        bool: True if the trees are identical, False otherwise.
    """
    if not p and not q:
        return True
    if not p or not q:
        return False
    
    queue = deque([(p, q)])
    
    while queue:
        node_p, node_q = queue.popleft()
        
        if node_p.val != node_q.val:
            return False
        
        if node_p.left and node_q.left:
            queue.append((node_p.left, node_q.left))
        elif node_p.left or node_q.left:
            return False
        
        if node_p.right and node_q.right:
            queue.append((node_p.right, node_q.right))
        elif node_p.right or node_q.right:
            return False
    
    return True

# Example usage:
if __name__ == "__main__":
    # Example 1: Identical trees
    # Tree 1
    p1 = TreeNode(1)
    p1.left = TreeNode(2)
    p1.right = TreeNode(3)

    # Tree 2 (identical to Tree 1)
    q1 = TreeNode(1)
    q1.left = TreeNode(2)
    q1.right = TreeNode(3)

    result1 = is_same_tree(p1, q1)
    print("Example 1: Trees are identical")
    print("Result:", result1)
    print()

    # Example 2: Non-identical trees
    # Tree 3
    p2 = TreeNode(1)
    p2.left = TreeNode(2)

    # Tree 4 (different structure compared to Tree 3)
    q2 = TreeNode(1)
    q2.right = TreeNode(2)

    result2 = is_same_tree(p2, q2)
    print("Example 2: Trees are not identical")
    print("Result:", result2)
    print()