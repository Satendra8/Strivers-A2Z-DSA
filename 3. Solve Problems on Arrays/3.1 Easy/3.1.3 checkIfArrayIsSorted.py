"""
Q. Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.

Note: Two consecutive equal values are considered to be sorted.

Example 1:
Input: N = 5, array[] = {1,2,3,4,5}
Output: True.
Explanation: The given array is sorted i.e Every element in the array is smaller than or equals to its next values, So the answer is True.

Example 2:
Input: N = 5, array[] = {5,4,6,7,8}
Output: False.
Explanation: The given array is Not sorted i.e Every element in the array is not smaller than or equal to its next values, So the answer is False.

Here element 5 is not smaller than or equal to its future elements.

"""

def checkSorted(arr):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(arr)
    # single element case
    if n==1:
        return True
    # check ascending and descending
    ascending = True
    if arr[0] > arr[1]:
        ascending = False
    
    for i in range(0, n-1):
        if ascending:
            if arr[i] > arr[i+1]:
                return False
        else:
            if arr[i] < arr[i+1]:
                return False
            
    return True

print(checkSorted([2,1]))