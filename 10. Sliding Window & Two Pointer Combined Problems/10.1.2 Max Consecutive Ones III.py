"""
Q. Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""

def longestOnes(nums, k):
    """
    Brute Force Approach
    1. find all possible substr which has atmost k 0
    2. keep updating counter and maxx
    Time Complexity: O(N^2)
    Space Complexity: O(N)
    """
    n = len(nums)
    temp = k
    j = 0
    maxx = 0

    for i in range(n):
        temp = k
        count = 0
        j = i
        while j < n and temp >= 0:
            if nums[j] == 0:
                temp -= 1
            if temp < 0:
                break
            j += 1
            count += 1
        maxx = max(maxx, count)
    return maxx


def longestOnesBetter(nums, k):
    """
    Better Approach
    1. use two pointer with sliding window
    2. if all k (utilized) then move the window
    3. move the window till one 0 released
    4. keep updating maxx
    Time Complexity: O(N)
    SPace Complexity: O(1)
    """
    n = len(nums)
    left = 0
    maxx = 0

    for right in range(n):
        if nums[right] == 0:
            k -= 1
        while k < 0:
            if nums[left] == 0:
                k += 1
            left += 1
        maxx = max(maxx, right - left + 1)

    return maxx



def longestOnesOptimal(nums, k):
    """
    Optimal Approach
    1. the basic idea is to move left poitner by only once
    2. keep counting zeros
    3. if zero exceeds k then move left pointer
    4. if any zero found on left decrease zero count
    5. update max only if zero count <= k
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n = len(nums)
    left = 0
    maxx = 0
    zeros = 0

    for right in range(n):
        if nums[right] == 0:
            zeros += 1

        if zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        if zeros <= k:
            maxx = max(maxx, right - left + 1)
    return maxx


nums = [1,1,1,0,0,0,1,1,1,1,0,0]
k = 2
print(longestOnesOptimal(nums, k))

"""
nums = [0,0,1,1,0,0,1,1,1,1,0]
k = 3


Optimal Approach
        0 1 2 3 4 5 6 7 8 9 10
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2


left = 5
right = 10
zeros = 2
maxx = 6





feeling lasy while dry run
not able to think which case will fail
"""