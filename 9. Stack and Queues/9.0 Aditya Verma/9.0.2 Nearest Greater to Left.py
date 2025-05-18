"""
Q. Given an array arr[] of size n. For each element in the array, find the value wise closest element to its left that is greater than or equal to the current element. If no such element exists, return -1 for that position.

Examples:  

Input : arr[] = [10, 5, 11, 6, 20, 12]
Output : [-1, 10, -1, 10, -1, 20]
Explanation: The first element has nothing on the left side, so the answer for first is -1. 
Second, element 5 has 10 on the left, so the answer is 10. 
Third element 11 has nothing greater or the same, so the answer is -1. 
Fourth element 6 has 10 as value wise closest, so the answer is 10.
Similarly, we get values for the fifth and sixth elements.

Input : arr[] = [1, 2, 3, 4, 5]
Output : [-1, -1, -1, -1, -1]
Explanation: The given array is arranged in strictly increasing order, and all the elements on left of any element are smaller. Thus no index has any value greater or equal in its left.

Input : arr[] = [5, 4, 3, 2, 1]
Output : [-1, 5, 4, 3, 2]
"""

def prevLargerElement(arr):
    """
    1. in brute force approch j depends on i
    2. using stack
    3. if stack is empty -> -1
    4. stack.top > arr[i] -> stack.top
    5. stop <= arr[i] -> keep poping
        i. if stack becomes empty -> -1
        ii. otherwise stack.top
    Time Complexity: O(2*N)
    Space Complexity: O(N)
    """
    n = len(arr)
    ans = []
    stack = []

    for i in range(n):
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
    return ans

arr = [10, 5, 11, 6, 20, 12]
print(prevLargerElement(arr))