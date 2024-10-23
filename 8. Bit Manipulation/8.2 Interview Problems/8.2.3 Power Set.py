"""
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

"""

def subsets(nums):
    """
    1. loop till 2^n
    2. loop over number bits and check set bits and form output
    3. if i & 1<<index (check set bits corresponding to each num of array)
    4. if bit is 1 at particular index, use that in ans
    5. Time Complexity: O(2^n * n)
    6. Space Complexity: O(N)
    """
    n = len(nums)
    final = []
    for i in range(0, 1<<n):
        arr = []
        for index, num in enumerate(nums):
            if i & 1<<index:
                arr.append(num)
        final.append(arr)
    return final

nums = [1,2,3]
print(subsets(nums))

"""
        0 1 2
nums = [1,2,3]

n = 3

000 => []
001 => [1] //element at index 0 is on
010 => [2]
011 => [1, 2]
100 => [3]
101 => [1, 3]
110 => [2, 3]
111 => [1, 2, 3]

1. loop till 2^n
2. loop over number bits and check set bits and form output
3. if i & 1<<index (check set bits corresponding to each num of array)
4. if bit is 1 at particular index, use that in ans
5. Time Complexity: O(2^n * n)
6. Space Complexity: O(N)



"""
