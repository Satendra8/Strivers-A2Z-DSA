"""
Q. Given a sorted array of N integers and an integer x, write a program to find the upper bound of x.

Example 1:
Input Format:
 N = 4, arr[] = {1,2,2,3}, x = 2
Result:
 3
Explanation:
 Index 3 is the smallest index such that arr[3] > x.

Example 2:
Input Format:
 N = 6, arr[] = {3,5,8,9,15,19}, x = 9
Result:
 4
Explanation:
 Index 4 is the smallest index such that arr[4] > x.
"""


def upper_bound(arr, x):
    """
    1. Brute Force Approach
    2. Linear Approach
    3. Keep checking if there is number exist > x and return if found
    4. Time Complexity - O(N)
    5. Space Complecity - O(1)
    """
    n = len(arr)

    for i in range(n):
        if arr[i] > x:
            return i
    return n


arr = [1,2,2,3]
x = 2
print(upper_bound(arr, x))


def upper_bound(arr, x):
    """
    1. Optimal Approach
    2. Use Binary Search
    3. check if a number exist > x, this can be a possible answer
    4. check for other posibilities
    4. Time Complexity - O(logN)
    5. Space Complecity - O(1)
    """
    n = len(arr)

    upper = n
    left = 0
    right = n-1

    while left <= right:
        mid = (left+right) // 2
        if arr[mid] > x:
            upper = mid
            right = mid-1
        else:
            left = mid+1
    return upper

arr = [1,2,2,3]
x = 1
print(upper_bound(arr, x))