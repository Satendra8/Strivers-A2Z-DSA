"""
Q. Given an adjacency list for a Directed Acyclic Graph (DAG) where adj[u] contains a list of all vertices v such that there exists a directed edge u -> v. Return topological sort for the given graph.

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u -> v, vertex u comes before v in the ordering.
Note: As there are multiple Topological orders possible, you may return any of them. If your returned Topological sort is correct then the output will be 1 else 0.

Examples:

Input: adj = [[], [0], [0], [0]] 

Output: 1
Explanation: The output 1 denotes that the order is valid. Few valid Topological orders for the given graph are:
[3, 2, 1, 0]
[1, 2, 3, 0]
[2, 3, 1, 0]
Input: adj = [[], [3], [3], [], [0,1], [0,2]]

Output: 1
Explanation: The output 1 denotes that the order is valid. Few valid Topological orders for the graph are:
[4, 5, 0, 1, 2, 3]
[5, 2, 4, 0, 1, 3]
"""

def dfs(node, adj, visited, ans):
    visited[node] = 1
    neighbours = adj[node]

    for neighbour in neighbours:
        if not visited[neighbour]:
            dfs(neighbour, adj, visited, ans)
    ans.append(node)


def topologicalSort(adj):
    """
    DFS
    1. whenever dfs for a node is done while returning put that in stack
    2. run loop for all components
    3. run normal dfs, while returning from a node put that node in stack
    Time Complexity: O(V+E)
    Space Complexity: 2V
    """
    n = len(adj)
    visited = [0]*n
    ans = []
    for i in range(n):
        if not visited[i]:
            dfs(i, adj, visited, ans)
    return ans[::-1]


adj = [[], [0], [0], [0]]
print(topologicalSort(adj))