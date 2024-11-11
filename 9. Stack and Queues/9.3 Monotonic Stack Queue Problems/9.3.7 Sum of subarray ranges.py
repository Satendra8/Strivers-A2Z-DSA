"""
You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:

Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
Example 2:

Input: nums = [1,3,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
Example 3:

Input: nums = [4,-2,-3,4,1]
Output: 59
Explanation: The sum of all subarray ranges of nums is 59.
"""

def subArrayRanges(nums):
    """
    Brute Force Approach
    """
    summ = 0
    n = len(nums)

    for i in range(n):
        minn = 10**9
        maxx = -10**9
        for j in range(i, n):
            minn = min(minn, nums[j])
            maxx = max(maxx, nums[j])
            summ += (maxx - minn)
    return summ



def prevSmallerElement(nums, n):
    stack = []
    ans = [-1]*n

    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(i)
    return ans


def nextSmallerElement(nums, n):
    stack = []
    ans = [n]*n

    for i in range(n-1, -1, -1):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(i)
    return ans


def minimumSubarraySum(nums, n):
    summ = 0

    prevArr = prevSmallerElement(nums, n)
    nextArr = nextSmallerElement(nums, n)

    for i in range(n):
        prev = i - prevArr[i]
        next = nextArr[i] - i
        summ += (prev * next * nums[i])
    return summ


def prevLargerElement(nums, n):
    stack = []
    ans = [-1]*n

    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(i)
    return ans

def nextLargerElement(nums, n):
    stack = []
    ans = [n]*n

    for i in range(n-1, -1, -1):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(i)
    return ans

def maximumSubarraySum(nums, n):
    summ = 0

    prevArr = prevLargerElement(nums, n)
    nextArr = nextLargerElement(nums, n)
    print(prevArr, nextArr)

    for i in range(n):
        prev = i - prevArr[i]
        next = nextArr[i] - i
        summ += (prev * next * nums[i])
    return summ


def subArrayRangesOptimal(nums):
    """
    1. Find sum of subarray minimum
        i. find prev smaller element
        ii. find next smaller element
        iii. prev * next * num (will get individual contribution)
    2. Find sum of subarray maximum
        i. find prev larger element
        ii. find next larger element
        iii. prev * next * num (will get individual contribution)
    3. do maximum sum - minimum sum
    Time Complexity: O(3N+3N)
    Space Complexity: O(4N+4N)
    """
    n = len(nums)
    return maximumSubarraySum(nums, n) - minimumSubarraySum(nums, n)


nums = [4,-2,-3,4,1]
print(subArrayRangesOptimal(nums))


"""
1. Find sum of subarray minimum
    i. find prev smaller element
    ii. find next smaller element
    iii. prev * next * num (will get individual contribution)
2. Find sum of subarray maximum
    i. find prev larger element
    ii. find next larger element
    iii. prev * next * num (will get individual contribution)
3. do maximum sum - minimum sum

"""