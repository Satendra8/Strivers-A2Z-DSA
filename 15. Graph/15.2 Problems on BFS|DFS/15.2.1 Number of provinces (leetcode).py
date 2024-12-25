"""
Q. There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
"""

def bfs(node, adjMatrix, visited, n):
    queue = [node]
    visited[node] = 1

    while queue:
        row = queue.pop(0)

        for i in range(n):
            isNeighbour = adjMatrix[row][i]
            if not visited[i] and isNeighbour:
                queue.append(i)
                visited[i] = 1


def findCircleNum(isConnected):
    """
    Similar to count number of components
    1. traverse all nodes
    2. use bfs to traverse node
    3. keep counting disconnected components
    Time Complexity: O(V) * O(V+E)
    Space Complexity: O(2V)
    """
    n = len(isConnected)
    visited = [0]*n
    count = 0
    for i in range(n):
        if not visited[i]:
            bfs(i, isConnected, visited, n)
            count += 1
    return count

isConnected = [[1,0,0],[0,1,0],[0,0,1]]
print(findCircleNum(isConnected))