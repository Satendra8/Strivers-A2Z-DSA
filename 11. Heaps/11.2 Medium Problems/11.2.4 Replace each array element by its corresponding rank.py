"""
Q. Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
 

Example 1:

Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
Example 2:

Input: arr = [100,100,100]
Output: [1,1,1]
Explanation: Same elements share the same rank.
Example 3:

Input: arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]
"""

def replace(arr):
    """
    1. create duplicate array and sort it
    2. create a map and assign rank to each element
    3. replace the actual array element with the rank
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    n = len(arr)
    new_arr = arr[:]
    new_arr.sort()

    d = {}
    rank = 1
    for i in range(n):
        if new_arr[i] not in d:
            d[new_arr[i]] = rank
            rank += 1
    for i in range(n):
        arr[i] = d.get(arr[i])
    return arr


arr = [37,12,28,9,100,56,80,5,12]
print(replace(arr))