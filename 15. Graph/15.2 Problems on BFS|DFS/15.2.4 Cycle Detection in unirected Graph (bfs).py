def detectCycle(adj, i, visited):
    queue = [(i, -1)]
    visited[i] = 1

    while queue:
        node, prev = queue.pop(0)

        neighbours = adj[node]
        for neighbour in neighbours:
            if neighbour != prev:
                if visited[neighbour] == 1:
                    return 1
                queue.append((neighbour, node))
                visited[neighbour] = 1
    return 0


def isCycle(V, adj):
    """
    Use BFS
    1. If collision found while traversing the cycle exist
    2. use queue to store curr node with its prev node
    3. keep track of visited array
    4. if an already visited node found then cycle exist (check also if curr node != prev)
    5. Edge case: if graph is broken down into multiple parts
    6. apply multiple component traversal in this case
    Time Complexity: O(N) * O(V+2E)
    Space Complexity: O(2V)
    """
    visited = [0]*V
    for i in range(V):
        if not visited[i]:
            if detectCycle(adj, i, visited) == 1:
                return 1
    return 0


adj = [[1], [0,2,4], [1,3], [2,4], [1,3]]
V = len(adj)
print(isCycle(V, adj))