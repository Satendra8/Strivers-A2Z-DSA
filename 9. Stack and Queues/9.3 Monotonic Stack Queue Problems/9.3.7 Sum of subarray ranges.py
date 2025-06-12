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


def NGR(arr, n):
    stack = []
    ans = []

    for i in range(n-1, -1, -1):
        if not stack:
            ans.append(n-i)
        elif arr[i] < stack[-1][0]:
            ans.append(stack[-1][1] - i)                                                                       
        else:
            while stack and arr[i] >= stack[-1][0]:
                stack.pop()
            if not stack:
                ans.append(n-i)
            else:
                ans.append(stack[-1][1] - i)
        stack.append((arr[i], i))
    ans.reverse()
    return ans

  
def NGL(arr, n):
    stack = []
    ans = []

    for i in range(n):
        if not stack:
            ans.append(i-(-1))
        elif arr[i] <= stack[-1][0]:
            ans.append(i - stack[-1][1])
        else:
            while stack and arr[i] > stack[-1][0]:
                stack.pop()
            if not stack:
                ans.append(i-(-1))
            else:
                ans.append(i - stack[-1][1])
        stack.append((arr[i], i))
    return ans


def NSR(arr, n):
    stack = []
    ans = []

    for i in range(n-1, -1, -1):
        if not stack:
            ans.append(n-i)
        elif arr[i] > stack[-1][0]:
            ans.append(stack[-1][1] - i)
        else:
            while stack and arr[i] <= stack[-1][0]:
                stack.pop()
            if not stack:
                ans.append(n-i)
            else:
                ans.append(stack[-1][1] - i)
        stack.append((arr[i], i))
    ans.reverse()
    return ans

  
def NSL(arr, n):
    stack = []
    ans = []

    for i in range(n):
        if not stack:
            ans.append(i-(-1))
        elif arr[i] >= stack[-1][0]:
            ans.append(i - stack[-1][1])
        else:
            while stack and arr[i] < stack[-1][0]:
                stack.pop()
            if not stack:
                ans.append(i-(-1))
            else:
                ans.append(i - stack[-1][1])
        stack.append((arr[i], i))
    return ans


def subarray(arr):
    """
    edge case: if duplicate elements count them while finding NGL and NSL
    """
    n = len(arr)

    next_largest = NGR(arr, n)
    prev_largest = NGL(arr, n)

    next_smallest = NSR(arr, n)
    prev_smallest = NSL(arr, n)

    greater = 0
    smaller = 0

    for i in range(n):
        greater += next_largest[i] * prev_largest[i] * arr[i]
        smaller += next_smallest[i] * prev_smallest[i] * arr[i]

    return greater - smaller

nums = [4,-2,-3,4,1]
print(subarray(nums))