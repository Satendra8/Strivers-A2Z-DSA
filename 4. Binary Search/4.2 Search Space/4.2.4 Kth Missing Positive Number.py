"""
Q. You are given a strictly increasing array 'vec' and a positive integer 'k'. Find the 'kth' positive integer missing from 'vec'.

Example 1:
Input Format:
 vec[]={4,7,9,10}, k = 1
Result:
 1
Explanation:
 The missing numbers are 1, 2, 3, 5, 6, 8, 11, 12, ……, and so on. Since 'k' is 1, the first missing element is 1.
Example 2:
Input Format:
 vec[]={4,7,9,10}, k = 4
Result:
 5
Explanation:
 The missing numbers are 1, 2, 3, 5, 6, 8, 11, 12, ……, and so on. Since 'k' is 4, the fourth missing element is 5.
"""


def findKthPositive(arr, k):
    """
    1. Brute Force Approach
    2. assume possible ans is k
    3. if any number found less than k, increment k, because i will not be the ans
    4. if no number is greater than k, break
    5. Time Complexity: O(N)
    6. Space Complexity: O(1)
    
    """
    for i in arr:
        if k >= i:
            k += 1
        else:
            break
    return k
arr = [2,3,4,7,11]
k = 5
print(findKthPositive(arr, k))

"""
arr = [2,3,4,7,11], k=5

[1,2,3,4,5,6,7,8,9,10,11] -> [1,5,6,8,9] -> so 9 will be answer

assume possible answer is 5
now 2 found then ignoring so possible answer is 6
now 3 found then ignoring so possible answer is 7
now 4 found then ignoring so possible answer is 8
now 4 found then ignoring so possible answer is 9
now 11 found but it is greater than 9, so this will not impact

"""

def findKthPositive(arr, k):
    """
    1. Optimal Approach
    2. find number of missing elements till mid using arr[mid] - mid - 1
    3. if missing <= k, look towards right
    4. else look towards right
    5. once k exceeds, now out missing number exist between (right, left)
    6. Once we find the index i, we can return the kth missing positive integer, which is equal to arr[i] + k - (arr[i] - i - 1).
    7. after simplifying we will get k + i + i (where i is right)
    8. Time Complexity: O(logn)
    9. Space Complexity: O(1)
    """
    n = len(arr)
    left = 0
    right = n - 1

    while left <= right:
        mid = (left+right) // 2
        missing = arr[mid] - mid - 1
        if missing < k:
            left = mid + 1
        else:
            right = mid - 1
    return k + right + 1
    
arr = [2,3,4,7,11]

k = 5
print(findKthPositive(arr, k))

"""
       0,1,2,3,4
arr = [2,3,4,7,11], k=5
                          left=0, right=4, mid=2 (4-2-1) = 1
                          left=3, right=4, mid=3 (7-3-1) = 3
                          left=4, right=4, mid=4 (11-4-1) = 6
                          left=4, right=3

                          ans = 5 + 3 + 1 = 9

       0,1,2,3  k = 4
arr = [4,7,9,10] left=0, right=3, mid=1 (7-1-1) = 5
                 left=0, right=0, mid=0 (4-0-1) = 3
                 left=1, right=0, mid=0

                 ans = 4 + 0 + 1

       0,1,2,3  k = 2
arr = [1,2,3,4] left=0, right=3, mid=1 (2-1-1) = 0
                left=2, right=3, mid=2 (3-2-1) = 0
                left=3, right=3, mid=3 (4-3-1) = 0
                left=4, right=3, mid=3

                ans = 2 + 3 + 1 = 6

 0  1  2  3  4 k=14
[1,10,21,22,25] left=0, right=5, mid=2 (21-2-1) = 18
                left=0, right=1, mid=0 (1-0-1) = 1
                left=1, right=1, mid=1 (10-1-1) = 8
                left=2, right=1, mid=1

                ans = 14 + 1 + 1 = 16

k = 14
"""