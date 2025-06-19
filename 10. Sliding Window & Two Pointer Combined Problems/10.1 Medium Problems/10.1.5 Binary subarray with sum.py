"""
Q. Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]


Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15
"""

def numSubarraysWithSum(nums, goal):
    """
    Brute Force Approach
    1. find all possible substr
    2. keep counting the sum
    3. if sum reaches goal count it
    4. if sum exceeds goal break
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    n = len(nums)
    counter = 0

    for i in range(n):
        summ = 0
        for j in range(i, n):
            summ += nums[j]
            if summ == goal:
                counter += 1
            if summ > goal:
                break
    return counter


def numSubarraysWithSumBetter(nums, goal):
    """
    use hash set
    keep adding and have a dict
    find required number dict, if found increase count

    wrong solution need revision
    """
    n = len(nums)
    d = {}
    counter = 0
    summ = 0

    for i in range(n):

        summ += nums[i]
        if (summ - goal) in d:
            counter += 1
        if summ == goal:
            counter += 1
        if summ not in d:
            d[summ] = i

    print(d)
    return counter


def countSubarray(nums, goal):
    if goal < 0:
        return 0
    n = len(nums)
    summ = 0
    left = 0
    counter = 0

    for right in range(n):
        summ += nums[right]
        while summ > goal:
            summ -= nums[left]
            left += 1
        if summ <= goal:
            counter += right - left + 1

    return counter


def numSubarraysWithSumOptimal(nums, goal):
    """
    Optimal Approach
    1. break down problem in 2 parts
    2. count sub array sum <= goal and sub array sum <= goal - 1
    3. subtract both
    4. find subarray sum <= goal
        i. if summ <= goal then count all possible subarrays (lenght of subarray)
    Time Complexity: O(2N+2N)
    Space Complexity: O(1)
    """
    return countSubarray(nums, goal) - countSubarray(nums, goal-1)


nums = [1,0,0,1,1,0]
goal = 2
print(numSubarraysWithSumOptimal(nums, goal))

"""
nums = [1,0,1,0,1]
goal = 2

counter = 3
summ = 1


"""


def atmostSum(arr, k):
    if k < 0:
        return 0
    n = len(arr)
    i = 0
    j = 0
    summ = 0
    cnt = 0

    while j < n:
        summ += arr[j]
        
        if summ > k:
            while summ > k:
                summ -= arr[i]
                i += 1
        cnt += (j-i+1)
        j += 1
    return cnt

        
def numberOfSubarrays(arr, target):
    """
    1. Sliding Window
    2. In normal sliding window - not sure whether to move i or move j
    3. finding the sum <= k
    4. then finding sum <= k-1, then subtracting both to find sum = k
    5. sliding window: consider the current element as last element and count all subarrays
        [1, 1, 0, 1, 1], for index=2, possible subarrays are 0, 10, 110 (all ending at 0)
    6. edge case: while doing k - 1, this can become negative so return 0 if negative
    Time Complexity: O(2N+2N)
    Space Complexity: O(1)
    """
    return atmostSum(arr, target) - atmostSum(arr, target-1)


arr = [1, 1, 0, 1, 1]
target = 5
print(numberOfSubarrays(arr, target))


"""
Sliding Window
Pattern: Atmost - Atleast
Identification: not sure whether to move i or j
Questions:
    1. Binary subarray with sum
    2. Count number of nice subarrays
    3. Number of substring containing all three characters
"""