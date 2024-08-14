# Write here the code challenge solution

class Node:
    def __init__(self, value=None):
        """
        Initialize a node with a given value.
        """
        self.value = value

    def __str__(self):
        """
        Return the string representation of the node's value.
        """
        return str(self.value)

    def __eq__(self, other):
        """
        Check if two nodes are equal by comparing their values.
        """
        return isinstance(other, Node) and self.value == other.value

    def __hash__(self):
        """
        Return the hash value of the node based on its value.
        """
        return hash(self.value)


class Graph:
    def __init__(self):
        """
        Initialize an empty graph with an adjacency list.
        """
        self.adjacency_list = {}

    def add_vertex(self, value):
        """
        Add a vertex to the graph if it does not already exist.
        
        :param value: The value of the vertex to be added.
        :return: The created vertex.
        """
        vertex = Node(value)
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
        return vertex

    def add_edge(self, vertex1, vertex2):
        """
        Add a directed edge between two vertices.

        :param vertex1: The starting vertex of the edge.
        :param vertex2: The ending vertex of the edge.
        :raises ValueError: If one or both vertices do not exist in the graph.
        """
        if vertex1 not in self.adjacency_list or vertex2 not in self.adjacency_list:
            raise ValueError("One or both vertices do not exist in the graph")
        self.adjacency_list[vertex1].append(vertex2)

    def _dfs(self, start_vertex, visited):
        """
        Perform Depth-First Search (DFS) from the start vertex and mark visited vertices.
        
        :param start_vertex: The starting vertex for the DFS.
        :param visited: A set to keep track of visited vertices.
        """
        stack = [start_vertex]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(self.adjacency_list[vertex])

    def _reverse_graph(self):
        """
        Create and return a reversed version of the graph where all edges are reversed.
        
        :return: A new Graph instance representing the reversed graph.
        """
        reversed_graph = Graph()
        for vertex in self.adjacency_list:
            reversed_graph.add_vertex(vertex.value)
        for vertex, neighbors in self.adjacency_list.items():
            for neighbor in neighbors:
                reversed_graph.add_edge(neighbor, vertex)
        return reversed_graph

    def is_strongly_connected(self):
        """
        Check if the graph is strongly connected by verifying that all vertices are reachable from any starting vertex 
        and also reachable in the reversed graph.

        :return: 'Strongly connected' if the graph is strongly connected, otherwise 'Not strongly connected'.
        """
        if not self.adjacency_list:
            return 'Not strongly connected'
        
        # Start DFS from any vertex (arbitrarily choosing the first one)
        start_vertex = next(iter(self.adjacency_list))
        visited = set()
        self._dfs(start_vertex, visited)
        
        # If not all vertices are visited, the graph is not strongly connected
        if len(visited) != len(self.adjacency_list):
            return 'Not strongly connected'
        
        # Reverse the graph and perform DFS again
        reversed_graph = self._reverse_graph()
        visited_reversed = set()
        reversed_graph._dfs(start_vertex, visited_reversed)
        
        # If not all vertices are visited in the reversed graph, it's not strongly connected
        if len(visited_reversed) != len(reversed_graph.adjacency_list):
            return 'Not strongly connected'
        
        return 'Strongly connected'


def create_graph_from_edges(edges):
    """
    Create a graph from a list of edges.

    :param edges: A list of edge pairs where each pair represents a directed edge.
    :return: A Graph instance constructed from the given edges.
    """
    graph = Graph()
    vertex_map = {}

    for v1, v2 in edges:
        if v1 not in vertex_map:
            vertex_map[v1] = graph.add_vertex(v1)
        if v2 not in vertex_map:
            vertex_map[v2] = graph.add_vertex(v2)
        graph.add_edge(vertex_map[v1], vertex_map[v2])

    return graph


# Example usage

edges1 = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 4], [1, 7], [7, 3]]
graph1 = create_graph_from_edges(edges1)

print("Graph 1 connectivity:", graph1.is_strongly_connected())  # Output: Not strongly connected

edges2 = [[1, 2], [1, 0], [0, 4], [4, 3], [3, 2], [3, 1], [2, 1], [2, 4]]
graph2 = create_graph_from_edges(edges2)

print("Graph 2 connectivity:", graph2.is_strongly_connected())  # Output: Strongly connected
