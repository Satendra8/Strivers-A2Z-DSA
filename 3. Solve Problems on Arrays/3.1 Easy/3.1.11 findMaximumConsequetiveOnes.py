"""
Q. Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.

Example 1:

Input: prices = {1, 1, 0, 1, 1, 1}

Output: 3

Explanation: There are two consecutive 1's and three consecutive 1's in the array out of which maximum is 3.

Input: prices = {1, 0, 1, 1, 0, 1} 

Output: 2

Explanation: There are two consecutive 1's in the array. 

"""


def fixMaxConsequtiveOnes(nums):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    
    counter = 0
    max_count = 0

    for i in nums:
        if i == 1:
            counter += 1
        else:
            max_count = max(counter, max_count)
            counter = 0
            
    max_count = max(max_count, counter)
    return max_count
    
arr = [1, 0, 1, 1, 0, 1]
print(fixMaxConsequtiveOnes(arr))