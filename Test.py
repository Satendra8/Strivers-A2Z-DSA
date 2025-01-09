def findAdj(V, edges):
    adj = [[] for _ in range(V)]
    for i in range(V):
        for item in edges:
            u, v, dist = item
            if i == u:
                adj[i].append((v, dist))
    return adj


def dfs(node, adj, visited, ans):
    visited[node] = 1
    neighbours = adj[node]
    for neighbour in neighbours:
        if not visited[neighbour[0]]:
            dfs(neighbour[0], adj, visited, ans)
    ans.append(node)


def topological(V, adj):
    visited = [0]*V
    ans = []
    for i in range(V):
        if not visited[i]:
            dfs(i, adj, visited, ans)
    return ans


def shortestPath(V, E, edges):
    """
    1. find the adjucency matrix
    2. Do topological sort on the graph (use DFS)
    3. pop from stack (topological)
    4. add curr_dist and dist to reach node
    5. if new dist is less than dist array then update
    Time Complexity: O(V+E)
    Space Complexity: O(V+E)
    """
    adj = findAdj(V, edges)
    topo = topological(V ,adj)
    
    dist = [float('inf')] * V
    dist[0] = 0
    while topo:
        curr = topo.pop()
        curr_dist = dist[curr]
        neighbours = adj[curr]

        for neighbour in neighbours:
            elem, cost = neighbour
            if dist[elem] > curr_dist + cost:
                dist[elem] = curr_dist + cost
    
    for i in range(V):
        if dist[i] == float('inf'):
            dist[i] = -1
    return dist


V = 4
E = 2
edges = [[0,1,2], [0,2,1]]
print(shortestPath(V, E, edges))