"""
Q. Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:
s
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

"""





def findMissingPositive(arr):
    """
    Time Complexity : O(n)
    Space Complexity : O(1)
    
    1. move all childrens to its right chair (do correct swapping)
    2. retain the cursor until the correct student sit.
    3. iterate over loop and find missing
    4. return n+1 if no element found
    
    
    """
    n = len(arr)
    for i in range(n):
        while 1<=arr[i] <= n and arr[i] != arr[arr[i] -1]:
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]

    for i in range(n):
        if arr[i] != i+1:
            return i+1
    return n+1

arr = [3,4,-1,1]
print(findMissingPositive(arr))




def findMissingBetter(arr):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(arr)
    new_set = set(arr)
    
    for i in range(1, n+1):
        if i not in new_set:
            return i

    return n+1