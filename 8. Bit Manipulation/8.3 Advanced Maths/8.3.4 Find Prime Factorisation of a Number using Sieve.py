"""
Q. You are given a positive number N. Using the concept of Sieve, compute its prime factorisation.

Example:

Input: 
N = 12246
Output: 
2 3 13 157
Explanation: 
2*3*13*157 = 12246 = N.
"""

import math


def sieve(N):
    arr = [1]*(N+1)
    x = math.ceil(math.sqrt(N))
    for i in range(2, x+1):
        if arr[i] == 1:
            for j in range(i*i, N+1, i):
                arr[j] = 0
    return arr


def findPrimeFactorsBrute(N):
    """
    1. create arr with sieve algorithm
    2. iterate and check prime and add in array
    3. Time Complexity: Nlog(logN)
    4. Space Complexity: O(N)
    """
    arr = sieve(N)
    ans = []
    
    num = N
    for i in range(2, N+1):
        if arr[i] == 1 and N%i == 0:
            while(N%i == 0):
                ans.append(i)
                N = N//i
    return ans
        


def findPrimeFactorsBetter(N):
    """
    1. use old school logic
    2. loop till N and keep dividing N by prime number
    3. Time Complexity: O(sqrt(N))
    4. Space Complexity: depend on length of ans
    """
    ans = []
    x = math.ceil(math.sqrt(N))
    for i in range(2, x+1):
        if N%i == 0:
            while(N%i == 0):
                ans.append(i)
                N = N//i
    if N > 1:
        ans.append(N)
    return ans


def findPrimeFactorsOptimal(N):
    """
    1. First find smallest prime factor spf
    2. use sieve, create an array of numbers itself
    3. mark divisors of all primes to same as smallest
    4. don't update if already updated
    5. now spf table is ready
    6. loop till N>1 and find smallest divisor from spf table and keep dividing.
    7. Time Complexity: Nlog(logN)
    8. Space Complexity: O(N) for sieve
    """
    if N <=1:
        return [N]
    arr = [i for i in range(N+1)]
    x = math.ceil(math.sqrt(N))
    for i in range(2, x+1):
        if arr[i] == i:
            for j in range(i*i, N+1, i):
                if arr[j] == j:
                    arr[j] = i

    ans = []
    while N > 1:
        ans.append(arr[N])
        N = N // arr[N]
    return ans


N = 20
print(findPrimeFactorsOptimal(N))



# def AllPrimeFactors(N):
#     ans = set()
#     if N == 1:
#         return ans

#     for i in range(2, int(math.ceil(math.sqrt(N+1)))):
#         while N%i == 0:
#             N = N//i
#             ans.add(i)
#     if N != 1:
#         ans.add(N)
#     return ans

# N = 100
# print(AllPrimeFactors(N))