"""
Q. Given an integer N, print all the divisors of N in the ascending order.
 

Example 1:

Input : 20
Output: 1 2 4 5 10 20
Explanation: 20 is completely 
divisible by 1, 2, 4, 5, 10 and 20.

Example 2:

Input: 21191
Output: 1 21191
Explanation: As 21191 is a prime number,
it has only 2 factors(1 and the number itself).

"""

import math
def print_divisors(N):
    """
    1. loop over and find divisor and add it to ans
    2. Time Complexity: O(N)
    3. Space Complexity: O(N)
    """
    ans = []
    for i in range(1, N+1):
        if N%i == 0:
            ans.append(i)
    return ans


def print_divisors_optimal(N):
    """
    1 36
    2 18
    3 12
    4 9
    6 6
    1. run loop till sqrt(N)
    2. check if divisor and print i and N//i
    3. Time Complexity: O(sqrt(N))
    4. Space Complexity: O(1)
    """
    ans = []
    x = round(N**(1/2))
    for i in range(1, x+1):
        if N%i == 0:
            ans.append(i)
            if i != N//i:
                ans.append(N//i)
    return ans



def print_divisor_gfg(N):
    """
    Just wanted to print the O/P in sorted order
    """
    last = []
    x = round(N**(1/2))
    for i in range(1, x+1):
        if N%i == 0:
            print(i, end=" ")
            if i != N//i:
                last.append(N//i)
    last = last[::-1]
    for num in last:
        print(num, end=" ")



def print_divisor_gfg_optimal(N):
    """
    1. Optimal Approach
    2. run loop 1 to sqrt(N) and print i
    3. add case for perfect square to avoid duplicate x -= 1
    4. run loop sqrt(N) to 1 and print N//i
    5. Time Complexity: O(sqrt(N))
    6. Space Complexity: O(1)
    """
    x = round(N**(1/2))
    for i in range(1, x+1):
        if N%i == 0:
            print(i, end=" ")
    #ignore repetition in case of perfect square
    if x*x == N:
        x -= 1
    for i in range(x, 0, -1):
        if N%i == 0:
            print(N//i, end=" ")

N = 39
print(print_divisor_gfg_optimal(N))