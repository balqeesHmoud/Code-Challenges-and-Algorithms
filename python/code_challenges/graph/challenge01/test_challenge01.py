# Write your test here
import pytest
from challenge01 import Node, Edge, Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        """
        Set up a graph for testing.
        """
        self.graph = Graph()
        self.node1 = self.graph.add_node("Node1")
        self.node2 = self.graph.add_node("Node2")
        self.node3 = self.graph.add_node("Node3")
        self.node4 = self.graph.add_node("Node4")
        self.node5 = self.graph.add_node("Node5")
        self.node6 = self.graph.add_node("Node6")
        self.node7 = self.graph.add_node("Node7")
        self.node8 = self.graph.add_node("Node8")
        self.node9 = self.graph.add_node("Node9")
        self.node10 = self.graph.add_node("Node10")
        self.graph.add_edge(self.node1, self.node2)
        self.graph.add_edge(self.node1, self.node3)
        self.graph.add_edge(self.node1, self.node5)
        self.graph.add_edge(self.node2, self.node4)
        self.graph.add_edge(self.node3, self.node6)
        self.graph.add_edge(self.node4, self.node5)
        self.graph.add_edge(self.node5, self.node6)
        self.graph.add_edge(self.node5, self.node7)
        self.graph.add_edge(self.node6, self.node8)
        self.graph.add_edge(self.node6, self.node9)
        self.graph.add_edge(self.node7, self.node8)
        self.graph.add_edge(self.node8, self.node10)
        self.graph.add_edge(self.node9, self.node10)

    def test_add_node(self):
        """
        Test adding nodes to the graph.
        """
        new_node = self.graph.add_node("NewNode")
        self.assertIn(new_node, self.graph.adj_list)
        self.assertEqual(new_node.value, "NewNode")

    def test_add_edge(self):
        """
        Test adding edges to the graph.
        """
        new_node1 = self.graph.add_node("NewNode1")
        new_node2 = self.graph.add_node("NewNode2")
        self.graph.add_edge(new_node1, new_node2)
        self.assertEqual(len(self.graph.adj_list[new_node1]), 1)
        self.assertEqual(len(self.graph.adj_list[new_node2]), 1)
        self.assertEqual(str(self.graph.adj_list[new_node1][0]), "NewNode2")
        self.assertEqual(str(self.graph.adj_list[new_node2][0]), "NewNode1")

    def test_breadth_first(self):
        """
        Test breadth-first traversal of the graph.
        """
        bfs_result = self.graph.breadth_first("Node1")
        expected_result = ['Node1', 'Node2', 'Node3', 'Node5', 'Node4', 'Node6', 'Node7', 'Node8', 'Node9', 'Node10']
        self.assertEqual(bfs_result, expected_result)

        bfs_result_non_existent = self.graph.breadth_first("NonExistent")
        self.assertEqual(bfs_result_non_existent, "Node with value 'NonExistent' does not exist in the graph.")

    def test_graph_structure(self):
        """
        Test the string representation of the graph.
        """
        expected_output = (
            "Graph Structure:\n"
            "Node1: Node2 -> Node3 -> Node5\n"
            "Node2: Node1 -> Node4\n"
            "Node3: Node1 -> Node6\n"
            "Node4: Node2 -> Node5\n"
            "Node5: Node1 -> Node4 -> Node6 -> Node7\n"
            "Node6: Node3 -> Node5 -> Node8 -> Node9\n"
            "Node7: Node5 -> Node8\n"
            "Node8: Node6 -> Node7 -> Node10\n"
            "Node9: Node6 -> Node10\n"
            "Node10: Node8 -> Node9\n"
        )
        self.assertEqual(str(self.graph), expected_output)

if __name__ == '__main__':
    unittest.main()