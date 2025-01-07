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