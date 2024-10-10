"""
Q. You are given a sorted array of integers and a target, your task is to search for the target in the given array. Assume the given array does not contain any duplicate numbers.

Let's say the given array is = {3, 4, 6, 7, 9, 12, 16, 17} and target = 6.

"""

def binary_search(arr, target):
    """
    1. Iterative Approach
    2. use left, right and mid, divide the array into 2 halves
    3. check target present in which half
    4. Time Complexity - O(logN)
    5. Space Complexity - O(1)
    """
    n = len(arr)
    left = 0
    right = n - 1

    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

arr = [3, 4, 6, 7, 9, 12, 16, 17]
target = 12
print(binary_search(arr, target))






def binary_search_recursive(arr, left, right, target):
    """
    1. Recursive Approach
    2. use left, right and mid, divide the array into 2 halves
    3. check target present in which half
    4. Time Complexity - O(logN)
    5. Space Complexity - O(1)
    """
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, left, mid-1, target)
    else:
        return binary_search_recursive(arr, mid+1, right, target)

print(binary_search_recursive(arr, 0, len(arr)-1, target))

"""
target = 6
arr = [3, 4, 6, 7, 9, 12, 16, 17], left=0, right=7, mid=3
arr = [3, 4, 6, 7] left=0, right=2, mid=1
arr = [6] left=2, right=2, mid=2

arr[2] is 6, so ans is 2


target = 3
arr = [3, 4, 6, 7, 9, 12, 16, 17], left=0, right=7, mid=3
arr = [3, 4, 6, 7] left=0, right=2, mid=1
arr = [3] left=0, right=0, mid=0

arr[0] is 3, so ans is 0

"""