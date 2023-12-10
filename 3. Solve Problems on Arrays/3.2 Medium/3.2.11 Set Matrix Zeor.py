"""
Q. Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.

Examples 1:

Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]

Output: [[1,0,1],[0,0,0],[1,0,1]]

Explanation: Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.
 
Input: matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

Output:[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Explanation:Since matrix[0][0]=0 and matrix[0][3]=0. Therefore 1st row, 1st column and 4th column will be set to 0

"""

import copy
def set_matrix_zero(arr):
    """
    1. Brute Force Approach
    2. Time Complexity - O(N^3)
    3. Space Complexity - O(N^2)
    """
    n = len(arr)
    m = len(arr[0])
    new = copy.deepcopy(arr)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                print(i, j)
                for k in range(m):
                    new[i][k] = 0
                for k in range(n):
                    new[k][j] = 0
    print(new)
    return arr
    
arr = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
set_matrix_zero(arr)


def set_matrix_zero_striver(arr):
    """
    1. Brute Force Approach
    2. Traverse over the each element
    3. Mark row and col to -1 if current element is 0
    4. Again Iterate over each element to and mark -1 to 0
    5. Time Complexity - O(M*N*(M+N))
    6. Space Complexity - O(1)
    """
    m = len(arr)
    n = len(arr[0])
    
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                
                for k in range(m):
                    if arr[k][j] !=0:
                        arr[k][j] = -1
                for k in range(n):
                    if arr[i][k] !=0:
                        arr[i][k] = -1
                
    for i in range(m):
        for j in range(n):
            if arr[i][j] == -1:
                arr[i][j] = 0
    print(arr)
arr = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
set_matrix_zero(arr)



def set_matrix_zero(arr):
    """
    1. Better Approach
    2. used set to store row or col with 0
    3. traversed again the matrix and mark row or col 0 if found in set
    4. Time Complexity - O(M*N)
    5. Space Complexity - O(M+N)
    """
    n = len(arr[0])
    m = len(arr)
    row = set()
    col = set()
    
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                row.add(i)
                col.add(j)
    
    for i in range(m):
        for j in range(n):
            if i in row or j in col:
                arr[i][j] = 0
        
            
    print(arr)


def set_matrix_zero_striver(arr):
    """
    1. Better Approach
    2. used arrays to store row or col with 0
    3. traversed again the matrix and mark row or col 0 if found in array
    4. Time Complexity - O(M*N)
    5. Space Complexity - O(M+N)
    """
    m = len(arr)
    n = len(arr[0])
    
    row = [0]*m
    col = [0]*n

    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                row[i] = 1
                col[j] = 1
                
    for i in range(m):
        for j in range(n):
            if row[i] == 1 or col[j] == 1:
                arr[i][j] = 0
    print(arr)
arr = [[1,1,1],[1,0,1],[1,1,1]]
set_matrix_zero(arr)



def set_matrix_zero(arr):
    """
    1. Optimal Approach
    2. Check each element and if it is 0 then mark 0 in first row and first col corresponding to that
    3. store the natural 0 of first row and first col in variables x and y
    4. Ignore first row and first col (as they are working as storage) mark 0 other elements if there corresponding row and col has 0
    5. check varible x and y and mark column or row to 0 if they are 0
    6. Time Complexity - O(M*N)
    7. Space Complexity - O(1)
    
    """
    m = len(arr)
    n = len(arr[0])
    x = None
    y = None
    
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                if i==0:
                    x = 0
                if j==0:
                    y=0
                arr[0][j] = 0
                arr[i][0] = 0
    for i in range(1, m):
        for j in range(1, n):
            if arr[i][j] != 0:
                if arr[0][j] == 0 or arr[i][0] == 0:
                    arr[i][j] = 0
    if y == 0:
        for i in range(m):
            print("i", arr[i][0])
            arr[i][0] = 0
    if x == 0:
        for j in range(n):
            arr[0][j] = 0
            
                    
    print(arr)

arr = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
set_matrix_zero(arr)