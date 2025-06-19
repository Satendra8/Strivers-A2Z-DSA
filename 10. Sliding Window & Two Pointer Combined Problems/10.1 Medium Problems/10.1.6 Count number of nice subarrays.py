"""
Q. Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].


Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
"""


def numberOfSubarrays(nums, k):
    """
    Brute Force Approach
    1. generate all substr
    2. keep updating the odd count
    3. if odd_count == k then add to ans
    4. if odd_count exceeds then break
    Time Complexity: O(N^2)
    Space Complexity: O(N)
    """
    n = len(nums)
    ans = 0

    for i in range(n):
        odd_count = 0
        for j in range(i, n):
            if nums[j] % 2 == 1:
                odd_count += 1
            if odd_count == k:
                ans += 1
            if odd_count > k:
                break
    return ans


def countSubarrays(nums, k):
    if k < 0:
        return 0
    n = len(nums)
    left = 0
    odd_count = 0
    ans = 0
    for right in range(n):

        if nums[right] % 2 == 1:
            odd_count += 1

        while odd_count > k:
            if nums[left] % 2 == 1:
                odd_count -= 1
            left += 1
        if odd_count <= k:
            ans += right - left + 1
    return ans

#1+2+3+4+4 = 14
#1+2+3+3+3 = 12

def numberOfSubarraysOptimal(nums, k):
    """
    Optimal Approach
    1. break down problem in 2 parts
    2. count sub array count <= k and sub array count <= k - 1
    3. subtract both
    4. find subarray count <= k
        i. if count <= goal then count all possible subarrays (lenght of subarray)
    Time Complexity: O(2N+2N)
    Space Complexity: O(1)
    """
    return countSubarrays(nums, k) - countSubarrays(nums, k-1)

nums = [2,4,6]
k = 1
print(numberOfSubarraysOptimal(nums, k))


def count(nums, k):
    """
    Sliding Window
    Pattern: Atmost - Atleast
    Identification: not sure whether to move i or j
    Find for odd_count <= k then odd_count <= k-1, then subtract to get answer
    """
    n = len(nums)
    ans = 0
    i = 0
    j = 0
    odd_count = 0

    while j < n:
        if nums[j] % 2 == 1:
            odd_count += 1
        if odd_count > k:
            while odd_count > k:
                if nums[i] % 2 == 1:
                    odd_count -= 1
                i += 1
        ans += (j-i+1)
        j += 1
    return ans

def countSubarrays(nums, k):
    return count(nums, k) - count(nums, k-1)

nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(countSubarrays(nums, k))