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
    stack = []
    ans = []

    for i in range(n-1, -1, -1):
        if not stack:
            ans.append(n-i-1)
        elif arr[i] > stack[-1][0]:
            ans.append(stack[-1][1]-i-1)
        else:
            while stack and arr[i] <= stack[-1][0]:
                stack.pop()
            if not stack:
                ans.append(n-i-1)
            else:
                ans.append(stack[-1][1]-i-1)
        stack.append((arr[i], i))
    ans.reverse()
    return ans

def NSL(arr, n):
    stack = []
    ans = []

    for i in range(n):
        if not stack:
            ans.append(i-(-1))
        elif arr[i] > stack[-1][0]:
            ans.append(i-stack[-1][1])
        else:
            while stack and arr[i] <= stack[-1][0]:
                stack.pop()
            if not stack:
                ans.append(i-(-1))
            else:
                ans.append(i-stack[-1][1])
        stack.append((arr[i], i))
    return ans


def rectangle(arr):
    n = len(arr)
    right = NSR(arr, n)
    left = NSL(arr, n)

    print(left)
    print(right)
    area = []
    for i in range(n):
        area.append(arr[i] * (left[i]+right[i]))
    return max(area)


def maximal(matrix):
    row = len(matrix)
    col = len(matrix[0])
    ans = []

    arr = [0] * col

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == '1':
                arr[j] += int(matrix[i][j])
            else:
                arr[j] = 0
        ans.append(rectangle(arr))
    return max(ans)

matrix = [["1"]]
print(maximal(matrix))