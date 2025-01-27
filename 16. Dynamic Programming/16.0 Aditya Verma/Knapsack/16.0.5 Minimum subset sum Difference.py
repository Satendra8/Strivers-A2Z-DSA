"""
Q. You are given an integer array nums of 2 * n integers. You need to partition nums into two arrays of length n to minimize the absolute difference of the sums of the arrays. To partition nums, put each element of nums into one of the two arrays.

Return the minimum possible absolute difference.

Example 1:

example-1
Input: nums = [3,9,7,3]
Output: 2
Explanation: One optimal partition is: [3,9] and [7,3].
The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.
Example 2:

Input: nums = [-36,36]
Output: 72
Explanation: One optimal partition is: [-36] and [36].
The absolute difference between the sums of the arrays is abs((-36) - (36)) = 72.
Example 3:

example-3
Input: nums = [2,-1,0,4,-2,-9]
Output: 0
Explanation: One optimal partition is: [2,4,-9] and [-1,0,-2].
The absolute difference between the sums of the arrays is abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0.
"""

def subsetSum(arr, target, n, t):
    for i in range(n+1):
        t[i][0] = True

    for i in range(1, n+1):
        for j in range(1, target+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t



def minimumDifference(nums):
    """
    Variation of subsetSum Problem
    1. divide the array in s1 & s2
    2. now we don't know s1&s2 to taking range 0 to sum(nums)
    3. s1&s2 lies b/w 0 to sum(nums)
    4. we need to minimize s1-s2
    5. s1 - range - s1 (minimize)
    6. range - 2s1 (minimize)
    7. now we need to only find s1
    8. s1 lies b/w 0 to sum(nums)//2
    9. check all possible sum using subset sum
    10. only last row of subset sum is useful for checking possible value of s1
    11. How to handle negative case
        ** shift all values to the right (+ve)
        ** find offset min(nums)
        ** add offset to all elements
    12. apply value in formula range - 2s1 and find minimum
    Time Complexity: O(nums * sum(nums))
    Space Complexity: O(nums * sum(nums))
    """
    offset = abs(min(nums))
    normalized_nums = [offset+num for num in nums]
    n = len(normalized_nums)
    target = sum(normalized_nums)

    t = [[False] * (target+1) for _ in range(n+1)]
    t = subsetSum(normalized_nums, target, n, t)
    minimize = float('inf')
    for i in range(target//2+1):
        if t[n][i]:
            minimize = min(minimize, target - 2 * i)
    return minimize


nums = [91,14,16,82,32,2,38,94]
print(minimumDifference(nums))