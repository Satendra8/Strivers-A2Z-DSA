"""
Q. Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""

def subsetSumRecursive(nums, target, n):
    if n == 0 and target == 0:
        return True

    if n == 0: return False
    if target == 0: return True

    if nums[n-1] <= target:
        return subsetSumRecursive(nums, target-nums[n-1], n-1) or subsetSumRecursive(nums, target, n-1)
    else:
        return subsetSumRecursive(nums, target, n-1)
    

def canPartitionRecursive(nums):
    """
    Similar to 0-1 Knapsack
    1. basic idea is if sum of all numbers is even then only we can partition
    2. now the problem is boiled down into subset sum problem
    3. here if i find subset sum for target//2 then my job is done
    Time Complexity: O(2^N)
    Space Complexity: O(N)
    """
    target = sum(nums)
    n = len(nums)
    if target % 2 == 1:
        return False
    
    return subsetSumRecursive(nums, target//2, n)


def subsetSumMemoization(nums, target, n, t):
    if n == 0 and target == 0:
        return True

    if n == 0: return False
    if target == 0: return True

    if t[n-1][target] != -1: return t[n-1][target]

    if nums[n-1] <= target:
        t[n-1][target] = subsetSumMemoization(nums, target-nums[n-1], n-1, t) or subsetSumMemoization(nums, target, n-1, t)
        return t[n-1][target]
    else:
        t[n-1][target] = subsetSumMemoization(nums, target, n-1, t)
        return t[n-1][target]
    
def canPartitionMemoization(nums):
    """
    Similar to 0-1 Knapsack
    1. basic idea is if sum of all numbers is even then only we can partition
    2. now the problem is boiled down into subset sum problem
    3. here if i find subset sum for target//2 then my job is done
    Time Complexity: O(2^N)
    Space Complexity: O(target * N)
    """
    target = sum(nums)
    n = len(nums)
    if target % 2 == 1:
        return False
    target = target // 2
    t = [[-1] * (target+1) for _ in range(n+1)]
    return subsetSumMemoization(nums, target, n, t)


def canPartition(nums):
    """
    Similar to 0-1 Knapsack
    1. basic idea is if sum of all numbers is even then only we can partition
    2. now the problem is boiled down into subset sum problem
    3. here if i find subset sum for target//2 then my job is done
    Time Complexity: O(target * N)
    Space Complexity: O(target * N)
    """
    target = sum(nums)
    n = len(nums)
    if target % 2 == 1:
        return False
    target = target // 2
    t = [[False] * (target+1) for _ in range(n+1)]

    for j in range(target+1):
        t[0][j] = False
    for i in range(n+1):
        t[i][0] = True

    for i in range(1, n+1):
        for j in range(1, target+1):
            if nums[i-1] <= j:
                t[i][j] = t[i-1][j-nums[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][target]


nums = [4,4,4,4,4,4,4,4,8,8,8,8,8,8,8,8,12,12,12,12,12,12,12,12,16,16,16,16,16,16,16,16,20,20,20,20,20,20,20,20,24,24,24,24,24,24,24,24,28,28,28,28,28,28,28,28,32,32,32,32,32,32,32,32,36,36,36,36,36,36,36,36,40,40,40,40,40,40,40,40,44,44,44,44,44,44,44,44,48,48,48,48,48,48,48,48,52,52,52,52,52,52,52,52,56,56,56,56,56,56,56,56,60,60,60,60,60,60,60,60,64,64,64,64,64,64,64,64,68,68,68,68,68,68,68,68,72,72,72,72,72,72,72,72,76,76,76,76,76,76,76,76,80,80,80,80,80,80,80,80,84,84,84,84,84,84,84,84,88,88,88,88,88,88,88,88,92,92,92,92,92,92,92,92,96,96,96,96,96,96,96,96,97,99]
print(canPartition(nums))