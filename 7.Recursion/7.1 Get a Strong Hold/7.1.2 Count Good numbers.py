"""
Q. A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.


Example 1:

Input: n = 1
Output: 5
Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".
Example 2:

Input: n = 4
Output: 400
Example 3:

Input: n = 50
Output: 564908303

"""

def countGoodNumbers(n):
    """
    1. Brute Force Approach
    """
    ans = 1
    for i in range(n):
        if i % 2 == 0:
            ans *= 5
        else:
            ans *= 4
    return ans % (10**9 + 7)


def powOptimal(x, n):
    """
    Time Complexity: O(logN), as we are dividing by 2
    """
    MOD = 10**9 + 7
    origional_n = n
    if (n < 0):
        n = -(n)
    ans = 1
    while(n>0):
        if n % 2 == 0:
            x = x * x
            x = x % MOD
            n = n // 2
        else:
            ans *= x
            ans = ans % MOD
            n -= 1
        
    #handle negative case
    if origional_n < 0:
        return 1/ans

    return ans % MOD


def countGoodNumbersOptimal(n):
    """
    1. Optimal Approach
    """
    MOD = 10**9 + 7

    half = (n // 2)
    ans = 1

    ans = (powOptimal(5, half) % MOD ) * (powOptimal(4,half) % MOD ) % MOD

    if n % 2 == 1:
        ans = (ans * 5) % MOD
    
    return ans % MOD


print(countGoodNumbersOptimal(4))


"""
n = 4

Formula = 

_ _ _ _   => since 0 is even we can put [0,2,4,6,8]
0 1 2 3 

_ _ _ _   => since 1 is odd we can put [2,3,5,7]
0 1 2 3 

_ _ _ _   => since 2 is even we can put [0,2,4,6,8]
0 1 2 3 

_ _ _ _   => since 3 is odd we can put [2,3,5,7]
0 1 2 3 


all possiblities = 5*4*5*4 = 400


Optimized Formula

n = 4 = even = (2 even) + (2 odd)
n = 5 = odd = (2 even) + (2 odd) + 1 even
n = 6 = odd = (3 even) + (3 odd)
"""