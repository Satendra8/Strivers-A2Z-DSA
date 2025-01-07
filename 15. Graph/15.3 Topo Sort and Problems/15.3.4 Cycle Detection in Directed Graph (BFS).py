"""
Q. Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.
The graph is represented as an adjacency list, where adj[i] contains a list of vertices that are directly reachable from vertex i. Specifically, adj[i][j] represents an edge from vertex i to vertex j.

Example 1:

Input:

Output: 1
Explanation: 3 -> 3 is a cycle
Example 2:
Input:

Output: 0
Explanation: no cycle in the graph
"""

def getIndegree(adj, V):
    indegree = [0]*V
    for i in range(V):
        for node in adj[i]:
            indegree[node] += 1
    return indegree

def isCyclic(V, adj):
    """
    BFS
    1. Use Kahn's Algorithm
    2. if you cannot produce topo sort with N size then that has cycle
    3. use a queue and an indegree array
    4. start with node has 0 indegree
    5. while visiting node reduce degree
    6. if indegree becomes 0 then add again in queue
    Time Complexity: O(V+E)
    Space Complexity: O(V)
    """
    indegree = getIndegree(adj, V)
    queue = []

    for i in range(V):
        if indegree[i] == 0:
            queue.append(i)

    topo = []
    while queue:
        curr = queue.pop(0)
        topo.append(curr)
        neighbours = adj[curr]
        for neighbour in neighbours:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)

    return V != len(topo)


V = 3
adj = [[1], [2], []]
print(isCyclic(V, adj))