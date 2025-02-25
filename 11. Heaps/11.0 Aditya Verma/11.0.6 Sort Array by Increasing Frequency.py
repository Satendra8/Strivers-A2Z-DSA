"""
Q. Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
Example 3:

Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]
"""

import heapq
def frequencySort(nums):
    """
    Using Heap
    1. find frequency using map
    2. using MIN HEAP
    3. push number and frequency in MIN heap
    4. here k is not given no need to pop
    5. pop element and multiply by its frequency
    Time Complexity: O(nlogk)
    Space Complexity: O(n)
    """
    mp = dict()
    for num in nums:
        if num in mp:
            mp[num] += 1
        else:
            mp[num] = 1
    
    heap = []
    for key, val in mp.items():
        heapq.heappush(heap, (val, -key))
    ans = []
    while heap:
        freq, num = heapq.heappop(heap)
        num = -num
        ans.extend([num]*freq)
    return ans

nums = [2,3,1,3,2]
print(frequencySort(nums))