"""
Q. Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3

Output: [1,2,3,4]

Example 2:

Input: arr = [1,1,2,3,4,5], k = 4, x = -1

Output: [1,1,2,3]
"""
import heapq
def findClosestElements(arr, k, x):
    """
    1. subtract x from all elements, use abs to get +ve
    2. to use as max heap use multiply with negative
    3. if 2 element tie up, means diff is same, take the one having smaller index
    4. keep removing if exceeds k
    5. at end pop remaining elements
    6. sort ans and return
    Time Complexity: O(nlogk)
    Space Complexity: O(k)
    """
    heap = []
    for index, num in enumerate(arr):
        heapq.heappush(heap, (-abs(x-num), -index))
        if len(heap) > k:
            heapq.heappop(heap)
    ans = []
    while heap:
        ans.append(arr[-heapq.heappop(heap)[1]])
    ans.sort()
    return ans


arr = [1,2,3,4,5]
k = 4
x = 3
print(findClosestElements(arr, k, x))