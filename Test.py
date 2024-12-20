def dfs(node, adj, visited, ans):
    neighbours = adj[node]

    for neighbour in neighbours:
        if not visited[neighbour]:
            ans.append(neighbour)
            visited[neighbour] = 1
            dfs(neighbour, adj, visited, ans)
    

def dfsOfGraph(adj):
    """
    1. find all neighbours nodes and recusively call function for all
    2. keep marking them visited
    3. keep adding visited node in ans
    Time Complexity: O(V+E)
    Space Complexity: O(2V)
    """
    n = len(adj)
    visited = [0]*n
    visited[0] = 1
    ans = [0]
    dfs(0, adj, visited, ans)
    return ans


adj = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
print(dfsOfGraph(adj))
