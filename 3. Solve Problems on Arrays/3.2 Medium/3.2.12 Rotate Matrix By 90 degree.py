"""
Q. Given a matrix, your task is to rotate the matrix 90 degrees clockwise.

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]

Output: [[7,4,1],[8,5,2],[9,6,3]]

Explanation: Rotate the matrix simply by 90 degree clockwise and return the matrix.

Example 2:

Input: [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

Output:[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Explanation: Rotate the matrix simply by 90 degree clockwise and return the matrix
"""



def rotate_matrix(arr):
    """
1. Brute Force Approach
2. Time Complexity O(N*N)
3. Space Complexity O(N*N)
    """
    
    rows = len(arr[0])
    cols = len(arr)
    final = []
    for i in range(rows):
        curr = []
        for j in range(cols-1, -1, -1):
            curr.append(arr[j][i])
        final.append(curr)
    return final
arr = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate_matrix(arr))



def rotate_matrix_optimized(arr):
    """
1. Better Approach
2. Transpose the matrix
3. Reverse all rows
4. Time Complexity - O(N*N)
5. Space Complexity - O(1)
    """
    
    row = len(arr)
    col = len(arr[0])
    
    for i in range(row):
        for j in range(i, col):
            print(arr[i][j], "<======>", arr[j][i])
            temp = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = temp
    
    for elem in arr:
        elem.reverse()
    return arr
    
arr = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate_matrix_optimized(arr))

"""
[1,2,3]    Transpose      [1,4,7]    Reverse row     [7,4,1]
[4,5,6]   ============>   [2,5,8]   ==============>  [8,5,2]
[7,8,9]                   [3,6,9]                    [9,6,3]
"""