"""
Q. Given a weighted, undirected and connected graph where you have given adjacency list adj. You have to find the shortest distance of all the vertices from the source vertex src, and return a list of integers denoting the shortest distance between each node and source vertex src.

Note: The Graph doesn't contain any negative weight edge.

Examples:

Input: adj = [[[1, 9]], [[0, 9]]], src = 0
Output: [0, 9]
Explanation:

The source vertex is 0. Hence, the shortest distance of node 0 is 0 and the shortest distance from node 0 to 1 is 9.
Input: adj = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]], src = 2
Output: [4, 3, 0]
Explanation:

For nodes 2 to 0, we can follow the path 2-1-0. This has a distance of 1+3 = 4, whereas the path 2-0 has a distance of 6. So, the Shortest path from 2 to 0 is 4.
The shortest distance from 0 to 1 is 1 .
"""

def dijkstra(adj, src):
    """
    Dijkstra Algorithm
    1. use normal queue and add src and 0 initially
    2. use a distance array initialize with infinite
    3. find neighbours, if any one is less than curr dist update in dist array
    Time Complexity: O(V+E)
    Space Complexity: O(N) + O(N)
    """
    n = len(adj)
    dist = [float('inf')] * n
    dist[src] = 0
    queue = [(src, 0)]

    while queue:
        curr, d = queue.pop(0)
        neighbours = adj[curr]
        for neighbour in neighbours:
            elem, cost = neighbour
            if dist[elem] > d + cost:
                dist[elem] = d + cost
                queue.append((elem, d + cost))
    return dist


adj = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]]
src = 2
print(dijkstra(adj, src))