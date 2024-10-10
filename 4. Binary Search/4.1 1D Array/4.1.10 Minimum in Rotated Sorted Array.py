"""
Q. Given an integer array arr of size N, sorted in ascending order (with distinct values). Now the array is rotated between 1 to N times which is unknown. Find the minimum element in the array. 

Example 1:
Input Format:
 arr = [4,5,6,7,0,1,2,3]
Result:
 0
Explanation:
 Here, the element 0 is the minimum element in the array.

Example 2:
Input Format:
 arr = [3,4,5,1,2]
Result:
 1
Explanation:
 Here, the element 1 is the minimum element in the array.

"""

def find_minimum(nums):
    """
    1. Optimal Approach
    2. Same as Search Element Array
    3. Twist is smaller element is may or may not be on sorted half
    4. pick the smallest element from sorted part and look on other part
    5. Time Complexity: O(logN)
    6. Space Complexity: O(1)
    """
    smallest = 2**31-1
    n = len(nums)

    left = 0
    right = n - 1

    while left <= right:
        mid = (left+right) // 2
        
        if nums[mid] >= nums[left]:
            smallest = min(smallest, nums[left])
            left = mid + 1
        else:
            smallest = min(smallest, nums[mid])
            right = mid - 1
    return smallest

nums = [5,1,2,3,4]

print(find_minimum(nums))

"""
nums = [5,1,2,3,4] left=0, right=4, mid=2
                         left=0, right=1, mid=0
                         left=1, right=1, mid=1


"""



def find_minimum_optimized(nums):
    """
    1. More Optimized Approach
    2. Same as find minimum
    3. if arr[left] <= arr[mid] <= arr[right] then no need to furthur binary search, just take arr[left]
    5. Time Complexity: O(logN)
    6. Space Complexity: O(1)
    """
    smallest = 2**31-1
    n = len(nums)

    left = 0
    right = n - 1

    while left <= right:
        mid = (left+right) // 2
        
        if nums[left] <= nums[mid] and nums[mid] <= nums[right]:
            smallest = min(smallest, nums[left])
            break
        elif nums[mid] >= nums[left]:
            smallest = min(smallest, nums[left])
            left = mid + 1
        else:
            smallest = min(smallest, nums[mid])
            right = mid - 1
    return smallest

nums = [5,1,2,3,4]

print(find_minimum_optimized(nums))

"""
nums = [4,5,6,7,0,1,2,3] left=0, right=7, mid=3
                         left=4, right=7, mid=5
                         left=1, right=1, mid=1

smallest = 4


nums = [5,1,2,3,4]       left=0, right=4, mid=2
                         left=0, right=1, mid=0
                         left=1, right=1, mid=1

smallest = 1
"""