"""
Q. Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of '0's (Water) and '1's(Land). Find the number of islands.

Note: An island is either surrounded by water or the boundary of a grid and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

Examples:

Input: grid = [[0,1],[1,0],[1,1],[1,0]]

Output: 1
Explanation:
The grid is-

All lands are connected.
Input: grid = [[0,1,1,1,0,0,0],[0,0,1,1,0,1,0]]

Output: 2
Expanation:
The grid is-
 
There are two islands :- one is colored in "blue" and other in "red".
"""

def bfsStriver(row, col, visited, m, n, grid):
    """
    for 8 direction row_range [-1,1] and col_range [-1,1]
    """
    visited[row][col] = 1
    queue = [(row, col)]

    while queue:
        i, j = queue.pop(0)

        for drow in range(-1, 2):
            for dcol in range(-1, 2):
                new_row = i + drow
                new_col = j + dcol
                if new_row >= 0 and new_row < n and new_col >= 0 and new_col < m and grid[new_row][new_col] == 1 and not visited[new_row][new_col]:
                    visited[new_row][new_col] = 1
                    queue.append((new_row, new_col))

def bfs(row, col, visited, m, n, grid):
    visited[row][col] = 1
    queue = [(row, col)]

    while queue:
        i, j = queue.pop(0)

        #left
        if j-1 >= 0 and grid[i][j-1] == 1 and not visited[i][j-1]:
            visited[i][j-1] = 1
            queue.append((i, j-1))

        #right
        if j+1 < m and grid[i][j+1] == 1 and not visited[i][j+1]:
            visited[i][j+1] = 1
            queue.append((i, j+1))

        #top
        if i-1 >= 0 and grid[i-1][j] == 1 and not visited[i-1][j]:
            visited[i-1][j] = 1
            queue.append((i-1, j))

        #bottom
        if i+1 < n and grid[i+1][j] == 1 and not visited[i+1][j]:
            visited[i+1][j] = 1
            queue.append((i+1, j))

        #top left
        if i-1 >= 0 and  j-1 >= 0 and grid[i-1][j-1] == 1 and not visited[i-1][j-1]:
            visited[i-1][j-1] = 1
            queue.append((i-1, j-1))

        #top right
        if i-1 >= 0 and  j+1 < m and grid[i-1][j+1] == 1 and not visited[i-1][j+1]:
            visited[i-1][j+1] = 1
            queue.append((i-1, j+1))

        #bottom left
        if i+1 < n and  j-1 >= 0 and grid[i+1][j-1] == 1 and not visited[i+1][j-1]:
            visited[i+1][j-1] = 1
            queue.append((i+1, j-1))

        #bottom right
        if i+1 < n and  j+1 < m  and grid[i+1][j+1] == 1 and not visited[i+1][j+1]:
            visited[i+1][j+1] = 1
            queue.append((i+1, j+1))
        print(queue)

def numIslands(grid):
    """
    Using DFS
    1. Same as connected components
    2. iterate over all cells (M*N)
    3. run BFS/DFS if they are not visited
    4. check in all 8 directions, if there is 1 and not visited cell
    Time Complexity: O(M*N) + O(M*N)
    Space Complexity: O(M*N) + O(M*N)
    """
    n = len(grid)
    m = len(grid[0])

    visited = [[0]*m for i in range(n)]
    counter = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                print(i,j)
                bfsStriver(i, j, visited, m, n, grid)
                counter += 1
    return counter


grid = [[0,1,1,1,0,0,0],[0,0,1,1,0,1,0]]
print(numIslands(grid))