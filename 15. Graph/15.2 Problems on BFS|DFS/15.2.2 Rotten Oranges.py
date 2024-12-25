"""
Q. You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""

def orangesRotting(grid):
    """
    Use BFS (because need to go simultaneously at each neighbouring node)
    1. push all cell having 2 in queue (row, col, count)
    2. pop from queue
    3. mark rotten left, right, top, bottom
    4. keep updating the max_time
    5. return -1 if any fresh orange left
    6. return max_time
    Time Complexity: O(M*N)
    Space Complexity: O(M*N)
    """
    n = len(grid)
    m = len(grid[0])
    max_time = 0
    queue = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                queue.append((i, j, 0))

    while queue:
        curr = queue.pop(0)
        i, j, cnt = curr
        #left
        if j-1 >= 0 and grid[i][j-1] == 1:
            grid[i][j-1] = 2
            queue.append((i, j-1, cnt+1))
        #right
        if j+1 < m and grid[i][j+1] == 1:
            grid[i][j+1] = 2
            queue.append((i, j+1, cnt+1))
        #top
        if i-1 >= 0 and grid[i-1][j] == 1:
            grid[i-1][j] = 2
            queue.append((i-1, j, cnt+1))
        #down
        if i+1 < n and grid[i+1][j] == 1:
            grid[i+1][j] = 2
            queue.append((i+1, j, cnt+1))
        max_time = max(max_time, cnt)

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                return -1
    return max_time

grid = [[0,2]]
print(orangesRotting(grid))