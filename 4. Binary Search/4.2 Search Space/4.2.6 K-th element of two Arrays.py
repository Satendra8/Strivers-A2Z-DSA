"""
Q. Given two sorted arrays a[] and b[] and an element k, the task is to find the element that would be at the kth position of the combined sorted array.

Examples :

Input: a[] = [2, 3, 6, 7, 9], b[] = [1, 4, 8, 10], k = 5
Output: 6
Explanation: The final combined sorted array would be [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th element of this array is 6.
Input: a[] = [100, 112, 256, 349, 770], b[] = [72, 86, 113, 119, 265, 445, 892], k = 7
Output: 256
Explanation: Combined sorted array is [72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892]. The 7th element of this array is 256.
"""

def kthElement(a, b, k):
    """
    Better Approach
    1. similar to merge array problem
    2. insted of storing in new array, counting here
    3. if the count becomes k, that's the required element
    Time Complexity: O(M+N)
    Space Complexity: O(1)
    """
    m = len(a)
    n = len(b)

    i = 0
    j = 0
    cnt = 0

    while i<m and j<n:
        if a[i] <= b[j]:
            val = a[i]
            i += 1
        else:
            val = b[j]
            j += 1
        cnt += 1

        if cnt == k:
            return val
    
    while i<m:
        cnt += 1
        if cnt == k:
            return a[i]
        i += 1

    while j<n:
        cnt += 1
        if cnt == k:
            return b[j]
        j += 1

    return -1


a = [100, 112, 256, 349, 770]
b = [72, 86, 113, 119, 265, 445, 892]
k = 7
print(kthElement(a, b, k))