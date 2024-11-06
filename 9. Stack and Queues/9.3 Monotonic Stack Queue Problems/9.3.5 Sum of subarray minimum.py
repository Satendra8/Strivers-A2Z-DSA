"""
Q. Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444
"""

def sumSubarrayMinsBrute(arr):
    n = len(arr)
    summ = 0

    for i in range(n):
        for j in range(i, n):
            summ += min(arr[i:j+1])
    return summ

def sumSubarrayMinsBetter(arr):
    n = len(arr)
    summ = 0

    for i in range(n):
        minn = arr[i]
        for j in range(i, n):
            minn = min(minn, arr[j])
            summ += minn
    return summ


def nextSmallerElement(arr):
    n = len(arr)
    stack = []
    ans = [n]*n # Initialize with `n` to represent the boundary (no smaller element found)
    for i in range(n-1, -1, -1):
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        ans[i] = stack[-1] if stack else n
        stack.append(i)
    return ans


def prevSmallerEqualElement(arr):
    n = len(arr)
    stack = []
    ans = [-1]*n # Initialize with `-1` to represent no previous smaller element

    for i in range(n):
        while stack and arr[i] < arr[stack[-1]]:
            stack.pop()
        ans[i] = stack[-1] if stack else -1
        stack.append(i)
    return ans


def sumSubarrayMinsOptimal(arr):
    """
    Step1: find next smaller element
    Step2: find prev smaller element
    Step3: find distance from left and right
    Step4: now multiply left*right*number and add to sum
    Time Complexity: O(N+N+N)
    Space Complexity: O(2N+2N)
    """
    n = len(arr)
    prev = prevSmallerEqualElement(arr)
    after = nextSmallerElement(arr)
    ans = 0
    mod = 10 ** 9 + 7
    for i in range(n):
        left = i - prev[i]
        right = after[i] - i
        ans = (ans + (((left * right)%mod) * arr[i]) % mod)%mod
    return ans



arr = [1,1]
print(prevSmallerEqualElement(arr))
print(nextSmallerElement(arr))
print(sumSubarrayMinsOptimal(arr))

"""
Intution:
arr = [3,1,2,4]

subarrays

3           = 3
3,1         = 1
3,1,2       = 1
3,1,2,4     = 1

1           = 1
1,2         = 1
1,2,4       = 1

2           = 2
2,4         = 2

4           = 4

contributions
x1  x6 x2 x1
[3, 1, 2, 4]

now problem is brokendown intto find the contributions

          0 1 2 3 4 5 6 7
consider [1,4,6,7,3,7,8,1]

contribution of 3 in ans on right side (next smaller element is 1 so ignoring 7th index)
[3]
[3,7]
[3,7,8]

contribution of 3 in ans on left side (prev smaller element is 1 so ignoring 0th index)
[4,6,7,3]
[6,7,3]
[7,3]
[3] #already counted

mid contribution

[3] #already counted
[7,3,7]
[6,7,3,7]
[7,3,7,8]
[4,6,7,3,7]
[6,7,3,7,8]
[4,6,7,3,7,8]

for final is left * right = 3 * 4 = 12

Find Next smaller element


Step1: find next smaller element
Step2: find prev smaller element
Step3: find distance from left and right
Step4: now multiply left*right*number and add to sum

Dry Run:

arr = [3,1,2,4]
prev smaller elements = [-1,-1,1,2]
next smaller elements = [1,4,4,4]

ans = [1*1*3, 2*3*1, 1*2*2, 1*1*4] = 17

Edge Case:
       0  1
arr = [1, 1]
nse =  2  2
pse =  -1 0(considering prev smaller is on 0th to avoid double counting) 

[1] -> 0 index
[1,1]
[1] -> 1 index

contributions = 3 (need to fix double counting here)
find prev smaller equal element
"""