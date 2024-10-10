"""
Q. Given an array, and an element num the task is to find if num is present in the given array or not. If present print the index of the element or print -1.

Example 1:
Input: arr[]= 1 2 3 4 5, num = 3
Output: 2
Explanation: 3 is present in the 2nd index

Example 2:
Input: arr[]= 5 4 3 2 1, num = 5
Output: 0
Explanation: 5 is present in the 0th index

"""

def linear_search(arr, num):
    N = len(arr)
    for i in range(N):
        if arr[i] == num:
            return i
    return -1

arr = [1,2,3,4,5]
num = 3
print("ans =>", linear_search(arr, num))