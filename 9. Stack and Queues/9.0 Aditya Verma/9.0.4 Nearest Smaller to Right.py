"""
Q. Given an array arr[] of integers, for each element in the array, find the nearest smaller element on its right. If there is no such smaller element, return -1 for that position.

Input: arr[] = [1, 6, 2]
Output: [-1, 2, -1]

Input: arr[] = [4, 5, 2, 10, 8]
Output: [2,2,-1,8,-1]
"""

def rightSmaller(arr):
    """
    1. pattern identification: j depends on i in O(n^2) solution
    2. use stack
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    n = len(arr)
    ans = []
    stack = []

    for i in range(n-1, -1, -1):
        if not stack:
            ans.append(-1)
        elif stack[-1] < arr[i]:
            ans.append(stack[-1])
        else:
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            if not stack:
                ans.append(-1)
            else:
                ans.append(stack[-1])
        stack.append(arr[i])
    ans.reverse()
    return ans

arr = [4,5,2,10,8]
print(rightSmaller(arr))