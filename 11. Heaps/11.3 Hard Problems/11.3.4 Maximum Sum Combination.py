"""
Given two integer array A and B of size N each.
A sum combination is made by adding one element from array A and another element of array B.
Return the maximum K valid sum combinations from all the possible sum combinations.

Note : Output array must be sorted in non-increasing order.

Example 1:

Input:
N = 2
K = 2
A [ ] = {3, 2}
B [ ] = {1, 4}
Output: {7, 6}
Explanation: 
7 -> (A : 3) + (B : 4)
6 -> (A : 2) + (B : 4)
Example 2:

Input:
N = 4
K = 3
A [ ] = {1, 4, 2, 3}
B [ ] = {2, 5, 1, 6}
Output: {10, 9, 9}
Explanation: 
10 -> (A : 4) + (B : 6)
9 -> (A : 4) + (B : 5)
9 -> (A : 3) + (B : 6)
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxCombinations() which takes the interger N,integer K and two integer arrays A [ ] and B [ ] as parameters and returns the maximum K valid distinct sum combinations .
"""
import heapq

def maxCombinationsBrute(N, K, A, B):
    """
    1. Use Min Heap
    2. Generate all possible combination sum
    3. Insert in heap and pop if k exceeds
    Time Complexity: O(N*N) + NlogK
    Space COmplexity: O(K)
    """
    heap = []
    maxA = max(A)
    for i in range(N):
        for j in range(N):
            heapq.heappush(heap, A[i]+B[j])
            if len(heap) > K:
                heapq.heappop(heap)
    
    ans = []
    while heap:
        ans.append(heapq.heappop(heap))
    ans.reverse()
    return ans



def maxCombinations(N, K, A, B):
    """
    1. use Min Heap
    2. sort both array
    3. similar to brute force but break loop if top of the heap has greater element than A[i]+B[j]
    Time Complexity: O(N^2logK) in worst case
    Space Complexity: O(K)
    """
    A.sort()
    B.sort()
    i = N-1
    heap = []

    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            if len(heap) < K:
                heapq.heappush(heap, A[i]+B[j])
            else:
                if heap[0] >= A[i]+B[j]:
                    break
                heapq.heappop(heap)
                heapq.heappush(heap, A[i]+B[j])
    ans = []
    while heap:
        ans.append(heapq.heappop(heap))
    ans.reverse()
    return ans



N = 7
K = 4
A = [9, 9, 10, 6, 1, 6, 4]
B = [5, 3, 4, 2, 10, 4, 9]
print(maxCombinations(N, K, A, B))