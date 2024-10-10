"""
Q. You have been given a 2-D array 'mat' of size 'N x M' where 'N' and 'M' denote the number of rows and columns, respectively. The elements of each row are sorted in non-decreasing order. Moreover, the first element of a row is greater than the last element of the previous row (if it exists). You are given an integer 'target', and your task is to find if it exists in the given 'mat' or not.

Example 1:
Input Format:
 N = 3, M = 4, target = 8,
mat[] = 
1 2 3 4
5 6 7 8 
9 10 11 12
Result:
 true
Explanation:
 The 'target'  = 8 exists in the 'mat' at index (1, 3).

Example 2:
Input Format:
 N = 3, M = 3, target = 78,
mat[] = 
1 2 4
6 7 8 
9 10 34
Result:
 false
Explanation:
 The 'target' = 78 does not exist in the 'mat'. Therefore in the output, we see 'false'.
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

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 20
print(searchMatrix(matrix, target))




def searchMatrix(matrix, target):
    """
    1. Better Approach
    2. pick each row
    3. check if target exist in that row using binary search
    4. Time Complexity: O(n) + O(logm) because binary search only performed once
    5. Space Complexity: O(1)
    """
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        left = 0
        right = cols - 1

        while left <= right:
            mid = (left+right) // 2
            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 15
print(searchMatrix(matrix, target))



def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

def searchMatrix(matrix, target):
    """
    1. Optimal Approach
    2. Apply binary search on both rows and cols
    3. if matrix[row_mid][0] <= target <= matrix[row_mid][cols-1] then this is the row we need to find the number
    4. if matrix[row_mid][0] > target move to left
    5. else move to right
    6. Time Complexity: O(logm*n)
    7. Space Complexity: O(1)
    """
    rows = len(matrix)
    cols = len(matrix[0])

    row_left = 0
    row_right = rows - 1

    while row_left <= row_right:
        row_mid = (row_left + row_right) // 2
        if matrix[row_mid][0] <= target <= matrix[row_mid][cols-1]:
            return binarySearch(matrix[row_mid], target)
        elif matrix[row_mid][0] > target:
            row_right = row_mid - 1
        else:
            row_left = row_mid + 1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 31
print(searchMatrix(matrix, target))


"""
[[1,3,5,7],[10,11,16,20],[23,30,34,60]] target = 20 row_left=0, row_right=2, row_mid=1

[[1,3,5,7],[10,11,16,20],[23,30,34,60]] target = 5 row_left=0, row_right=2, row_mid=1
                                                   row_left=0, row_right=1, row_mid=0

[[1,3,5,7],[10,11,16,20],[23,30,34,60]] target = 31 row_left=0, row_right=2, row_mid=1
                                                    row_left=2, row_right=2, row_mid=2

"""




def searchMatrix(matrix, target):
    """
    1. Striver's Optimal Approach
    2. Hypothetically flatten array then apply binary search
    3. find row and col of mid using formula row = mid/m, col = mid%m
    4. if matrix[row][col] == target return True
    5. if matrix[row][col] > target then search on left
    6. if matrix[row][col] < target then search on right
    7. Time Complexity: O(logm*n)
    8. Space Complexity: O(1)
    """
    rows = len(matrix)
    cols = len(matrix[0])
    left = 0
    right = rows * cols - 1

    while left <= right:
        mid = (left+right) // 2
    
        row = mid//cols
        col = mid%cols

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 20
print(searchMatrix(matrix, target))


"""
[[1,3,5,7],[10,11,16,20],[23,30,34,60]]

Hypothetically flatten array then apply binary search

 0 1 2 3 4   5 6  7  8  9  10  11
[1,3,5,7,10,11,16,20,23,30,34,60]

m = 4, n = 3

(0,0) (0,1) (0,2) (0,3)
[1,    3,    5,    7]
(1,0) (1,1) (1,2)   (1,3)
[10,    11,    16,    20]
(2,0)  (2,1)  (2,2)  (2,3)
[23,    30,    34,    60]

formula => row = 5/m = 1
           col = 5%m = 1

intution behind the formula
for row we have m=4 elements in each row so we can find the row number by dividing
for column we can find by using %


DRY RUN:
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 20

left=0, right= 11, mid=5, row=1, col=1, elem=11
left=6, right= 11, mid=8, row=2, col=0, elem=23
left=6, right= 7, mid=6, row=1, col=2, elem=16
left=7, right= 7, mid=7, row=1, col=3, elem=20


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 31

left=0, right= 11, mid=5, row=1, col=1, elem=11
left=6, right= 11, mid=8, row=2, col=0, elem=23
left=9, right= 11, mid=10, row=2, col=2, elem=34
left=9, right= 9, mid=10, row=2, col=1, elem=30
left=9, right= 8, mid=9, break




"""