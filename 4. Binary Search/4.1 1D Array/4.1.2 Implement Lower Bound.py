"""
Q. Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.

Example 1:
Input Format:
 N = 4, arr[] = {1,2,2,3}, x = 2
Result:
 1
Explanation:
 Index 1 is the smallest index such that arr[1] >= x.

Example 2:
Input Format:
 N = 5, arr[] = {3,5,8,15,19}, x = 9
Result:
 3
Explanation:
 Index 3 is the smallest index such that arr[3] >= x.
"""

def lower_bound(arr, x):
    """
    1. Brute Force Approach
    2. Linear Approach
    3. Keep checking if there is number exist >= x
    4. Time Complexity - O(N)
    5. Space Complecity - O(1)
    """
    n = len(arr)
    lower_bound = n

    for i in range(n):
        if arr[i] >= x:
            lower_bound = i
            break
    return lower_bound


arr = [3,5,8,15,19]
x = 9
print(lower_bound(arr, x))



def lower_bound(arr, x):
    """
    1. Optimal Approach
    2. Use Binary Search
    3. check if a number exist >= x, this can be a possible answer
    4. check for other posibilities
    4. Time Complexity - O(logN)
    5. Space Complecity - O(1)
    """
    n = len(arr)
    left = 0
    right = n - 1
    lower = n

    while left <= right:
        mid = (left+right) // 2
        if arr[mid] >= x:
            lower = mid
            right = mid - 1
        else:
            left = mid + 1
    return lower

arr = [1,2,2,3]
x = 2
print(lower_bound(arr, x))


"""
arr = [3,5,8,15,19] left=0, right=4, mid=2
arr=[15, 19] left=3, right=4, mid=3
arr=[15, 19] left=4, right=4, mid=4

"""