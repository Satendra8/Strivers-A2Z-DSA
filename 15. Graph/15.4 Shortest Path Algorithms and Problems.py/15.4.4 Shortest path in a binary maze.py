"""
Q. Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:

Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
"""

def shortestPathBinaryMatrix(grid):
    """
    Dijkstra's Algorithm
    1. take a dist matrix with infinite
    2. statrt with (0,0) and initialize queue with (0,0,1)
    3. move in all 8 directions
    4. if cell is 0 and minimum distance found then update in dist
    5. if last cell is still infinite return -1 otherwise return last cell value
    Time Complexity: O(N*N)
    Space Complexity: O(N*N)
    """
    #edge case
    if grid[0][0] == 1:
        return -1
    n = len(grid)
    dist = [[float('inf')]*n for _ in range(n)]
    dist[0][0] = 1
    queue = [(0, 0, 1)]
    while queue:
        i, j, d = queue.pop(0)

        #left
        if j-1 >= 0 and grid[i][j-1] == 0 and dist[i][j-1] > d+1:
            dist[i][j-1] = d+1
            queue.append((i, j-1, d+1))

        #right
        if j+1 < n and grid[i][j+1] == 0 and dist[i][j+1] > d+1:
            dist[i][j+1] = d+1
            queue.append((i, j+1, d+1))

        #top
        if i-1 >= 0 and grid[i-1][j] == 0 and dist[i-1][j] > d+1:
            dist[i-1][j] = d+1
            queue.append((i-1, j, d+1))

        #bottom
        if i+1 < n and grid[i+1][j] == 0 and dist[i+1][j] > d+1:
            dist[i+1][j] = d+1
            queue.append((i+1, j, d+1))

        #top left
        if i-1 >= 0 and j-1 >= 0 and grid[i-1][j-1] == 0 and dist[i-1][j-1] > d+1:
            dist[i-1][j-1] = d+1
            queue.append((i-1, j-1, d+1))

        #top right
        if i-1 >= 0 and j+1 < n and grid[i-1][j+1] == 0 and dist[i-1][j+1] > d+1:
            dist[i-1][j+1] = d+1
            queue.append((i-1, j+1, d+1))
        
        #bottom left
        if i+1 < n and j-1 >= 0 and grid[i+1][j-1] == 0 and dist[i+1][j-1] > d+1:
            dist[i+1][j-1] = d+1
            queue.append((i+1, j-1, d+1))

        #bottom right
        if i+1 < n and j+1 < n and grid[i+1][j+1] == 0 and dist[i+1][j+1] > d+1:
            dist[i+1][j+1] = d+1
            queue.append((i+1, j+1, d+1))

    if dist[n-1][n-1] == float('inf'):
        return -1
    return dist[n-1][n-1]


grid = [[1,0,0],[1,1,0],[1,1,0]]
print(shortestPathBinaryMatrix(grid))