"""
Q. Given an array arr[] containing integers and an integer k, your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. If there is no subarray with sum equal to k, return 0.

Examples:

Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
Output: 6
Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. The length of the longest subarray with a sum of 15 is 6.
Input: arr[] = [-5, 8, -14, 2, 4, 12], k = -5
Output: 5
Explanation: Only subarray with sum = -5 is [-5, 8, -14, 2, 4] of length 5.
Input: arr[] = [10, -10, 20, 30], k = 5
Output: 0
Explanation: No subarray with sum = 5 is present in arr[].
"""


def longestSubarray(arr, k):
    """
    Sliding Window Variable
    1. sum < k: keep adding
    2. sum == k: update length
    3. sum > k: subtract till sum > k
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n = len(arr)
    i = 0
    j = 0
    summ = 0
    ans = 0

    while j < n:
        summ += arr[j]
        if summ < k:
            j += 1
        elif summ == k:
            ans = max(j-i+1, ans)
            j += 1
        else:
            while summ > k and i < j:
                summ -= arr[i]
                i += 1
            if summ == k:
                ans = max(j-i+1, ans)
            j += 1
    return ans

arr = [4,1,1,1,2,3,5]
k = 5
print((longestSubarray(arr, k)))