"""
Q. Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
"""

def singleNumber(nums):
    """
    1. Use XOR operator
    2. same number will be cancelled, unique will remain
    3. Time Complexity: O(N)
    4. Space Complexity: O(1)
    """
    ans = 0
    for i in nums:
        ans = ans ^ i
    return ans

nums = [2,2,1]
print(singleNumber(nums))