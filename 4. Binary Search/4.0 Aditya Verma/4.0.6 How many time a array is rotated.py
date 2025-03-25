"""
Q. Given an increasing sorted rotated array arr of distinct integers. The array is right-rotated k times. Find the value of k.
Let's suppose we have an array arr = [2, 4, 6, 9], so if we rotate it by 2 times so that it will look like this:
After 1st Rotation : [9, 2, 4, 6]
After 2nd Rotation : [6, 9, 2, 4]

Examples:

Input: arr = [5, 1, 2, 3, 4]
Output: 1
Explanation: The given array is 5 1 2 3 4. The original sorted array is 1 2 3 4 5. We can see that the array was rotated 1 times to the right.
Input: arr = [1, 2, 3, 4, 5]
Output: 0
Explanation: The given array is not rotated.
"""


def findkRotation(arr):
    """
    1. no of rotation = index of min element
    2. if mid is smaller from left and right neighbour then return it
    3. min will always be present in unsorted part
    4. avoid index overflow while check prev and next
        i. prev = (mid - 1 + n) % n
        ii. next = (mid + 1) % n
    5. if arr already sorted return low
    """
    n = len(arr)

    low = 0
    high = n-1
    
    while low <= high:
        if arr[low] <= arr[high]:
            return low
        mid = (low+high) // 2
        prev = (mid - 1 + n) % n
        next = (mid + 1) % n
        if arr[prev] > arr[mid] and arr[next] > arr[mid]:
            return mid
        elif arr[low] <= arr[mid]:
            low = mid + 1
        elif arr[mid] <= arr[high]:
            high = mid - 1
    return 0

arr = [3,4,5,1,2]
print(findkRotation(arr))