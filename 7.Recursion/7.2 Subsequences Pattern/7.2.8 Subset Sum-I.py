"""
Q. Given an array print all the sum of the subset generated from it, in the increasing order.

Example 1:

Input: N = 3, arr[] = {5,2,1}

Output: 0,1,2,3,5,6,7,8

Explanation: We have to find all the subset’s sum and print them.in this case the generated subsets are [ [], [1], [2], [2,1], [5], [5,1], [5,2]. [5,2,1],so the sums we get will be  0,1,2,3,5,6,7,8


Input: N=3,arr[]= {3,1,2}

Output: 0,1,2,3,3,4,5,6

Explanation: We have to find all the subset’s sum and print them.in this case the generated subsets are [ [], [1], [2], [2,1], [3], [3,1], [3,2]. [3,2,1],so the sums we get will be  0,1,2,3,3,4,5,6
"""


def subsetSum(arr, index, ans, n, l):
    """
    1. base case: if index exceeds add it to the ans (ans is at leaf node)
    2. pick and add it to ans
    3. not pick
    4. Time Complexity: O(2^n)
    5. Space Complexity: O(2^n)
    """
    if index >= n:
        l.append(ans)
        return

    #pick
    subsetSum(arr, index+1, ans+arr[index], n, l)
    #not pick
    subsetSum(arr, index+1, ans, n, l)
    return

arr = [1,2,1]
n = 3
l = []
subsetSum(arr, 0, 0, n, l)
print(l)
