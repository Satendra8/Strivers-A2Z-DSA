"""
Q. Given an array arr[], where each element is at most k away from its target position, you need to sort the array optimally.
Note: You need to change the given array arr[] in place.

Examples:

Input: arr[] = [6, 5, 3, 2, 8, 10, 9], k = 3
Output: [2, 3, 5, 6, 8, 9, 10]
Explanation: The sorted array will be 2 3 5 6 8 9 10
Input: arr[]= [1, 4, 5, 2, 3, 6, 7, 8, 9, 10], k = 2
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Explanation: The sorted array will be 1 2 3 4 5 6 7 8 9 10
"""
import heapq
def nearlySorted(arr, k):
    """
    1. expected element is k position left or right
    2. use min heap in range k
    3. pop the smallest element if len exceeds k
    4. at end pop all elements
    Time Complexity: O(nlogk)
    Space Complexity: O(n)
    """
    heap = []
    ans = []
    for num in arr:
        heapq.heappush(heap, num)
        if len(heap) > k:
            ans.append(heapq.heappop(heap))
    while heap:
        ans.append(heapq.heappop(heap))
    arr[:] = ans
    return arr

arr = [6, 5, 3, 2, 8, 10, 9]
k = 3
nearlySorted(arr, k)
print(arr)