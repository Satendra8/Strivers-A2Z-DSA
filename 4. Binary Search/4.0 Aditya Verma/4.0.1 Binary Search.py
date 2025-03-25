"""
Q. Binary Search Algorithm
"""

def binarysearch(arr, k):
    """
    Binary Search
    1. if arr[mid] == k return index
    2. if arr[mid] > k, move left
    3. if arr[mid] < k, move right
    Time Complexity: O(logN)
    Space Complexity: O(1)
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return -1

arr = [1, 1, 1, 1, 2]
k = 1
print(binarysearch(arr, k))