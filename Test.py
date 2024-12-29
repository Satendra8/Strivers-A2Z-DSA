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