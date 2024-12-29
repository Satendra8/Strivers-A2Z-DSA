"""
Q. There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

Example 1:


Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
Example 2:


Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
"""

def dfs(node, adj, visited, n):
    neighbours = adj[node]

    for neighbour in neighbours:
        if visited[neighbour] == -1:
            visited[neighbour] = not visited[node]
            if not dfs(neighbour, adj, visited, n):
                return False
        else:
            if visited[neighbour] != (not visited[node]):
                return False
    return True

def isBipartite(graph):
    """
    Use DFS
    1. If 2 adjacent node has same color then not bipertite
    2. use a visited array and save color as 0 and 1
    3. run DFS if a node is already visited and this time its color is different then return false
    4. handle disconnected components
    Time Complexity: O(V+2E)
    Space Complexity: O(V)
    """
    n = len(graph)
    visited = [-1]*n

    for i in range(n):
        if visited[i] == -1:
            visited[i] = 0
            if not dfs(i, graph, visited, n):
                return False
    return True

graph = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
print(isBipartite(graph))