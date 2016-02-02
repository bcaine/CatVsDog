#!/usr/bin/env python
"""
Solution to Spotify's catsvsdogs puzzle:
https://labs.spotify.com/puzzles/

This solution uses networkx to make dealing with graphs cleaner, and provides
functions for finding the maximum bipartite matching using the Hopcroft Karp
matching algorithm.

We create a bipartite graph where each node is a vote and each edge is a
conflict.

We then use maximum bipartite matching to find the maximum number of edges
we can with none of these edges sharing an endpoint. This number of edges
tells us the number of nodes we would have to remove to seperate the graph,
therefore satisfying the remaining voters (nodes).

The total_number_of_votes - len(max_matching) gives us the max number of
satisfied voters.
"""

__author__ = "Ben Caine"
__email__ = "Bcaine0@gmail.com"
__date__ = "1/22/2016"


import sys
from graph import Graph
from input_helpers import read_stdin, format_input


class CatsVsDogs(object):

    def __init__(self, instance):
        """ Create the graph and seperate out the data"""
        self.graph = Graph()
        self.c, self.d, self.v = instance['header']
        self.votes = instance['votes']

        assert self.c >= 1 and self.c < 100
        assert self.d >= 1 and self.d < 100
        assert self.v >= 0 and self.v < 500

    def _conflict(self, node_1, node_2):
        """Returns whether or not there is a conflict between two nodes"""
        vote1 = self.graph.node[node_1]['votes']
        vote2 = self.graph.node[node_2]['votes']
        # Check if what vote1 loves is what
        # vote2 hates, or vise versa
        if vote1[0] == vote2[1]:
            return True
        if vote1[1] == vote2[0]:
            return True
        return False

    # TODO: Potentially remove
    def _remove_duplicates(self, matching):
        """Removes duplicates from a matching"""
        # Sort the individual tuples so (1, 4) and (4, 1) are
        # now both (1, 4), which makes deduping easy
        sorted_matches = [sorted(m) for m in matching.items()]
        deduped = {}
        for match in sorted_matches:
            key, val = match
            deduped[key] = val
        return deduped

    def max_satisfied_voters(self):
        """Calculates the maximum number of satisfied voters of an instance"""
        if self.v == 0:
            return 0

        # Construct bipartite graph
        for i, vote in enumerate(self.votes):
            loves_val = 'cat' if 'C' in vote[0] else 'dog'
            self.graph.add_node(i, loves=loves_val, votes=vote)

        # Create edges for each conflict
        for u in self.graph.nodes():
            for v in self.graph.nodes():
                if u == v:
                    continue

                if self._conflict(u, v):
                    self.graph.add_edge(u, v)

        matching = self.graph.maximum_matching('loves')

        return self.v - len(matching)


if __name__ == "__main__":
    # Read data from stdin
    input_text = read_stdin()
    data = format_input(input_text)

    for inst in data:
        cats_vs_dogs = CatsVsDogs(inst)
        print cats_vs_dogs.max_satisfied_voters()
        # print cats_vs_dogs.graph.nodes(data=True)
        # print cats_vs_dogs.graph.edges(data=True)
