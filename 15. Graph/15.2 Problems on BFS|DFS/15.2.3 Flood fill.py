"""
Q. You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.

Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]

Explanation:

From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

Note the bottom corner is not colored 2, because it is not horizontally or vertically connected to the starting pixel.

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0

Output: [[0,0,0],[0,0,0]]

Explanation:

The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.
"""

def floodFill(image, sr, sc, color):
    """
    Using BFS
    1. if color is same as initial, no need to proceed
    2. store initial color
    3. move left, right, top, bottom, if color matches with initial color 
    4. keep filling with new color and push in queue
    Time Complexity: O(M*N)
    Space Complexity: O(M*N)
    """
    initial = image[sr][sc]

    #if color is same as initial, no need to proceed
    if initial == color:
        return
    n = len(image)
    m = len(image[0])

    queue = [(sr, sc)]
    image[sr][sc] = color

    while queue:
        i, j = queue.pop(0)
        print(i,j)
        #left
        if j-1 >= 0 and image[i][j-1] == initial:
            image[i][j-1] = color
            queue.append((i, j-1))

        #right
        if j+1 < m and image[i][j+1] == initial:
            image[i][j+1] = color
            queue.append((i, j+1))

        #top
        if i-1 >= 0 and image[i-1][j] == initial:
            image[i-1][j] = color
            queue.append((i-1, j))
        
        #bottom
        if i+1 < n and image[i+1][j] == initial:
            image[i+1][j] = color
            queue.append((i+1, j))


def floodFillDFS(image, sr, sc, color, init, m, n):
    """
    Use DFS
    1. pick a cell
    2. move to left, right, top and bottom recusrively
    3. base case if init and color are same
    Time Complexity: O(4MN) # for each node going left, right, top, bottom
    Space Complexity: O(MN)
    """
    if init == color:
        return
    image[sr][sc] = color

    #left
    if sc-1 >= 0 and image[sr][sc-1] == init:
        floodFillDFS(image, sr, sc-1, color, init, m, n)
    
    #right
    if sc+1 < n and image[sr][sc+1] == init:
        floodFillDFS(image, sr, sc+1, color, init, m, n)

    #top
    if sr-1 >= 0 and image[sr-1][sc] == init:
        floodFillDFS(image, sr-1, sc, color, init, m, n)

    #bottom
    if sr+1 < m and image[sr+1][sc] == init:
        floodFillDFS(image, sr+1, sc, color, init, m, n)


image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
init = image[sr][sc]
n = len(image)
m = len(image[0])
floodFillDFS(image, sr, sc, color, init, m, n)
print(image)