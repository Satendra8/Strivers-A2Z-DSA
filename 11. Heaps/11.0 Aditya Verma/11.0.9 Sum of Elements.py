"""
Given an array A[] of N positive integers and two positive integers K1 and K2. Find the sum of all elements between K1th and K2th smallest elements of the array. It may be assumed that (1 <= k1 < k2 <= n).

Example 1:

Input:
N  = 7
A[] = {20, 8, 22, 4, 12, 10, 14}
K1 = 3, K2 = 6
Output:
26
Explanation:
3rd smallest element is 10
6th smallest element is 20
Element between 10 and 20 
12,14. Their sum = 26.
 
Example 2:

Input
N = 6
A[] = {10, 2, 50, 12, 48, 13}
K1= 2, K2 = 6
Output:
73
"""
import heapq

def kthSmallest(A, K):
    heap = []
    for num in A:
        heapq.heappush(heap, -num)
        if len(heap) > K:
            heapq.heappop(heap)
    return -heapq.heappop(heap)

def sumBetweenTwoKth(A, N, K1, K2):
    """
    Heap Variation: Use MAX HEAP
    1. find K1th smallest element
    2. find K2th smallest element
    3. Traverse the array and add up number b/w K1th and K2th
    Time Complexity: O(NlogK)
    Space Complexity: O(k)
    """
    first = kthSmallest(A, K1)
    second = kthSmallest(A, K2)

    ans = 0
    for num in A:
        if num > first and num < second:
            ans += num
    return ans

N  = 7
A = [10, 2, 50, 12, 48, 13]
K1 = 2
K2 = 6

print(sumBetweenTwoKth(A, N, K1, K2))