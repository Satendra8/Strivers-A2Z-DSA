def dfs(node, adj, visited, visitedPath, V):
    visited[node] = 1
    visitedPath[node] = 1

    neighbours = adj[node]

    for neighbour in neighbours:
        if not visited[neighbour]:
            if dfs(neighbour, adj, visited, visitedPath, V):
                return True
        else:
            if visitedPath[neighbour]:
                return True
    visitedPath[node] = 0
    return False


def isCyclic(V, adj):
    """
    Use DFS
    1. for cycle on the same path node has to be visited again
    2. maintain a visited path array
    3. use disconnected component to traverse all node
    4. while returning back mark visited path 0
    5. at any moment if cycle found return true
    Time Complexity: O(V+E)
    Space Complexity: O(2N)
    """
    visited = [0]*V
    visitedPath = [0]*V

    for i in range(V):
        if not visited[i]:
            if dfs(i, adj, visited, visitedPath, V):
                return True
    return False



adj = [[1], [2], [3,6], [4], [5], [], [4], [8], [9], []]
V = len(adj)
print(isCyclic(V, adj))