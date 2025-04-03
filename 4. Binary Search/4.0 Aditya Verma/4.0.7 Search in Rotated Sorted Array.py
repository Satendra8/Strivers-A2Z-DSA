"""
Q. There is an integer array arr sorted in ascending order (with distinct values).

Prior to being passed to your function, arr is possibly rotated at an unknown pivot index k (1 <= k < arr.length) such that the resulting array is [arr[k], arr[k+1], ..., arr[n-1], arr[0], arr[1], ..., arr[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array arr after the possible rotation and an integer key, return the index of key if it is in arr, or -1 if it is not in arr.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: arr = [4,5,6,7,0,1,2], key = 0
Output: 4
Example 2:

Input: arr = [4,5,6,7,0,1,2], key = 3
Output: -1
Example 3:

Input: arr = [1], key = 0
Output: -1
"""

def findMinIndex(arr):
    n = len(arr)

    low = 0
    high = n - 1

    while low <= high:
        if arr[low] <= arr[high]:
            return low
        mid = (low + high) // 2
        prev = (mid - 1 + n) % n
        next = (mid + 1) % n
        if arr[mid] < arr[prev] and arr[mid] < arr[next]:
            return mid
        elif arr[low] <= arr[mid]:
            low = mid + 1
        elif arr[mid] <= arr[high]:
            high = mid - 1
    return 0


def binarySearch(arr, low, high, key):
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def search(arr, key):
    """
    1. find min index (pivot), break arr into 2 part then do binary search
    2. find element in left part (binary search)
    3. find element in right part (binary search)
    4. if not found both side return -1
    """
    pivot = findMinIndex(arr)

    print(pivot)
    if arr[pivot] == key:
        return pivot
    left = binarySearch(arr, 0, pivot - 1, key)
    right = binarySearch(arr, pivot + 1, len(arr) - 1, key)

    if left == -1 and right == -1:
        return -1

    if left == -1:
        return right
    else:
        return left


arr = [2,3,4,5,1]
key = 1
print(search(arr, key))







