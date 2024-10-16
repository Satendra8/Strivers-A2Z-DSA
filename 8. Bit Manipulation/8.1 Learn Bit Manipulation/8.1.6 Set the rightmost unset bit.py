"""
Q. Given a non-negative number n . The problem is to set the rightmost unset bit in the binary representation of n.

Examples :

Input: n = 6
Output: 7
Explanation: The binary representation of 6 is 110. After setting right most bit it becomes 111 which is 7.


Input: n = 15
Output: 31
Explanation: The binary representation of 15 is 01111. After setting right most bit it becomes 11111 which is 31.

"""

def setBit(n):
    return (n | n+1)

n = 9
print(setBit(n))

"""
n | n+1

n = 15, n+1 = 16
01111
10000 (|)
--------
11111


n = 9, n+1 = 10

1001
1010
-------
1011
"""