"""
Q. Given an array arr[] of integers, for each element in the array, find the nearest smaller element on its left. If there is no such smaller element, return -1 for that position.

Input: arr[] = [1, 6, 2]
Output: [-1, 1, 1]
Explaination: 
There is no number to the left of 1, so we return -1. 
After that, the number is 6, and the nearest smaller number on its left is 1. 
Next, the number is 2, and the nearest smaller number on the left is also 1.
Input: arr[] = [1, 5, 0, 3, 4, 5]
Output: [-1, 1, -1, 0, 3, 4]
Explaination: 
There is no number to the left of 1,  so we return -1. 
After that, the number is 5,  and the nearest smaller number on its left is 1. 
 Next, the number is 0, and there is no smaller number on the left, so we return -1.
Then comes 3, and the nearest smaller number on its left is 0.
After that, the number is 4, and the nearest smaller number on the left is 3. 
Finally, the number is 5, and the nearest smaller number on its left is 4.
"""

def leftSmaller(arr):
    """
    1. pattern identification: j depends on i in O(n^2) solution
    2. use stack
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    n = len(arr)
    ans = []
    stack = []

    for i in range(n):
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
    return ans

arr = [4,5,2,10,8]
print(leftSmaller(arr))