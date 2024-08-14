# Write your test here
import unittest
from challenge02 import *

class TestGraph(unittest.TestCase):

    def setUp(self):
        """
        Set up a graph instance and add nodes and edges for testing.
        """
        self.graph = Graph()

        # Create nodes
        self.v1 = self.graph.add_node("A")
        self.v2 = self.graph.add_node("B")
        self.v3 = self.graph.add_node("C")
        self.v4 = self.graph.add_node("D")
        self.v5 = self.graph.add_node("E")
        self.v6 = self.graph.add_node("F")
        self.v7 = self.graph.add_node("G")
        self.v8 = self.graph.add_node("H")
        self.v9 = self.graph.add_node("I")
        self.v10 = self.graph.add_node("K")

        # Add edges
        self.graph.add_edge(self.v1, self.v2)
        self.graph.add_edge(self.v1, self.v3)
        self.graph.add_edge(self.v1, self.v5)
        self.graph.add_edge(self.v2, self.v4)
        self.graph.add_edge(self.v3, self.v6)
        self.graph.add_edge(self.v4, self.v5)
        self.graph.add_edge(self.v5, self.v6)
        self.graph.add_edge(self.v5, self.v7)
        self.graph.add_edge(self.v6, self.v8)
        self.graph.add_edge(self.v6, self.v9)
        self.graph.add_edge(self.v7, self.v8)
        self.graph.add_edge(self.v8, self.v10)
        self.graph.add_edge(self.v9, self.v10)

    def test_add_node(self):
        """
        Test adding a new node to the graph.
        """
        node = self.graph.add_node("Z")
        self.assertIn(node, self.graph.adj_list)
        self.assertEqual(node.value, "Z")

    def test_add_edge(self):
        """
        Test adding an edge between two existing nodes.
        """
        initial_edges = len(self.graph.adj_list[self.v1])
        self.graph.add_edge(self.v1, self.v4)
        final_edges = len(self.graph.adj_list[self.v1])
        self.assertEqual(final_edges, initial_edges + 1)
        self.assertIn(self.v4, [edge.vertex for edge in self.graph.adj_list[self.v1]])

    def test_add_edge_nonexistent_node(self):
        """
        Test adding an edge with a nonexistent node.
        """
        non_existent_node = Node("X")
        result = self.graph.add_edge(self.v1, non_existent_node)
        self.assertEqual(result, "One or both nodes do not exist.")

    def test_breadth_first(self):
        """
        Test breadth-first traversal starting from a specified node.
        """
        expected_result = ["A", "B", "C", "E", "D", "F", "G", "H", "I", "K"]
        bfs_result = self.graph.breadth_first("A")
        self.assertEqual(bfs_result, expected_result)

    def test_breadth_first_nonexistent_node(self):
        """
        Test breadth-first traversal starting from a nonexistent node.
        """
        bfs_result = self.graph.breadth_first("Z")
        self.assertEqual(bfs_result, "Node with value 'Z' does not exist.")

    def test_graph_str(self):
        """
        Test the string representation of the graph.
        """
        graph_str = str(self.graph)
        self.assertTrue("A" in graph_str)
        self.assertTrue("B" in graph_str)
        self.assertTrue("K" in graph_str)
        self.assertTrue("Graph Structure:" in graph_str)
        self.assertTrue("A: B -> C -> E" in graph_str)

if __name__ == '__main__':
    unittest.main()
