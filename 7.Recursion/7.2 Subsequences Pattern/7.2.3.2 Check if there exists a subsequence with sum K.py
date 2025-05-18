"""
Q. Given an array arr and target sum k, check whether there exists a subsequence such that the sum of all elements in the subsequence equals the given target sum(k).

Example:

Input:  arr = [10,1,2,7,6,1,5], k = 8.
Output:  Yes
Explanation:  Subsequences like [2, 6], [1, 7] sum upto 8

Input:  arr = [2,3,5,7,9], k = 100. 
Output:  No
Explanation:  No subsequence can sum upto 100
"""

def solve(arr, index, output, n, k):
    """
    1. use IP-OP method
    2. either consider the element either not
    3. base condition: if at leaf node, output matches with k, return True otherwise False
    4. return true if any true found
    """
    if index == n:
        if output == k:
            return True
        return False
    
    return solve(arr, index+1, output, n, k) or solve(arr, index+1, output+arr[index], n, k)

arr = [2,3,5,7,9]
k = 100.
n = len(arr)
print(solve(arr, 0, 0, n, k))


# use DP for optimal Approach