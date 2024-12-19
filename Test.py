def bfsOfGraph(adj):
    """
    BFS Algorithm
    1. use a queue and a visited array
    2. initialize queue and visited array
    3. pop the current node from queue and insert all neighbouring node if not visited already
    4. mark node visited
    Time Complexity: O(N) + O(2E)
    Space Complexity: O(2N) 
    """
    queue = [0]
    nodes = len(adj)
    visited = [0]*(nodes)
    visited[0] = 1
    BFS = [0]

    while queue:
        curr = queue.pop(0)
        neighbours = adj[curr]

        for neighbour in neighbours:
            if not visited[neighbour]:
                BFS.append(neighbour)
                queue.append(neighbour)
                visited[neighbour] = 1
    print(BFS)


adj =  [[2,3,1], [0], [0,4], [0], [2]]
bfsOfGraph(adj)
