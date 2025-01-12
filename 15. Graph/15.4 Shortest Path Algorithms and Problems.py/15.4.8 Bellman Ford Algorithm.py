"""
Q. Given a weighted and directed graph of v vertices and edges, Find the shortest distance of all the vertex's from the source vertex, src and return a list of integers where the ith integer denotes the distance of the ith node from the source node. If a vertices can't be reach from the s then mark the distance as 10^8.
Note: If the graph contains a negative cycle then return an array consisting of only -1.

Examples:

Input: edges = [[0,1,9]], src = 0

Output: [0, 9]
Explanation: Shortest distance of all nodes from source is printed.
Input: edges = [[0,1,5], [1,0,3], [1,2,-1], [2,0,1]], src = 2

Output: [1, 6, 0]
Explanation: For nodes 2 to 0, we can follow the path: 2-0. This has a distance of 1. For nodes 2 to 1, we cam follow the path: 2-0-1, which has a distance of 1+5 = 6,
"""


def bellmanFord(V, edges, src):
    """
    BellmanFord Algorithm
    1. work with negative weights
    2. do relaxation if dist[u] + wt < dist[v] then update dist[v]
    3. do this for N-1 to cover all edges
    4. detect cycle seperately if we are still updating dist[v] at n-1 then there is a negative cycle
    Time Complexity: O(V*E)
    Space Complexity: O(V)
    """
    maxx = 10**8
    dist = [maxx] * V
    dist[src] = 0

    for i in range(V):
        for edge in edges:
            u, v, wt = edge
            if dist[u] != maxx and dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt

    # check negative cycle
    for edge in edges:
        u, v, wt = edge
        if dist[u] != maxx and dist[u] + wt < dist[v]:
            return -1
    return dist

V = 7
edges = [[4,5,10], [5,3,1], [1,2,-1], [2,0,1]]
src = 2
print(bellmanFord(V, edges, src))