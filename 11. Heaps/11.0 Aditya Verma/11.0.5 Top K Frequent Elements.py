"""
Q. Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

import heapq
def topKFrequent(nums, k):
    """
    Using Heap
    1. find frequency using map
    2. using MIN HEAP
    3. push number and frequency in MIN heap
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
        heapq.heappush(heap, (val, key))
        if len(heap) > k:
            heapq.heappop(heap)
    ans = []
    while heap:
        ans.append(heapq.heappop(heap)[1])
    return ans

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))