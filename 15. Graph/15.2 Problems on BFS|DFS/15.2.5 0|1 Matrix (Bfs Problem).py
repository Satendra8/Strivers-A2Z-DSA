"""
Q. Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""

def updateMatrix(mat):
    """
    Use BFS
    1. consider all 0 as source, push them in queue and mark visited
    2. pop from queue and add distance to ans
    3. move in all 4 direction and push to queue if not visited
    Time Complexity: O(M*N)
    Space Complexity: O(2*M*N)
    """
    n = len(mat)
    m = len(mat[0])
    visited = [[0]*m for i in range(n)]
    ans = [[-1]*m for i in range(n)]
    queue = []

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                visited[i][j] = 1
                queue.append((i, j, 0))

    while queue:
        i, j, d = queue.pop(0)
        ans[i][j] = d
        #left
        if j-1 >= 0 and not visited[i][j-1]:
            visited[i][j-1] = 1
            queue.append((i, j-1, d+1))
        
        #right
        if j+1 < m and not visited[i][j+1]:
            visited[i][j+1] = 1
            queue.append((i, j+1, d+1))

        #top
        if i-1 >= 0 and not visited[i-1][j]:
            visited[i-1][j] = 1
            queue.append((i-1, j, d+1))

        #bottom
        if i+1 < n and not visited[i+1][j]:
            visited[i+1][j] = 1
            queue.append((i+1, j, d+1))
    return ans

mat = [[0],[0],[0],[0],[0]]
print(updateMatrix(mat))