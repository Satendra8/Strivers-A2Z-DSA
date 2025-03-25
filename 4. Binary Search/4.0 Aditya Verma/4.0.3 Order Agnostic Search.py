"""
Q. Array is sorted either in ASC/DESC order.

"""

def binarysearchASC(arr, k):
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

def binarysearchDESC(arr, k):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def binarysearch(arr, k):
    """
    Binary Search
    1. if single element then just compare
    2. arr[0] > arr[1], binarysearch DESC
    3. arr[0] > arr[1], binarysearch ASC
    Time Complexity: O(logN)
    Space Complexity: O(1)
    """

    if len(arr) == 1:
        if arr[0] == k:
            return 0
        else:
            return -1
    
    if arr[0] > arr[1]:
        return (arr, k)
    return binarysearchASC(arr, k)

arr = [6,5,4,3,2,1]
k = 10
print(binarysearch(arr, k))