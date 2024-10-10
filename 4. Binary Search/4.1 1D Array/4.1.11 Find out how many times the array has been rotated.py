"""
Q. Given an integer array arr of size N, sorted in ascending order (with distinct values). Now the array is rotated between 1 to N times which is unknown. Find how many times the array has been rotated. 

Example 1:
Input Format:
 arr = [4,5,6,7,0,1,2,3]
Result:
 4
Explanation:
 The original array should be [0,1,2,3,4,5,6,7]. So, we can notice that the array has been rotated 4 times.

Example 2:
Input Format:
 arr = [3,4,5,1,2]
Result:
 3
Explanation:
 The original array should be [1,2,3,4,5]. So, we can notice that the array has been rotated 3 times.
"""


def findKRotation(arr):
    """
    1. Optimal Approach
    2. Find the index of minimum number in order to find rotation count
    3. Same as previous problem, just need to track index variable
    4. Time Complexity: O(logN)
    5. Space Complexity: O(1)
    """
    n = len(arr)
    index = 0
    smallest = 2**31-1

    left = 0
    right = n - 1

    while left <= right:
        mid = (left+right) // 2
        if arr[mid] >= arr[left]:
            if arr[left] < smallest:
                smallest = arr[left]
                index = left
            left = mid + 1
        else:
            if arr[mid] < smallest:
                smallest = arr[mid]
                index = mid
            right = mid - 1
    return index



# [5,1,2,3,4]

arr = [4,5,6,7,0,1,2,3]
print(findKRotation(arr))

"""
arr = [4,5,6,7,0,1,2,3]  left=0, right=7, mid=3
                         left=4, right=7, mid=5
                         left=6, right=7, mid=6
                         left=7, right=7, mid=7
                         left=8, right=7, mid=7 stop iteration

smallest = 1
index = 4
"""