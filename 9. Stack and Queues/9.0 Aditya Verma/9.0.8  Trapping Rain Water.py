"""
Q. Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
"""

def maxL(arr, n):
    ans = []
    ans.append(arr[0])

    for i in range(1, n):
        ans.append(max(ans[i-1], arr[i]))
    return ans


def maxR(arr, n):
    ans = [0]*n
    ans[-1] = arr[-1]

    for i in range(n-2, -1, -1):
        ans[i] = max(ans[i+1], arr[i])
    return ans


def trap(arr):
    """
    1. check water on each building
    2. total unit of water = sum of water on each building
    3. water level depend on min(greatest element on left, greatest element on right)
    4. find max to left for each
    5. find max to right for each
    6. find minArr by doing min(maxL, maxR)
    7. do minArr[i] - arr[i]
    8. sum them
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    n = len(arr)
    left = maxL(arr, n)
    right = maxR(arr, n)
    result = 0

    minArr = []

    for i in range(n):
        minArr.append(min(left[i], right[i]))

    for i in range(n):
        result += (minArr[i] - arr[i])
    return result


height = [4,2,0,3,2,5]
print(trap(height))