"""
Given a number N. Find its unique prime factors in increasing order.
 

Example 1:

Input: N = 100
Output: 2 5
Explanation: 2 and 5 are the unique prime
factors of 100.
Example 2:

Input: N = 35
Output: 5 7
Explanation: 5 and 7 are the unique prime
factors of 35.
"""

import math
def isPrime(N):
    if N <= 1:
        return False
    if N == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

def AllPrimeFactorsBrute(N):
    """
    1. Iterate from 2 to N
    2. check if N is divisible and that number is prime then append to list
    3. Time Complexity: O(N*sqrt(N))
    4. Space Complexity: depend on length of ans
    """
    s = set()

    for i in range(2, N+1):
        if N%i == 0:
            if isPrime(i):
                s.add(i)
    return s



def AllPrimeFactorsBetter(N):
    """
    1 36
    2 18
    3 12
    4 9
    6 6
    1. Iterate from 2 to sqrt(N)
    2. check if N is divisible and that number is prime then append to list
    Time Complexity: O(sqrt(N)*sqrt(N))
    Space Complexity: depend on length of ans
    """
    s = set()
    for i in range(2, math.ceil(math.sqrt(N))+1):
        if N%i == 0:
            if isPrime(i):
                s.add(i)
    if(isPrime(N)):
        s.add(N)
    return s



def AllPrimeFactors(N):
    """
    1. Use old school factor method
    2. check if N is divisible then keep dividing
    3. update N by N/i
    4. Time Complexity: O(N)
    5. Space Complexity: depend on length of ans
    """
    ans = []
    for i in range(2, N+1):
        if N%i == 0:
            ans.append(i)
            while(N%i == 0):
                N = N/i
    return ans


def AllPrimeFactorsOptimal(N):
    """
    1. Use old school factor method
    2. check if N is divisible then keep dividing
    3. update N by N/i
    4. ** check if N is still not 1, add it to ans
    5. Time Complexity: O(sqrt(N))
    6. Space Complexity: depend on length of ans
    """
    ans = []
    for i in range(2, math.ceil(math.sqrt(N))+1):
        if N%i == 0:
            ans.append(i)
            while(N%i == 0):
                N = N/i
    if N != 1:
        ans.append(N)
    return ans

N = 10
print(AllPrimeFactorsOptimal(N))




import math

def largestPrimeFactor(n):
    """
    1. use old school method
    2. check if N is divisible then keep dividing
    3. update N by N/i
    4. if n becomes 1 means we have captured lagest prime
    5. otherwise largest number is remainder
    6. Time Complexity: O(sqrt(N))
    7. Space Complexity: O(1)
    """
    for i in range(2, math.ceil(math.sqrt(n))+1):
        while n % i == 0:
            n = n/i
            ans = i
    if n == 1:
        return ans
    return n

n = 4
print(largestPrimeFactor(n))