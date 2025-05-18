"""
Q. Given an array nums and an integer k.Return the number of non-empty subsequences of nums such that the sum of all elements in the subsequence is equal to k.


Examples:
Input : nums = [4, 9, 2, 5, 1] , k = 10

Output : 2

Explanation : The possible subsets with sum k are [9, 1] , [4, 5, 1].

Input : nums = [4, 2, 10, 5, 1, 3] , k = 5

Output : 3

Explanation : The possible subsets with sum k are [4, 1] , [2, 3] , [5].
"""

def solve(arr, index, output, n, k):
    """
    1. use IP-OP method
    2. either consider the element either not
    3. base condition: if at leaf node, output matches with k, add it up
    4. sum all the counts and return
    """
    if index == n:
        if output == k:
            return 1
        return 0
    
    l = solve(arr, index+1, output, n, k)
    r = solve(arr, index+1, output+arr[index], n, k)
    return l + r

arr = [4, 2, 10, 5, 1, 3]
k = 5
n = len(arr)
print(solve(arr, 0, 0, n, k))