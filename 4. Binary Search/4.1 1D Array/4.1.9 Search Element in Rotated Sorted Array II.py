"""
Q. Given an integer array arr of size N, sorted in ascending order (may contain duplicate values) and a target value k. Now the array is rotated at some pivot point unknown to you. Return True if k is present and otherwise, return False. 

Example 1:
Input Format:
 arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3
Result:
 True
Explanation:
 The element 3 is present in the array. So, the answer is True.

Example 2:
Input Format:
 arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 10
Result:
 False
Explanation:
 The element 10 is not present in the array. So, the answer is False.
"""

def search_element_2(nums, target):
    """
    1. Optimal Approach
    2. same as Search Element in Rotated Array
    3. [1,0,1,1,1] edge case is if arr[left] == arr[mid] == arr[right] then unable to find sorted part
    3. if arr[left] == arr[mid] == arr[right] then trim down search space left += 1, right -= 1
    5. Time Complexity: O(logN)
    6. Space Complexity: O(1)  
    
    """
    n = len(nums)
    left = 0
    right = n - 1
    
    while left <= right:
        mid = (left+right) // 2

        if nums[mid] == target:
            return True
        elif nums[left] == nums[right] == nums[mid]:
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]:
            if nums[left] <= target and nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target and nums[right] >= target:
                left = mid + 1
            else:
                right = mid - 1
    return False

nums = [1,0,1,1,1]
target = 0
print(search_element_2(nums, target))

"""
target=0
nums = [1,0,1,1,1] left=0, right=4, mid=2
                   left=1, right=3, mid=2
                   left=1, right=1, mid=1

                   
if arr[left] == arr[mid] == arr[right] then trim down search space left += 1, right -= 1
"""