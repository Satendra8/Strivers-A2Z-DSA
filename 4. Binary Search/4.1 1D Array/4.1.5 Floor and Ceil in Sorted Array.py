"""
Q. You're given an sorted array arr of n integers and an integer x. Find the floor and ceiling of x in arr[0..n-1].
The floor of x is the largest element in the array which is smaller than or equal to x.
The ceiling of x is the smallest element in the array greater than or equal to x.

Example 1:
Input Format: n = 6, arr[] ={3, 4, 4, 7, 8, 10}, x= 5
Result: 4 7
Explanation: The floor of 5 in the array is 4, and the ceiling of 5 in the array is 7.

Example 2:
Input Format: n = 6, arr[] ={3, 4, 4, 7, 8, 10}, x= 8
Result: 8 8
Explanation: The floor of 8 in the array is 8, and the ceiling of 8 in the array is also 8.
"""

def floor_ceiling(a, n,x):
    """
    1. Optimal Approach
    2. Similar as lower bound
    3. check if the element itself if found then lower and upper bound is same
    4. if a[mid] > x, then this may be possible ceiling
    5. if a[mid] < x, then this may be possible floor
    6. Time Copmlexity: O(logN)
    7. Space Complexity: O(1)
    """
    a.sort()
    left = 0
    right = n - 1
    floor = -1
    ceiling = a[n-1]

    while left <= right:
        mid = (left+right) // 2
        if a[mid] == x:
            return a[mid], a[mid]
        elif a[mid] > x:
            ceiling = a[mid]
            right = mid - 1
        else:
            floor = a[mid]
            left = mid + 1   
    return floor, ceiling

x = 28 
a = [80, 59, 26, 46]

print(floor_ceiling(a, 4,  x))

"""
a = [3, 4, 4, 7, 8, 10] left=0, right=5, mid=2
a = [3, 4, 4, 7, 8, 10] left=3, right=5, mid=4
a = [3, 4, 4, 7, 8, 10] left=3, right=3, mid=3

floor=4
ceiling=7
"""