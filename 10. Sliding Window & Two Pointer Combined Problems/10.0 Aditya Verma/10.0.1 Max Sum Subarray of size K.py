"""
Q. Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.

Note: A subarray is a contiguous part of any given array.

Examples:

Input: arr[] = [100, 200, 300, 400] , k = 2
Output: 700
Explanation: arr3  + arr4 = 700, which is maximum.
Input: arr[] = [100, 200, 300, 400] , k = 4
Output: 1000
Explanation: arr1 + arr2 + arr3 + arr4 = 1000, which is maximum.
Input: arr[] = [100, 200, 300, 400] , k = 1
Output: 400
Explanation: arr4 = 400, which is maximum.
"""

def maximumSumSubarray(arr, k):
    """
    1. Sliding window
    2. Identification:
        i. array
        ii. sub array / sub str
        iii. window size
        iv. find max, min
    3. keep updating summ till reaches to window size
    4. calculation: add new value to summ
    5. slide the window
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    n = len(arr)
    summ = 0
    maxx = 0
    i = 0
    j = 0
    while j < n:
        if j-i < k:
            summ += arr[j]
            j += 1
        elif j-i == k:
            summ += arr[j]
            summ -= arr[i]
            i += 1
            j += 1
        maxx = max(summ, maxx)
    return maxx

arr = [100, 200, 300, 400] 
k = 1
print(maximumSumSubarray(arr, k))

"""
arr = [100, 200, 300, 400] 
k = 2

n = 4
summ = 700
maxx = 0
i = 2
j = 4
"""