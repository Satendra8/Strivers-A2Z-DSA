"""
Q. Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
"""

def NSR(arr, n):
    """
    pattern: nearest smaller to right
    push n if stack is empty as right most
    """
    stack = []
    ans = []

    for i in range(n-1, -1, -1):
        if not stack:
            ans.append(n)
        elif stack[-1][0] < arr[i]:
            ans.append(stack[-1][1])
        else:
            while stack and stack[-1][0] >= arr[i]:
                stack.pop()
            if not stack:
                ans.append(n)
            else:
                ans.append(stack[-1][1])
        stack.append((arr[i], i))
    ans.reverse()
    return ans


def NSL(arr, n):
    """
    pattern: nearest smaller to right
    push -1 if stack is empty as left most
    """
    stack = []
    ans = []

    for i in range(n):
        if not stack:
            ans.append(-1)
        elif stack[-1][0] < arr[i]:
            ans.append(stack[-1][1])
        else:
            while stack and stack[-1][0] >= arr[i]:
                stack.pop()
            if not stack:
                ans.append(-1)
            else:
                ans.append(stack[-1][1])
        stack.append((arr[i], i))
    return ans

def getMaxArea(arr):
    """
    1. Building can be expended into other building if other building >= current building
    2. Find nearest smaller to right
    3. Find nearest smaller to left
    3. Find width = right[i] - left[i] - 1
    4. area =  widht[i] * arr[i]
    5. return max of area
    """
    n = len(arr)
    right = NSR(arr, n)
    left = NSL(arr, n)
    width = []

    for i in range(n):
        width.append(right[i]-left[i]-1)
    area = []
    for i in range(n):
        area.append(width[i]*arr[i])
    return max(area)


def maximalRectangle(matrix):
    """
    1. pattern in getMaxArea of rectangle we were finding the same max area
    2. don't start this from scratch
    3. how it is different from getMaxArea of rectangle
        i. here we have 2D array
        ii. binary input
    4. convert 2D array into 1D then apply getMaxArea of rectangle
    5. then return max of them
    6. if the bottom elemnent is 0 then don't add it (no building without base)
    Time Complexity: O(M*N)
    Space Complexity: O(M*N)
    """
    m = len(matrix)
    n = len(matrix[0])

    ans = []

    arr = [0]*n
    for i in range(m):
        for j in range(n):
            if matrix[i][j] != "0":
                arr[j] += int(matrix[i][j])
            else:
                arr[j] = 0
        ans.append(getMaxArea(arr))
    return max(ans)


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalRectangle(matrix))
