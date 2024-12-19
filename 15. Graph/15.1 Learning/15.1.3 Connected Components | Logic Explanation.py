"""
Q. Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
"""


def BFS(n, edges, visited, start):
    queue = [start]
    visited[start] = 1

    while queue:
        curr = queue.pop(0)
        neighbours = edges[curr] if len(edges) > curr else []

        for neighbour in neighbours:
            if not visited[neighbour]:
                visited[neighbour] = 1
                queue.append(neighbour)

def countComponents(n , edges):
    """
    Brute Force Approach
    1. form adjacency matrix
    2. irerate over all nodes
    3. do BFS and mark nodes as visited
    4. all 1 connected componenet is traversed increase count
    5. do the same for all components
    Time Complexity: O(N) * (O(N) + O(2E))
    Space Complexity: 2N + 2E
    """
    adj = [[]*n for i in range(n)]
    for i in edges:
        adj[i[0]].append(i[1])
        adj[i[1]].append(i[0])
    print(adj)

    visited = [0]*n
    count = 0

    for node in range(n):
        if not visited[node]:
            BFS(n, adj, visited, node)
            count += 1
    return count

n = 5

edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
print(countComponents(n, edges))
