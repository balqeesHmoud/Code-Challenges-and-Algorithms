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
