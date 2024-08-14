# Write your test here
import pytest
from challenge03 import Graph

@pytest.fixture
def create_graph():
    """
    Fixture to create a Graph instance from a list of edges.
    
    :return: A function that creates and returns a Graph instance given a list of edges.
    """
    def _create_graph(edges):
        graph = Graph()
        vertex_map = {}
        
        for v1, v2 in edges:
            if v1 not in vertex_map:
                vertex_map[v1] = graph.add_vertex(v1)
            if v2 not in vertex_map:
                vertex_map[v2] = graph.add_vertex(v2)
            graph.add_connection(vertex_map[v1], vertex_map[v2])
        
        return graph
    return _create_graph

def test_graph_connectivity(create_graph):
    """
    Test the connectivity of various graph instances.

    :param create_graph: Fixture function to create a Graph instance from edges.
    """
    test_cases = {
        'test_case_1': ([[1,2],[2,3],[3,4],[4,5],[5,6],[6,4],[1,7],[7,3]], 'Not strongly connected'),
        'test_case_2': ([[1,2],[1,0],[0,4],[4,3],[3,2],[3,1],[2,1],[2,4]], 'Strongly connected'),
        'test_case_3': ([[1,2],[2,3],[3,1]], 'Strongly connected'),
        'test_case_4': ([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,1]], 'Strongly connected'),
        'test_case_5': ([[1,2],[2,3],[3,4],[4,2]], 'Not strongly connected'),
        'test_case_6': ([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8]], 'Not strongly connected')
    }
    
    for case_name, (edges, expected_result) in test_cases.items():
        graph = create_graph(edges)
        result = graph.is_fully_connected()
        assert result == expected_result, f"Failed for {case_name}. Expected: {expected_result}, Got: {result}"