def shortestPath(adj, src):
    """
    BFS
    1. use queue and keep track of node and distance
    2. initialize distance as infinite
    3. for any node if smaller distance found update and push in queue
    4. in the last if any distance found to be infinite then update it with -1
    Time Complexity: O(V+2E)
    Space Complexity: O(V)
    """
    n = len(adj)
    queue = [(src, 0)]
    distance = [float('inf')]*n
    distance[src] = 0
    
    while queue:
        curr, dist = queue.pop(0)
        neighbours = adj[curr]

        for neighbour in neighbours:
            if distance[neighbour] > dist + 1:
                queue.append((neighbour, dist+1))
                distance[neighbour] = dist + 1
    for i in range(n):
        if distance[i] == float('inf'):
            distance[i] = -1
    return distance

adj = [[], [], [], [4], [3], [], []]
src=1
print(shortestPath(adj, src))