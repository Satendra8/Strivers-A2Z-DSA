"""
Q. Given a double x and integer n, calculate x raised to power n. Basically Implement pow(x, n).

Example 1:

Input: x = 2.00000, n = 10

Output: 1024.00000

Explanation: You need to calculate 2.00000 raised to 10 which gives ans 1024.00000

Example 2:

Input: x = 2.10000, n = 3

Output: 9.26100

Explanation: You need to calculate 2.10000 raised to 3 which gives ans 9.26100

"""

def pow(x, n):
    """
    1. Brute Force Approach
    2. base case if n == 0: return 1
    3. return num * power of num - 1
    4. Time Complexity: O(N)
    4. Space Complexity: O(N)
    """
    #base case
    if n == 0:
        return 1

    return x * pow(x, n-1)


def powOptimal(x, n):
    """
    1. if n is even (2)^10 = even = (2*2)^5 (make x*x and reduce n by half)
    2. if n is odd  (4)^5 = odd = 4 * (4)^4 (multiply x to ans and reduce n by 1)
    3. if n was negative return 1/n else return n
    4. Time Complexity: O(logN), as we are dividing by 2
    5. Space Complexity: O(1)
    """
    origional_n = n
    if (n < 0):
        n = -(n)
    ans = 1
    while(n>0):
        if n % 2 == 0:
            x = x * x
            n = n // 2
        else:
            ans *= x
            n -= 1
        
    #handle negative case
    if origional_n < 0:
        return 1/ans

    return ans

x = 2.00000
n = -2
print(powOptimal(x,n))


"""
Dry Run:

x = 2.00000
n = 5

going top -> down

2 * pow(2, 4) => return 32

2 * pow(2, 3) => return 16

2 * pow(2, 2) => return 8

2 * pow(2, 1) => return 4

2 * pow(2, 0) => return 2

return 1


Dry Run Optimal

(2)^10 = even = (2*2)^5
(4)^5 = odd = 4 * (4)^4
(4)^4 = even = (4*4)^2
(16)^2 = odd = (16*16)^1
(256)^1 = odd = 256 * (256)^0

ans = 256 * 4 = 1024



Dry Run Optimal

ans = 8*16*16*16

(2)^15 = odd = 2 * (2)^14
(2)^14 = even = (2*2)^7
(4)^7 = odd = 4 * (4)^6
(4)^6 = even = (16)^3
(16)^3 = odd = 16 * (16)^2
(16)^2 = even = (16*16)^1
(16)^1 = odd = 16 * (16)^0

"""
