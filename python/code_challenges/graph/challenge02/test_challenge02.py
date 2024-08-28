import unittest
from collections import deque

# Assuming the classes Node, Edge, and Graph are in a module named graph_module
from challenge02 import *

class TestGraph(unittest.TestCase):

    def setUp(self):
        # Create a new graph instance for each test
        self.graph = Graph()
        # Set up a sample graph
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('A', 'C')
        self.graph.add_edge('B', 'D')
        self.graph.add_edge('B', 'E')
        self.graph.add_edge('C', 'F')
        self.graph.add_edge('C', 'G')
        self.graph.add_edge('D', 'H')
        self.graph.add_edge('E', 'I')
        self.graph.add_edge('F', 'J')
        self.graph.add_edge('G', 'K')

    def test_bfs_traverse(self):
        # Expected BFS traversal order from node 'A'
        expected_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
        result = self.graph.bfs_traverse('A')
        self.assertEqual(result, expected_order)

    def test_bfs_traverse_node_not_in_graph(self):
        # Test BFS traversal from a node not in the graph
        result = self.graph.bfs_traverse('Z')
        self.assertEqual(result, [])

    def test_add_edge_creates_nodes(self):
        # Test that adding an edge creates nodes if they do not exist
        self.graph.add_edge('X', 'Y')
        self.assertIn('X', self.graph.nodes)
        self.assertIn('Y', self.graph.nodes)

    def test_add_edge_adds_edges(self):
        # Test that adding an edge updates nodes' edges list
        node_x = self.graph.add_node('X')
        node_y = self.graph.add_node('Y')
        self.graph.add_edge('X', 'Y')
        self.assertTrue(any(edge.to_node == node_y for edge in node_x.edges))
        self.assertTrue(any(edge.from_node == node_x for edge in node_y.edges))

if __name__ == '__main__':
    unittest.main()
