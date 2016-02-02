"""
Graph library to help with the Spotify Dog vs Cat challenge. This provides 
very basic functionality to make storing graph data easie and more
intuitive.

While the functionality is very stripped down, it is inspired by NetworkX.
The matching function is based loosely on the Hopcroft Karp implementation in
NetworkX.
"""
import collections


INFINITY = float('inf')


class Graph(object):

    def __init__(self):
        self.node = {}
        self.edge = {}


    def nodes(self, data=False):
        if data:
            return self.node.items()
        else:
            return self.node.keys()

    def edges(self, data=False):
        edge_tuples = [(k, self.edge[k].keys()[0]) for k in self.edge]

        if data:
            edges_with_data = []
            for edg in edge_tuples:
                edges_with_data.append([edg, self.edge[edg[0]][edg[1]]])
            return edges_with_data
        else:
            return edge_tuples

    def add_node(self, key, **kwargs):
        self.node[key] = kwargs

    def add_edge(self, u, v, **kwargs):
        # Add node if not added yet
        for n in [u, v]:
            if n not in self.node:
                self.add_node(n)

        self.edge[u] = {v: kwargs}

    def maximum_matching(self, sep_key):

        left, right = self._bipartite_sets(sep_key)
        left_matches = {v: None for v in left}
        right_matches = {v: None for v in right}

        distances = {}

        return {}

    def _bfs(left, right, left_matches, right_matches, distances):
        """Use Breadth first search to check if """
        queue = collections.deque()
        
        


    def _bipartite_sets(self, sep_key):
        keys = set()
        for n in self.node:
            keys.add(self.node[n][sep_key])

        keys = list(keys)
        assert len(keys) == 2

        left = set([n for n in self.node if self.node[n][sep_key] == keys[0]])
        right = set([n for n in self.node if self.node[n][sep_key] == keys[1]])

        return (left, right)

        

if __name__ == "__main__":
    graph = Graph()

    for n in range(10):
        graph.add_node(n)

    graph.add_edge(0, 2)
    graph.add_edge(1, 5)
    graph.add_edge(2, 0)
    graph.add_edge(3, 5)

    print graph.nodes()
    print graph.nodes(data=True)
    print graph.edges()
    print graph.edges(data=True)
    
