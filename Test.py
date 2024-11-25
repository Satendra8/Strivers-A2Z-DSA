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