"""
Q. Find first and last occurance of an element.
"""

def binarysearch(arr, k):
    """
    Binary Search
    1. if arr[mid] == k, move left to find first occurence
    2. if arr[mid] > k, move left
    3. if arr[mid] < k, move right
    Time Complexity: O(logN)
    Space Complexity: O(1)
    """
    low = 0
    high = len(arr) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == k:
            ans = mid
            high = mid - 1
        elif arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return ans

arr = [1, 1, 1, 1, 2]
k = 1
print(binarysearch(arr, k))