from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []  # List to store edges connected to this node

    def add_edge(self, edge):
        self.edges.append(edge)

class Edge:
    def __init__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node

class Graph:
    def __init__(self):
        self.nodes = {}  # Dictionary to store nodes by their values

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)
        return self.nodes[value]

    def add_edge(self, from_value, to_value):
        from_node = self.add_node(from_value)
        to_node = self.add_node(to_value)
        edge = Edge(from_node, to_node)
        from_node.add_edge(edge)
        to_node.add_edge(edge)  # For an undirected graph

    def bfs_traverse(self, start_value):
        if start_value not in self.nodes:
            return []

        visited = set()
        queue = deque([self.nodes[start_value]])
        result = []

        while queue:
            node = queue.popleft()
            if node.value not in visited:
                visited.add(node.value)
                result.append(node.value)
                for edge in node.edges:
                    neighbor = edge.to_node if edge.from_node == node else edge.from_node
                    if neighbor.value not in visited:
                        queue.append(neighbor)

        return result

# Example Usage
if __name__ == "__main__":
    # Create a graph instance
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    g.add_edge('C', 'G')
    g.add_edge('D', 'H')
    g.add_edge('E', 'I')
    g.add_edge('F', 'J')
    g.add_edge('G', 'K')

    # Perform BFS traversal starting from node 'A'
    result = g.bfs_traverse('A')
    print(result)
