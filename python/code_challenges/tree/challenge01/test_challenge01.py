import pytest
from challenge01 import Tree, levelOrderTraversal

def test_tree_construction_empty():
    '''Test case for handling empty input lists in binary tree construction.'''
    tree = Tree()
    preorder = []
    inorder = []

    tree.root = tree.buildTree(preorder, inorder)
    expected_output = []

    assert levelOrderTraversal(tree.root) == expected_output

def test_tree_construction_large():
    '''Test case for constructing a large binary tree from preorder and inorder traversals.'''
    tree = Tree()
    preorder = [50, 25, 10, 40, 70, 60, 90]
    inorder = [10, 25, 40, 50, 60, 70, 90]

    tree.root = tree.buildTree(preorder, inorder)
    expected_output = [50, 25, 70, 10, 40, 60, 90]

    assert levelOrderTraversal(tree.root) == expected_output

def test_tree_construction_missing_nodes():
    '''Test case for handling missing nodes in binary tree construction.'''
    tree = Tree()
    preorder = [1, 2, 4, 5, 3, 7]
    inorder = [4, 2, 5, 1, 3, 7]

    tree.root = tree.buildTree(preorder, inorder)
    expected_output = [1, 2, 3, 4, 5, None, 7]

    assert levelOrderTraversal(tree.root) == expected_output
    
def test_tree_construction_normal():
    '''Test case for constructing a binary tree from preorder and inorder traversals.'''
    tree = Tree()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    tree.root = tree.buildTree(preorder, inorder)
    expected_output = [3, 9, 20, None, None, 15, 7]

    assert levelOrderTraversal(tree.root) == expected_output

def test_tree_construction_single_node():
    '''Test case for constructing a binary tree with a single node.'''
    tree = Tree()
    preorder = [5]
    inorder = [5]

    tree.root = tree.buildTree(preorder, inorder)
    expected_output = [5]

    assert levelOrderTraversal(tree.root) == expected_output

def test_tree_construction_unbalanced():
    '''Test case for constructing an unbalanced binary tree.'''
    tree = Tree()
    preorder = [1, 2, 3, 4, 5]
    inorder = [5, 4, 3, 2, 1]

    tree.root = tree.buildTree(preorder, inorder)
    expected_output = [1, 2, None, 3, None, 4, None, 5]

    assert levelOrderTraversal(tree.root) == expected_output
