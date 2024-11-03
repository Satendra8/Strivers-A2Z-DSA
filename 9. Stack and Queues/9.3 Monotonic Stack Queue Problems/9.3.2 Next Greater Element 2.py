"""
Q. Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number.
If it doesn't exist, return -1 for this number.

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
"""

def nextGreaterElementCircularBrute(arr):
    """
    1. Brute Force Approach
    2. Time Complexity: O(N^2)
    3. Space Complexity: O(2N)
    """
    arr = arr+arr
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
    return ans[0:n//2]



def nextGreaterElementCircularBetter(arr):
    """
    basic idea: hypothetically double the array
    """
    n = len(arr)
    ans = []
    for i in range(n):
        not_found = True
        for j in range(i+1, n+i):
            if arr[i] < arr[j%n]:
                not_found = False
                ans.append(arr[j%n])
                break
        if not_found:
            ans.append(-1)
    return ans

def nextGreaterElementCircularOptimal(arr):
    """
    Step 1: push all elements in stack in reverse order
    Step 2: iterate over all elements and check if greater element found in stack
    Step 3: if found add it to ans
    Step 4: if not found pop number from stack till greater element found
    Step 5: if stack becomes empty add -1 to ans
    Step 6: keep adding current numbers to stack
    Time Complexity: O(N)
    Space Complexity: O(2N)
    """
    n = len(arr)
    NGE = []
    stack = arr[::-1]

    for i in range(n-1, -1, -1):
        if not stack:
            NGE.append(-1)
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


arr = [2,10,12,1,11]
print(nextGreaterElementCircularOptimal(arr))


