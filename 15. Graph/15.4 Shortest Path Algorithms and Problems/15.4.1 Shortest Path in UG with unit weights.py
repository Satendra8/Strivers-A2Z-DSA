"""
Q. You are given an adjacency matrix, adj of Undirected Graph having unit weight of the edges, find the shortest path from src to all the vertex and if it is unreachable to reach any vertex, then return -1 for that vertex.

Examples :

Input: adj[][] = [[1, 3], [0, 2], [1, 6], [0, 4], [3, 5], [4, 6], [2, 5, 7, 8], [6, 8], [7, 6]], src=0
Output: 0 1 2 1 2 3 3 4 4

Input: adj[][]= [[3], [3], [0, 1]], src=3
Output: 1 1 -1 0

Input: adj[][]= [[], [], [], [4], [3], [], []], src=1
Output: -1 0 -1 -1 -1 -1 -1 
"""

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