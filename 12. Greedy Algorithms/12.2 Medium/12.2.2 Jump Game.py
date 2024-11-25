"""
Q. You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""

def canJump(nums, ind, n):
    """
    Brute Force Approach (Recursion)
    1. Generate all possbilities
    2. and if we can reach to end
    Time COmplexity: O(N^N)
    Space Complexity: O(N)
    """

    if ind == n-1:
        return True
    
    for i in range(1, nums[ind]+1):
        if ind+i < n:
            if canJump(nums, ind+i, n):
                return True
    return False


def canJumpBetter(nums):
    """
    Better Approach
    1. basic idea: move the goal toward left
    2. iterate from last
    3. check if element reach to goal then that is the new goal
    4. if at the end goal becomes 0 return true
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n = len(nums)

    goal = n - 1
    for i in range(n-2, -1, -1):
        if i+nums[i] >= goal:
            goal = i
    return goal == 0



def canJumpOptimal(nums):
    """
    Optimal Approach (Greedy Algorithm)
    1. keep consider maximum jump by moving 1 step each time
    2. if moved at maximum index but maxInd is less then no possible ways return false
    3. if reached at last index or more than last index return true
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n = len(nums)
    maxInd = 0

    for i in range(n):
        if i > maxInd:
            return False
    
        if maxInd >= n-1:
            return True
        maxInd = max(maxInd, i+nums[i])
        
    return False


nums = [1,2,4,1,1,0,2,5]
n = len(nums)
print(canJumpBetter(nums))