"""
Q. Given two numbers N and M, find the Nth root of M. The nth root of a number M is defined as a number X when raised to the power N equals M. If the 'nth root is not an integer, return -1.

Example 1:
Input Format:
 N = 3, M = 27
Result:
 3
Explanation:
 The cube root of 27 is equal to 3.

Example 2:
Input Format:
 N = 4, M = 69
Result:
 -1
Explanation:
 The 4th root of 69 does not exist. So, the answer is -1.

"""


def NthRoot(n, m):
    """
    1. Brute Force Approach
    2. Iterate from 1 to m+1
    3. check if i**n matches then return
    4. return -1 if no match
    5. Time Complexity: O(NlogN)
    6. Space Complexity: O(1)
    """
    for i in range(1, m+1):
        if i**n == m:
            return i
        
    return -1

n = 4
m = 1
print(NthRoot(n, m))





def NthRoot(n, m):
    """
    1. Optimal Approach
    2. if m == 1 return 1 or n == 1 return m
    3. check if mid**n matches then return
    4. if mid ** n > m then trim right
    5. if mid ** n < m then trim left
    6. Time Complexity: O(logN*logN) if using exponent method, O(NlogN) if using for loop for mid**n
    7. Space Complexity: O(1)
    """
    left = 1
    right = m
    if m == 1:
        return 1
    if n == 1:
        return m
    
    while left <= right:
        mid = (left+right) // 2
        if mid**n == m:
            return mid
        elif mid**n > m:
            right = mid - 1
        else:
            left = mid + 1
    return -1

n = 3
m = 27
print(NthRoot(n, m))

# n = 1
# m = 15
"""
n = 3
m = 27

[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,27] left=1, right=27, mid=14
                                                                       left=1, right=13, mid=7
                                                                       left=1, right=6, mid=3


n = 4
m = 69

[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,30,31,32,33,34]  left=1, right=34, mid=17
                                                                                             left=1, right=16, mid=8
                                                                                             left=1, right=7, mid=4
                                                                                             left=5, right=7, mid=6
                                                                                             left=5, right=5, mid=5
                                                                                             left=5, right=4, mid=5
"""