"""
Q. You are given an array of 'N' integers.
You need to find the length of the longest sequence which contains the consecutive elements.

Example 1:

Input: [100, 200, 1, 3, 2, 4]

Output: 4

Explanation: The longest consecutive subsequence is 1, 2, 3, and 4.

Input: [3, 8, 5, 7, 6]

Output: 4

Explanation: The longest consecutive subsequence is 5, 6, 7, and 8.

"""


def LCS(arr):
    """
    Brute Force Approach
    1. iterate over all elements
    2. try to find if element + 1, element + 2 ..... find in array
    3. if found, keep increaing the count

    Time Complexity - O(N^2)
    Space Complexity - O(1)
    """
    n = len(arr)
    longest = 1
    x = 1
    i = 0
    
    while i<n:
        if arr[i] + x in arr:
            x += 1
        else:
            x = 1
            i += 1
        longest = max(longest, x)
                
    return longest


def LCS(arr):
    """
    Better Approach
    1. sort the array
    2. check if next - prev == 1, then increse counter
    3. update the final counter

    Time Complexity - O(NlogN)
    Space Complexity - O(1)
    """
    n = len(arr)
    arr.sort()
    longest = 1
    prev = arr[0]
    counter = 1
    
    for i in range(1, n):
        if arr[i] - prev != 1:
            counter = 1
        else:
            counter += 1
        prev = arr[i]
        longest = max(longest, counter)

    return longest




def LCS(arr):
    """
    Optimal Approach
    1. use set to store all elements
    2. check if prev element found then leave that number
    3. else keep checking next and increase counter

    Time Complexity - O(N)
    Space Complexity - O(N)
    """
    n = len(arr)
    longest = 1
    x = 1
    i = 0
    new_set = set(arr)
    while i<n:
        if arr[i] - 1 in new_set:
            i += 1
            x = 1
        elif arr[i] + x in new_set:
            x += 1
        else:
            i += 1
        longest = max(longest, x)
                
    return longest
