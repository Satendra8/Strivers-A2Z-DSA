"""
Q. Given an array arr[] and an integer k where k is smaller than the size of the array, the task is to find the kth smallest element in the given array.

Follow up: Don't solve it using the inbuilt sort function.

Examples :

Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
Output:  7
Explanation: 3rd smallest element in the given array is 7.
Input: arr[] = [2, 3, 1, 20, 15], k = 4 
Output: 15
Explanation: 4th smallest element in the given array is 15.
"""

import heapq

def kthSmallest(arr, k):
    """
    1. identification: k, find kth smallest
    2. find Smallest ----> max heap used: remove the maximum element from top
    3. if heap exceeds k remove it, it will not contribute in ans
    4. heapq library uses construct min heap, so multiplying with (-)
    Time Complexity: O(nlogk)
    Space Complexity: O(k)
    """
    heap = []
    for num in arr:
        heapq.heappush(heap, -num)
        if len(heap) > k:
            heapq.heappop(heap)
    return - heapq.heappop(heap)

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kthSmallest(arr, k))