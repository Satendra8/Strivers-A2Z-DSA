"""
Given a weighted, undirected, and connected graph with V vertices and E edges, your task is to find the sum of the weights of the edges in the Minimum Spanning Tree (MST) of the graph. The graph is represented by an adjacency list, where each element adj[i] is a vector containing vector of integers. Each vector represents an edge, with the first integer denoting the endpoint of the edge and the second integer denoting the weight of the edge.

Input:
3 3
0 1 5
1 2 3
0 2 1

Output: 4
Explanation:

The Spanning Tree resulting in a weight
of 4 is shown above.
Input: 
2 1
0 1 5

Output: 5 

Explanation: Only one Spanning Tree is possible which has a weight of 5.
"""

import heapq

def spanningTree(V, adj):
    """
    Prim's Algorithm
    1. do similar to BFS (mark node as visited at end)
    2. use priority queue, visited array
    3. if node is node visited then only go to other neighbours
    4. priority queue is ensuring to chose path with minimum cost
    5. keep adding the weight
    6. and mark visited at last
    Time Complexity: O(2E) * log(E)
    Space Complexity: O(E)
    """
    ans = 0
    visited = [0]*V
    queue = []
    heapq.heappush(queue, (0, 0, -1))

    while queue:
        wt, v, u = heapq.heappop(queue)
        if not visited[v]:
            neighbours = adj[v]
            for neighbour in neighbours:
                if not visited[neighbour[0]]:
                    heapq.heappush(queue, (neighbour[1], neighbour[0], v))
            if u != -1:
                ans += wt
            visited[v] = 1
    return ans


V = 3
E  = [[0,1,5], [1,2,3] ,[0,2,1]]
print(spanningTree(V, E))
