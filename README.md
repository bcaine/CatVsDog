# Spotify Cats vs Dogs Challenge Solution

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

To run:

   cat tests/in1.txt | python catsvsdogs.py