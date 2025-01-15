"""
Q. You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.

Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.

Example 1:

Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
Output: 4
Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6
Example 2:

Input: n = 2, roads = [[1,0,10]]
Output: 1
Explanation: There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.
"""

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