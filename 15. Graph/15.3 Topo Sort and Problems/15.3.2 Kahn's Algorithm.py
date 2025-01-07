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

def getIndegree(adj, n):
    indegree = [0]*n
    for i in range(n):
        for node in adj[i]:
            indegree[node] += 1
    return indegree


def dfs(adj):
    """
    BFS
    1. Kahn's Algorithm
    2. find indegree, insert all nodes with indegree 0 in queue
    3. take them off from the queue, and reduce the indegree
    4. if indegree becomes 0 push that node in queue
    Time Complextiy: O(V+E)
    Space Complexity: O(V)
    """
    n = len(adj)
    indegree = getIndegree(adj, n)
    queue = []

    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
    topo = []

    while queue:
        curr = queue.pop(0)
        topo.append(curr)

        for neighbour in adj[curr]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)
    return topo


adj = [[], [3], [3], [], [0,1], [0,2]]
print(dfs(adj))