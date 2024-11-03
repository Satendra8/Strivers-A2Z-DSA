"""
Q. Given a circular integer array A, return the next greater element for every element in A.
   The next greater element for an element x is the first element greater than x that we come across while traversing the array. If it doesn't exist, return -1 for this element.

Example 1: 

Input: N = 11, A[] = {3,10,4,2,1,2,6,1,7,2,9}

Output: 10,-1,6,6,2,6,7,7,9,9,-1


Example 2:

Input:  N = 6, A[] = {5,7,1,7,6,0}

Output: 7,-1,7,-1,-1,-1

"""

def nextGreaterElementBrute(arr):
    """
    1. Brute Force Approach
    2. Time Complexity: O(N^2)
    3. Space Complexity: O(2N)
    """
    arr = arr
    n = len(arr)
    ans = []
    for i in range(n):
        flag = True
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                ans.append(arr[j])
                flag = False
                break
        if flag:
            ans.append(-1)
    return ans



def nextGreaterElementOptimal(arr):
    """
    Basic idea: maintain elements in stack in increasing order (maintaining some order in stack is called monotonic stack problem)
    
    """
    n = len(arr)
    NGE = []
    stack = []

    for i in range(n-1, -1, -1):
        if not stack:
            NGE.append(-1)
        else:
            if arr[i] < stack[-1]:
                NGE.append(stack[-1])
            else:
                while stack and arr[i] >= stack[-1]:
                    stack.pop()
                if stack:
                    NGE.append(stack[-1])
                else:
                    NGE.append(-1)
        stack.append(arr[i])
    return NGE[::-1]

arr = [3,10,4,2,1,2,6,1,7,2,9]
print(nextGreaterElementOptimal(arr))