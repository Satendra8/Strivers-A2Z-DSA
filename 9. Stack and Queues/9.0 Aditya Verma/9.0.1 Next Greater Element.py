"""
Q. Given an array arr[ ] of integers, the task is to find the next greater element for each element of the array in order of their appearance in the array. Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.

Examples

Input: arr[] = [1, 3, 2, 4]
Output: [3, 4, 4, -1]
Explanation: The next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4, since it doesn't exist, it is -1.
Input: arr[] = [6, 8, 0, 1, 3]
Output: [8, -1, 1, 3, -1]
Explanation: The next larger element to 6 is 8, for 8 there is no larger elements hence it is -1, for 0 it is 1 , for 1 it is 3 and then for 3 there is no larger element on right and hence -1.
Input: arr[] = [10, 20, 30, 50]
Output: [20, 30, 50, -1]
Explanation: For a sorted array, the next element is next greater element also except for the last element.
Input: arr[] = [50, 40, 30, 10]
Output: [-1, -1, -1, -1]
Explanation: There is no greater element for any of the elements in the array, so all are -1.
"""

def nextLargerElement(arr):
    """
    1. in brute force approch j depends on i
    2. using stack
    3. learn loop in reverse order
    4. if stack is empty -> -1
    5. stack.top > arr[i] -> stack.top
    6. stop <= arr[i] -> keep poping
        i. if stack becomes empty -> -1
        ii. otherwise stack.top
    Time Complexity: O(2*N)
    Space Complexity: O(N)
    """
    n = len(arr)
    ans = []
    stack = []

    for i in range(n-1, -1, -1):
        if not stack:
            ans.append(-1)
        elif stack[-1] > arr[i]:
            ans.append(stack[-1])
        else:
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            if not stack:
                ans.append(-1)
            else:
                ans.append(stack[-1])
        stack.append(arr[i])
    ans.reverse()
    return ans

arr = [6, 8, 0, 1, 3]
print(nextLargerElement(arr))