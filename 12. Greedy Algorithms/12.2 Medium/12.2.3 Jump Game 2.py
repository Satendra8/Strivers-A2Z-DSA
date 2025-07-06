"""
Q. You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
"""

def canJump(nums, ind, n, cnt):
    """
    Brute Force Approach (Recursion)
    1. Generate all possbilities
    2. and if we can reach to end
    3. draw full recursive tree
    Time COmplexity: O(N^N)
    Space Complexity: O(N)
    """

    if ind >= n-1:
        return cnt
    
    minn = 10**4 + 1
    for i in range(1, nums[ind]+1):
            minn = min(minn, canJump(nums, ind+i, n, cnt+1))
    return minn


def jump(nums):
    """
    Optimal Approach
    1. iterate till last-1
    2. keep a variable farthest to keep track for maximum index
    3. curr will be the index till that need to find maximum index
    4. if i is at curr need jump and increase the count
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n = len(nums)

    farthest = 0
    cnt = 0
    curr = 0

    for i in range(n-1):
        farthest = max(farthest, i+nums[i])

        if i == curr:
            curr = farthest
            cnt += 1
    return cnt



nums = [2,3,1,1,4]
print(jump(nums))


"""
        0 1 2 3 4
nums = [2,3,1,1,4]

farthest = 4
cnt = 2
curr = 4


"""

def jumpGame2(nums):
    """
    1. Greedy Approach
    2. Basic idea is from each group how farthest we can jump (BFS approach)
    3. slide the window l = r+1, r = farthest
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n = len(nums)
    ans = 0
    l = r = 0
    while r < n - 1:
        farthest = 0
        for i in range(l, r + 1):
            farthest = max(farthest, nums[i] + 1)
        l = r + 1
        r = farthest
        ans += 1
    return ans