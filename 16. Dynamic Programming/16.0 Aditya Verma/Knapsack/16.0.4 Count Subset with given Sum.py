"""
Q. Given an array arr of non-negative integers and an integer target, the task is to count all subsets of the array whose sum is equal to the given target.

Examples:

Input: arr[] = [5, 2, 3, 10, 6, 8], target = 10
Output: 3
Explanation: The subsets {5, 2, 3}, {2, 8}, and {10} sum up to the target 10.
Input: arr[] = [2, 5, 1, 4, 3], target = 10
Output: 3
Explanation: The subsets {2, 1, 4, 3}, {5, 1, 4}, and {2, 5, 3} sum up to the target 10.
Input: arr[] = [5, 7, 8], target = 3
Output: 0
Explanation: There are no subsets of the array that sum up to the target 3.
Input: arr[] = [35, 2, 8, 22], target = 0
Output: 1
Explanation: The empty subset is the only subset with a sum of 0.
"""
def perfectSumRecursive(arr, target, n, add, i):
    if target == add:
        return 1
    if i == n:
        return 0

    return perfectSumRecursive(arr, target, n, add+arr[i], i+1) + perfectSumRecursive(arr, target, n, add, i+1)
    

def perfectSumMemoization(arr, target, n, t):
    if target == 0:
        return 1
    if n == 0:
        return 0

    if t[n-1][target] != -1: return t[n-1][target]

    if arr[n-1] <= target:
        t[n-1][target] =  perfectSumMemoization(arr, target-arr[n-1], n-1, t) + perfectSumMemoization(arr, target, n-1, t)
    else:
        t[n-1][target] = perfectSumMemoization(arr, target, n-1, t)
    return t[n-1][target]


def perfectSum(arr, target):
    """
    Top Down Approach (Similar to Subset Sum)
    1. initialization: we can make sum=0 without choosing any element hence first col will be 1
    2. either choose or not choose
    3. add up all the previous result same as memoization
    4. edge case: start the j loop with 0 to make contribution of 0 in ans
    Time Complexity: O(target*n)
    Space Complexity: O(target*n)
    """
    n = len(arr)
    t = [[0] * (target+1) for _ in range(n+1)]

    for i in range(n+1):
        t[i][0] = 1

    for i in range(1, n+1):
        for j in range(target+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][target]

arr = [28, 4, 3, 27, 0, 24, 26]
target = 24
print(perfectSum(arr, target))