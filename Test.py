import heapq
def getAdj(n, roads):
    adj = {i: [] for i in range(n)}

    for road in roads:
        u, v, cost = road
        adj[u].append((v, cost))
        adj[v].append((u, cost))
    return adj

def countPaths(n, roads):
    """
    Dijkstra Algorithm
    1. convert into adj array (it is indirected graph so consider two way)
    2. take a queue, a dist array and a ways array to track the ways
    3. if minimum dist found at a node v, include all the ways that comes at u
    4. if equal dist found add the ways of u and v node
    5. return the last ways[n-1]
    Time Complexity: O(2E) * log(V) (for priority queue)
    Space Complexity: O(V+2E)
    """
    MOD = 10**9 + 7
    adj = getAdj(n, roads)
    print(adj)
    queue = []
    heapq.heappush(queue, (0,0))
    dist = [float('inf')] * n
    dist[0] = 0
    ways = [0] * n
    ways[0] = 1

    while queue:
        cost, curr = heapq.heappop(queue)
        neighbours = adj[curr]
        for neighbour in neighbours:
            v, new_cost = neighbour
            if dist[v] > cost+new_cost:
                heapq.heappush(queue, (cost+new_cost, v))
                dist[v] = cost+new_cost
                ways[v] = ways[curr]%MOD
            elif dist[v] == cost+new_cost:
                ways[v] = (ways[v] + ways[curr])%MOD
    return ways[n-1]%MOD

n = 7
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]

print(countPaths(n, roads))