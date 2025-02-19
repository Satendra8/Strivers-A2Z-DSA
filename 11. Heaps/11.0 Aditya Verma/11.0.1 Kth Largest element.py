"""
Q. Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""

import heapq
def findKthLargest(nums, k):
    """
    1. identification: k, find kth largest
    2. find Largest ----> min heap used: remove the minimum element from top
    3. if heap exceeds k remove it, it will not contribute in ans
    Time Complexity: O(nlogk)
    Space Complexity: O(k)
    """
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heapq.heappop(heap)

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(findKthLargest(nums, k))