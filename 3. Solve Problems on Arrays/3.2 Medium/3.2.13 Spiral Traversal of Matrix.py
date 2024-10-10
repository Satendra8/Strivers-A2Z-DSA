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


def spiral_matrix(arr):
    """
    1. Time Complexity - O(m+n)
    2. Space Complexity - O(1)
	"""
    n = len(arr[0]) #rows
    m = len(arr) #columns

    top=left=0
    right=n-1
    bottom=m-1
    while left <= right and top <=bottom:

		# move left => right
        for i in range(top, right+1):
            print(arr[top][i], end=" ")
        top += 1
        
		# move top => bottom
        for i in range(top, bottom+1):
            print(arr[i][right], end=" ")
        right -= 1
        
		# move right => left
        for i in range(right, left-1, -1):
            print(arr[bottom][i], end=" ")
        bottom -= 1
        
		# move bottom => top
        for i in range(bottom, top-1, -1):
            print(arr[i][left], end=" ")
        left += 1

arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9],
       [10,11,12]]
spiral_matrix(arr)
    
