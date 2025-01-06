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