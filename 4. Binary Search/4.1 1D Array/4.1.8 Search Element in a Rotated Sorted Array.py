"""
Q. Given an integer array arr of size N, sorted in ascending order (with distinct values) and a target value k. Now the array is rotated at some pivot point unknown to you. Find the index at which k is present and if k is not present return -1.

Example 1:
Input Format: arr = [4,5,6,7,0,1,2,3], k = 0
Result: 4
Explanation: Here, the target is 0. We can see that 0 is present in the given rotated sorted array, nums. Thus, we get output as 4, which is the index at which 0 is present in the array.

Example 2:
Input Format: arr = [4,5,6,7,0,1,2], k = 3
Result: -1
Explanation: Here, the target is 3. Since 3 is not present in the given rotated sorted array. Thus, we get the output as -1.
"""


def search_element(arr, k):
    """
    1. Optimal Approach
    2. check if first half is sorted arr[left] <= arr[mid]
    3. if it is sorted and arr[left] <= k >= arr[mid] eliminate second half right=mid-1
    4. if not sorted then second half will be sorted check arr[mid] <= k >= arr[right] eliminate half left=mid+1
    5. Time Complexity: O(logN)
    6. Space Complexity: O(1)   
    """
    n = len(arr)
    left = 0
    right = n -1


    while left <= right:
        mid = (left+right) // 2

        if arr[mid] == k:
            return mid
        elif arr[left] <= arr[mid]:
            #left part is sorted
            if arr[left] <= k and arr[mid] >= k:
                right = mid - 1
            else:
                left = mid + 1
        else:
            #right part is sorted
            if arr[mid] <= k and arr[right] >= k:
                left = mid + 1
            else:
                right = mid - 1

    return -1

arr = [6,7,0,1,2,3,4,5]
k = 5
print(search_element(arr, k))

"""
arr = [4,5,6,7,0,1,2,3] left=0, right=7, mid=3 check arr[left] <= k >= arr[mid]
arr = [4,5,6,7,0,1,2,3] left=4, right=7, mid=5
arr = [4,5,6,7,0,1,2,3] left=4, right=4, mid=4, matched


arr = [6,7,0,1,2,3,4,5] left=0, right=7, mid=3 check if arr[left] <= arr[mid] then check arr[left] <= k >= arr[mid]
"""
