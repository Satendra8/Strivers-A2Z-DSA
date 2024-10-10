"""
Q. You have been given a 2-D array 'mat' of size 'N x M' where 'N' and 'M' denote the number of rows and columns, respectively. The elements of each row and each column are sorted in non-decreasing order.
But, the first element of a row is not necessarily greater than the last element of the previous row (if it exists).
You are given an integer 'target', and your task is to find if it exists in the given 'mat' or not.


Example 1:
Input Format:
 N = 5, M = 5, target = 14
mat[] = 

Result:
 true
Explanation:
 Target 14 is present in the cell (3, 2)(0-based indexing) of the matrix. So, the answer is true.

Example 2:
Input Format:
 N = 3, M = 3, target = 12,
mat[] = 

Result:
 false
Explanation:
 As target 12 is not present in the matrix, the answer is false.
"""

def searchMatrix(matrix, target):
    """
    1. Brute Force Approach
    2. check every element in matrix and if found return True
    3. if not found return False
    4. Time Complexity: O(m*n)
    5. Space Complexity: O(1)
    """
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == target:
                return True
    return False



def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left+right) // 2

        if arr[mid] == target:
            return True
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

def searchMatrix(matrix, target):
    """
    1. Better Approach
    2. pick 1 row and apply binary search to find element
    3. if found then return else keep cheking
    4. Time Complexity: O(n*logm)
    5. Space Complexity: O(1)
    """
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        ans = binarySearch(matrix[i], target)
        if ans:
            return True
    return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 25
print(searchMatrix(matrix, target))


def searchMatrix(matrix, target):
    """
    1. Optimal Approach
    2. stand at matrix[0][m-1], here left elements are smaller and down elements are larger
    3. if matrix[row][col] == target return True
    4. matrix[row][col] > target, so target will never be on down eleminate col
    5. matrix[row][col] < target, so target will never be on left eleminate row
    6. Time Complexity: O(n+m)
    7. Space Complexity: O(1)
    """
    n = len(matrix)
    m = len(matrix[0])

    row = 0
    col = m - 1

    while row <= n - 1 and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 27
print(searchMatrix(matrix, target))



"""
[

(0,0) (0,1) (0,2) (0,3) (0,4)
[1,    4,    7,    11,   15],
(1,0) (1,1) (1,2) (1,3) (1,4)
[2,    5,    8,    12,   19],
(2,0) (2,1) (2,2) (2,3) (2,4)
[3,    6,    9,    16,   22],
(3,0) (3,1) (3,2) (3,3) (3,4)
[10,   13,   14,   17,   24],
(4,0) (4,1) (4,2) (4,3) (4,4)
[18,   21,   23,   26,   30]
]

if i stand on 15 (0,4) left elements are smaller and down elements are larger
i will use the same to solve this problem

target = 14

row = 0, col = 4, element=15, so target will never be on down eleminate col
row = 0, col = 3, element=11, so target will never be on left eleminate row
row = 1, col = 3, element=12, so target will never be on left eleminate row
row = 2, col = 3, element=16, so target will never be on down eleminate col
row = 2, col = 2, element=9, so target will never be on left eleminate row
row = 3, col = 2, element=14, target matched

target = 25

row = 0, col = 4, element=15, so target will never be on left eleminate row
row = 1, col = 4, element=19, so target will never be on left eleminate row
row = 2, col = 4, element=22, so target will never be on left eleminate row
row = 3, col = 4, element=24, so target will never be on left eleminate row
row = 4, col = 4, element=30, so target will never be on down eleminate col
row = 4, col = 3, element=26, so target will never be on down eleminate col
row = 4, col = 2, element=23, so target will never be on left eleminate row
row = 5, col = 2, break


target = 6

row = 0, col = 4, element=15, so target will never be on down eleminate col
row = 0, col = 3, element=11, so target will never be on down eleminate col
row = 0, col = 2, element=7, so target will never be on down eleminate col
row = 0, col = 1, element=4, so target will never be on left eleminate row
row = 1, col = 1, element=5, so target will never be on left eleminate row
row = 2, col = 1, element=6, target mathced
"""