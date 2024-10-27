"""
Q. Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""


def myPow(x, n):
    """
    1. if n is even x = x*x and n = n//2
    2. if n is odd n = n-1 and multiply x to ans
    3. Time Complexity: log(N)
    4. Space Complexity: O(1)
    """
    if n == 0:
        return 1
    
    origional_n = n
    if n < 0:
        n = -(n)

    ans = 1
    while n > 1:
        if n % 2 == 0:
            x = x*x
            n = n//2
        else:
            ans = ans * x
            n -= 1
    ans = ans * x
    print(ans)
    # handle negative case
    if origional_n < 0:
        return (1/ans)
    return ans

x = 2
n = -2

print(myPow(x, n))



"""
x = 2, n = 10, ans = 4

(even) => (2*2)^5
(odd)  => 4*(4)^4
(even) => (4*4)^2
(even) => (16*16)^1

ans = 256 * 4 = 1024
"""