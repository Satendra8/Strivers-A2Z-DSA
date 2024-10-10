"""
Q. You are given a sorted array containing N integers and a number X, you have to find the occurrences of X in the given array.

Example 1:
Input:
 N = 7,  X = 3 , array[] = {2, 2 , 3 , 3 , 3 , 3 , 4}
Output
: 4
Explanation:
 3 is occurring 4 times in 
the given array so it is our answer.

Example 2:
Input:
 N = 8,  X = 2 , array[] = {1, 1, 2, 2, 2, 2, 2, 3}
Output
: 5
Explanation:
 2 is occurring 5 times in the given array so it is our answer.
"""

def last_occurance(arr, n, x):
    left = 0
    right = n - 1
    last = -1
    # last occurance
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] > x:
            right = mid-1
        else:
            if arr[mid] == x:
                last = mid
            left = mid+1
    return last


def first_occurance(arr, n, x):
    left = 0
    right = n - 1
    first = -1
    # first occurance
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] >= x:
            if arr[mid] == x:
                first = mid
            right = mid-1
        else:
            left = mid+1
    return first


def count_occurances(arr, n, x):
    """
    1. Optimal Approach
    2. find the fist occurance
    3. find the last occurance
    4. calculate last - first + 1
    5. Time Complexity: O(logN)
    6. Space Complexity: O(1)
    """
    first = first_occurance(arr, n, x)
    last = last_occurance(arr, n, x)
    if first > -1 and last > -1:
        return last - first + 1
    return 0


arr = [10,11]
x = 10
n = 2
print(count_occurances(arr, n, x))