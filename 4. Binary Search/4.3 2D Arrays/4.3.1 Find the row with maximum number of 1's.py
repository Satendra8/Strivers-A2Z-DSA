"""
Q. You have been given a non-empty grid 'mat' with 'n' rows and 'm' columns consisting of only 0s and 1s. All the rows are sorted in ascending order.
Your task is to find the index of the row with the maximum number of ones.
Note: If two rows have the same number of ones, consider the one with a smaller index. If there's no row with at least 1 zero, return -1.


Example 1:
Input Format:
 n = 3, m = 3, 
mat[] = 
1 1 1
0 0 1
0 0 0
Result:
 0
Explanation:
 The row with the maximum number of ones is 0 (0 - indexed).

Example 2:
Input Format:
 n = 2, m = 2 , 
mat[] = 
0 0
0 0
Result:
 -1
Explanation:
  The matrix does not contain any 1. So, -1 is the answer.
"""

def rowWithMaxis(arr):
    """
    1. Brute Force Approach
    2. check and count all ones in a row
    3. return the row index having max count
    4. Time Complexity: O(m*n)
    5. Space Complexity: O(1)
    """
    rows = len(arr)
    cols = len(arr[0])
    max_count = 0
    max_count_index = -1

    for i in range(rows):
        counter = 0
        for j in range(cols):
            if arr[i][j] == 1:
                counter += 1
        if counter > max_count:
            max_count = counter
            max_count_index = i

    return max_count_index

arr = [[0, 0],
       [1, 1]]

print(rowWithMaxis(arr))




def findFirstOccurance(subarray):
    left = 1
    right = len(subarray) - 1
    if subarray[0] == 1:
        return 0

    while left <= right:
        mid = (left+right) // 2
        if subarray[mid] == 1 and subarray[mid-1] == 0:
            return mid
        elif subarray[mid] < 1:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def rowWithMaxis(arr):
    """
    1. Optimal Approach
    2. find first occurance of 1 using binary search
    3. count number of 1 using formula cols - first_occurance
    4. update max_count and max_count_index
    4. Time Complexity: O(n*logm)
    5. Space Complexity: O(1)
    """
    rows = len(arr)
    cols = len(arr[0])
    max_count = 0
    max_count_index = -1

    for i in range(rows):
        counter = 0
        first_occurance = findFirstOccurance(arr[i])
        if first_occurance != -1:
            counter = cols - first_occurance
        if counter > max_count:
            max_count = counter
            max_count_index = i
    return max_count_index

arr =  [[0],
        [0]]

print(rowWithMaxis(arr))


"""    0  1  2
arr = [0, 0, 1]    left=1, right=2, mid=1
                   left=2, right=2, mid=2
"""