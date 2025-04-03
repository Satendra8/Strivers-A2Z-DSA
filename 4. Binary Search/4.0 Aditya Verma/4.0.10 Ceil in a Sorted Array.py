"""
Q. Given a sorted array arr[] and an integer x, find the index (0-based) of the smallest element in arr[] that is greater than or equal to x. This element is called the ceil of x. If such an element does not exist, return -1.

Note: In case of multiple occurrences of ceil of x, return the index of the first occurrence.

Examples

Input: arr[] = [1, 2, 8, 10, 11, 12, 19], x = 5
Output: 2
Explanation: Smallest number greater than 5 is 8, whose index is 2.
Input: arr[] = [1, 2, 8, 10, 11, 12, 19], x = 20
Output: -1
Explanation: No element greater than 20 is found. So output is -1.
Input: arr[] = [1, 1, 2, 8, 10, 11, 12, 19], x = 0
Output: 0
Explanation: Smallest number greater than 0 is 1, whose indices are 0 and 1. The index of the first occurrence is 0.
"""

def findCeil(arr, x):
    """
    1. if arr[mid] matches with value that that is the ceil
    2. if greater element that can be poosible ans, store and move in left to find better ans
    3. if smaller element then move to right
    Time Complexity: O(logN)
    Space Complexity: O(1)
    """
    n = len(arr)
    start = 0
    end = n - 1
    ans  = -1

    while start <= end:
        mid = (start+end) // 2

        if arr[mid]  >= x:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans

arr = [1, 1, 4, 4, 4, 4, 10]
x = 4
print(findCeil(arr, x))