"""
Q. Given an integer n, return the number of prime numbers that are strictly less than n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
"""

import math
def isPrime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    x = int(math.ceil(math.sqrt(num)))
    for i in range(2, x+1):
        if num % i == 0:
            return False
    return True

def countPrimes(N):
    """
    1. Loop till N and check if prime
    2. increment the counter
    3. Time Complexity: O(N*sqrt(N))
    4. Space Complexity: O(1)
    """
    count = 0
    for i in range(1, N):
        if isPrime(i):
            count += 1
    return count



def sieve(N):
    """
    1. Create an array of 0 till N+1
    2. divide numbers till N by prime numbers and mark 0 if they are divisible
    3. at the end count number of 1's present in arr
    Time Complexity: Nlog(logN) (prime harmonic series)
    Space Complexity: O(N)
    """
    arr = [1]*(N+1)
    x = int(math.ceil(math.sqrt(N)))
    for i in range(2, x+1):
        if arr[i] == 1:
            for j in range(i*i, N+1, i):
                arr[j] = 0
    count = 0
    for i in range(2, N+1):
        if arr[i] == 1:
            count += 1
    return count



N = 2
print(sieve(10))