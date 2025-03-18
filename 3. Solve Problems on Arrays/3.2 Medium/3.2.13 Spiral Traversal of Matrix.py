"""
Q. Given a Matrix, print the given matrix in spiral order.

Example 1:
Input: Matrix[][] = { { 1, 2, 3, 4 },
		      { 5, 6, 7, 8 },
		      { 9, 10, 11, 12 },
	              { 13, 14, 15, 16 } }

Outhput: 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10.
Explanation: The output of matrix in spiral form.

Example 2:
Input: Matrix[][] = { { 1, 2, 3 },
	              { 4, 5, 6 },
		      { 7, 8, 9 } }
			    
Output: 1, 2, 3, 6, 9, 8, 7, 4, 5.
Explanation: The output of matrix in spiral form.
"""
"""
(0,0)(0,1)(0,2)(0,3)
(1,0)(1,1)(1,2)(1,3)
(2,0)(2,1)(2,2)(2,3)
(3,0)(3,1)(3,2)(3,3)

top=0      right=3
1, 2, 3, 4
5, 6, 7, 8
9,10,11,12
13,14,15,16
left=0      bottom=3



1. loop i = 0, j(0, right)
    bottom += 1
2. loop j=3, i(1, bottom)
    left -= 1
3. loop i=3, j(2, 0)
    top -= 1
4. loop j=0, i(2, 0)
    top += 1

"""
"""
    1. Time Complexity - O(m+n)
    2. Space Complexity - O(1)
"""


def spiralOrder(matrix):
    """
    1. go from left to right
    2. go from top to down
    3. again from right to left
    4. again down to top
    5. edge case 1: don't go right to left if single row
    5. edge case 2: don't go down to top if single column
    Time Complexity: O(M*N)
    Space Complexity: O(1)
    """
    ans = []
    m = len(matrix)
    n = len(matrix[0])

    left = 0
    right = n - 1
    top = 0
    down = m - 1

    while left <= right and top <= down:
        for i in range(left, right+1):
            ans.append(matrix[top][i])
        top += 1

        for i in range(top, down+1):
            ans.append(matrix[i][right])
        right -= 1

        if top <= down: #if single row don't do this
            for i in range(right, left-1, -1):
                ans.append(matrix[down][i])
            down -= 1

        if left <= right: #if single column don't do this
            for i in range(down, top-1, -1):
                ans.append(matrix[i][left])
            left += 1

    return ans

arr = matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

spiralOrder(arr)