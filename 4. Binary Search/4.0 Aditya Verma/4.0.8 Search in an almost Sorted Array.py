"""
Q. Given a sorted integer array arr[] consisting of distinct elements, where some elements of the array are moved to either of the adjacent positions, i.e. arr[i] may be present at arr[i-1] or arr[i+1].
Given an integer target.  You have to return the index ( 0-based ) of the target in the array. If target is not present return -1.

Examples:

Input: arr[] = [10, 3, 40, 20, 50, 80, 70], target = 40
Output: 2
Explanation: Index of 40 in the given array is 2.
Input: arr[] = [10, 3, 40, 20, 50, 80, 70], target = 90
Output: -1
Explanation: 90 is not present in the array.
Input: arr[] = [-20], target = -20
Output: 0
Explanation: -20 is the only element present in the array.
"""

def findTarget(arr, target):
    """
    1. check at mid, mid-1, mid+1 positions and if match return respective index
    2. if greater serch on left (end = mid - 2)
    3. if less serch on right (start = mid + 2)
    Time Complexity: O(logN)
    Space Complexity: O(logN)
    """
    n = len(arr)
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif mid-1 >= 0 and arr[mid-1] == target:
            return mid - 1
        elif mid+1 < n and arr[mid+1] == target:
            return mid+1
        elif arr[mid] > target:
            end = mid - 2
        else:
            start = mid + 2
    return -1

arr = [-20]
target = -20
print(findTarget(arr, target))