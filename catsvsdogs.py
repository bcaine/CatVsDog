#!/usr/bin/env python

__author__ = "Ben Caine"
__email__ = "Bcaine0@gmail.com"
__date__ = "1/22/2016"


import networkx as nx
from networkx.algorithms import bipartite

from 


class CatsVsDogs(object):


    def __init__(self, data):
        self.graph = nx.Graph()
        self.c, self.d, self.v = instance['header']
        self.votes = instance['votes']

        assert(self.c >= 1 and self.c < 100)
        assert(self.d >= 1 and self.d < 100)
        assert(self.v >= 0 and self.v < 500)
    
        
    
    def _conflict(self, n1, n2):
        vote1 = self.graph.node[n1]['votes']
        vote2 = self.graph.node[n2]['votes']
        # Check if what vote1 loves is what
        # vote2 hates, or vise versa
        if vote1[0] == vote2[1]:
            return True
        if vote1[1] == vote2[0]:
            return True
        return False

    def _remove_duplicates(self, matching):
        sorted_matches = [sorted(m) for m in matching.items()]
        
        deduped = {}
        for match in sorted_matches:
            k, v = match
            deduped[k] = v
        return deduped

    def max_satisfied_voters(self):
        if self.v == 0: return 0

        # Construct bipartite graph
        for i, vote in enumerate(self.votes):
            loves_val = 'cat' if 'C' in vote[0] else 'dog'
            self.graph.add_node(i, loves=loves_val, votes=vote)
        
        # Create edges for each conflict
        for n1 in self.graph.nodes():
            for n2 in self.graph.nodes():
                if n1 == n2:
                    continue
            
                if self._conflict(n1, n2):
                    self.graph.add_edge(n1, n2)
                
        matching = bipartite.maximum_matching(graph)
        matching = self._remove_duplicates(matching)
    
        return self.v - len(matching)



print max_satisfied_voters(data[instance])


if __name__=="__main__":
    data = format_input(in1)

