"""
Q. Given a Directed Acyclic Graph of V vertices from 0 to n-1 and a 2D Integer array(or vector) edges[ ][ ] of length E, where there is a directed edge from edge[i][0] to edge[i][1] with a distance of edge[i][2] for all i.

Find the shortest path from src(0) vertex to all the vertices and if it is impossible to reach any vertex, then return -1 for that vertex.

Examples :

Input: V = 4, E = 2, edges = [[0,1,2], [0,2,1]]
Output: [0, 2, 1, -1]
Explanation: Shortest path from 0 to 1 is 0->1 with edge weight 2. Shortest path from 0 to 2 is 0->2 with edge weight 1. There is no way we can reach 3, so it's -1 for 3.
Input: V = 6, E = 7, edges = [[0,1,2], [0,4,1], [4,5,4], [4,2,2], [1,2,3], [2,3,6], [5,3,1]]
Output: [0, 2, 3, 6, 1, 5]
Explanation: Shortest path from 0 to 1 is 0->1 with edge weight 2. Shortest path from 0 to 2 is 0->4->2 with edge weight 1+2=3. Shortest path from 0 to 3 is 0->4->5->3 with edge weight 1+4+1=6. Shortest path from 0 to 4 is 0->4 with edge weight 1.Shortest path from 0 to 5 is 0->4->5 with edge weight 1+4=5.
"""

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