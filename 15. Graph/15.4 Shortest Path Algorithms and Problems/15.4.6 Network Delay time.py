"""
Q. You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
"""

import heapq
def getAdj(times, n):
    adj = {i: [] for i in range(1, n+1)}

    for i in range(1, n+1):
        for item in times:
            u, v, w = item
            if i == u:
                adj[i].append((v, w))
    return adj

def networkDelayTime(times, n, k):
    """
    Dijkstra Algorithm
    1. calculate adj matrix
    2. initialize distance array with infinite
    3. initialize queue with k
    4. go to all neighbours if lesser time found update in queue and dist
    5. if any node in dist found infinite return -1
    6. retun max of dist array
    Time Complexity: n * len(times)
    Space Complexity: n
    """
    adj = getAdj(times, n)
    dist = [float('inf')] * (n+1)
    dist[k] = 0
    queue = []
    heapq.heappush(queue, (k,0))

    while queue:
        u, w = heapq.heappop(queue)
        neighbours = adj[u]
        for neighbour in neighbours:
            v, new_weight = neighbour
            if dist[v] > w + new_weight:
                dist[v] = w + new_weight
                heapq.heappush(queue, (v, w+new_weight))
    max_dist = -1
    for i in range(1, n+1):
        if dist[i] == float('inf'):
            return -1
        max_dist = max(max_dist, dist[i])
    return max_dist


times = [[1,2,1]]
n = 2
k = 2
print(networkDelayTime(times, n, k))