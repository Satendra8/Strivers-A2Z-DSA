"""
Q. Given an array arr[] of integers and an integer k, your task is to find the maximum value for each contiguous subarray of size k. The output should be an array of maximum values corresponding to each contiguous subarray.

Examples:

Input: arr[] = [1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3
Output: [3, 3, 4, 5, 5, 5, 6] 
Explanation: 
1st contiguous subarray = [1 2 3] max = 3
2nd contiguous subarray = [2 3 1] max = 3
3rd contiguous subarray = [3 1 4] max = 4
4th contiguous subarray = [1 4 5] max = 5
5th contiguous subarray = [4 5 2] max = 5
6th contiguous subarray = [5 2 3] max = 5
7th contiguous subarray = [2 3 6] max = 6
Input: arr[] = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13], k = 4
Output: [10, 10, 10, 15, 15, 90, 90]
Explanation: 
1st contiguous subarray = [8 5 10 7], max = 10
2nd contiguous subarray = [5 10 7 9], max = 10
3rd contiguous subarray = [10 7 9 4], max = 10
4th contiguous subarray = [7 9 4 15], max = 15
5th contiguous subarray = [9 4 15 12], max = 15
6th contiguous subarray = [4 15 12 90], max = 90
7th contiguous subarray = [15 12 90 13], max = 90
Input: arr[] = [5, 1, 3, 4, 2, 6], k = 1
Output: [5, 1, 3, 4, 2, 6]
Explanation: 
When k = 1, each element in the array is its own subarray, so the output is simply the same array
"""

def maxOfSubarrays(arr, k):
    """
    1. Sliding Window
    2. [3,2,1], if 3 is removed we need to store 2 as largest so we can use a variable
    3. [1,3,-1], 1 is never used because we got larger then that, but -1 can be use if 3 removed
    4. for the above reason we remove all smaller before a larger
    5. larger element is always at first index
    6. remove matching element from left and slide the window
    """
    n = len(arr)
    max_arr = []
    i = 0
    j = 0
    ans = []

    while j < n:
        if j-i+1 < k:
            while max_arr and max_arr[-1] < arr[j]:
                max_arr.pop()
            max_arr.append(arr[j])
            j += 1
        elif j-i+1 == k:
            while max_arr and max_arr[-1] < arr[j]:
                max_arr.pop()
            max_arr.append(arr[j])
            ans.append(max_arr[0])
            if arr[i] == max_arr[0]:
                max_arr.pop(0)
            i += 1
            j += 1
    return ans

arr = [1,3,-1,-3,5,3,6,7]
k = 3

print(maxOfSubarrays(arr, k))

"""
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 3
n = 9

max_arr = [3, 3, 4]
j = 5
i = 2
ans = [3, 1]
"""