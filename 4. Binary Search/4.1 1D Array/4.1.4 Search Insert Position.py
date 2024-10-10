"""
Q. You are given a sorted array arr of distinct values and a target value x. You need to search for the index of the target value in the array.

If the value is present in the array, then return its index. Otherwise, determine the index where it would be inserted in the array while maintaining the sorted order.

Example 1:
Input Format: arr[] = {1,2,4,7}, x = 6
Result: 3
Explanation: 6 is not present in the array. So, if we will insert 6 in the 3rd index(0-based indexing), the array will still be sorted. {1,2,4,6,7}.

Example 2:
Input Format: arr[] = {1,2,4,7}, x = 2
Result: 1
Explanation: 2 is present in the array and so we will return its index i.e. 1.
"""

def insert_position(nums, target):
    """
    1. Optimal Approach
    2. Same as Lower Bound Approach
    3. check if a number exist >= x, this can be a possible answer
    4. check for other posibilities
    4. Time Complexity - O(logN)
    5. Space Complecity - O(1)
    """
    n = len(nums)
    lower = n
    left = 0
    right = n-1

    while left <= right:
        mid = (left+right) // 2
        if nums[mid] >= target:
            lower = mid
            right = mid-1
        else:
            left = mid+1
    return lower

nums = [1,3,5,6]
target = 7
print(insert_position(nums, target))