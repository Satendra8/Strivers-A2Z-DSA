"""
Q. You are given a number n. Find the total count of set bits for all numbers from 1 to n (both inclusive).

Examples :

Input: n = 4
Output: 5
Explanation: For numbers from 1 to 4. For 1: 0 0 1 = 1 set bits For 2: 0 1 0 = 1 set bits For 3: 0 1 1 = 2 set bits For 4: 1 0 0 = 1 set bits Therefore, the total set bits is 5.


Input: n = 17
Output: 35
Explanation: From numbers 1 to 17(both inclusive), the total number of set bits is 35.
"""

def countSetBits(n):
    counter = 0

    while(n>1):
        rem = n % 2
        n = n // 2
        if rem == 1:
            counter += 1
    if n == 1:
        counter += 1
    return counter 

def countSetBitsUsingBitWiseOperator(n):
    counter = 0

    while(n>1):
        #check odd, if odd is 1 remainder is 1
        counter += n&1
        n = n >> 1
    if n == 1:
        counter += 1
    return counter


def countSetBitsUsingRemoveLastSetBit(n):
    """
    1. Remove Last Set Bit (keep removing last set bit untill it becomes 0)
    2. Time Complexity: O(logN)
    3. Space Complexity: O(1)
    """
    counter = 0

    while (n>0):
        counter += 1
        n = n & n-1

    return counter


n = 15 #01111
print(countSetBitsUsingRemoveLastSetBit(n))


def findLargestPowerOf2(n):
    x = 0
    while((1<<x) <= n):
        x += 1
    return x-1

def countSetBitsOptimal(n):
    """
    1. base case: if n becomes 0 return 0
    Step1: find largest power of 2 less than 11 #keep checking if 2^0 < 11, 2^1 < 11, 2^2 < 11, 2^3 < 11, 2^4 < 11 break
    Step2: now number till 7 has total bits = 4+4+4, 2^2*3 = 2^(x-1) * x
    Step3: settle leftmost 1's after 7 = n - (2^x - 1) = n - 2^x + 1
    Step4: count for rest using loop n - 2^x
    Time Complexity: O(logN)
    Space Complexity: O(1)
    """
    if n == 0:
        return 0
    x = findLargestPowerOf2(n)

    countTillx = 0 if x == 0 else x * (1<<(x-1))
    settleLeftMost = n - (1<<x) + 1
    rest = n - (1<<x)
    return countTillx + settleLeftMost + countSetBitsOptimal(rest)

n = 4
print(countSetBitsOptimal(n))
"""
n = 16

Iterate and check if rem is 1
check if n is 1 at last


Bit Wise Solution (use >> to divide)

1000 >> 1 = 100 (4)
100 >> 1 = 10 (2)
10 >> 1 = 01 (1)


Remove Last Set Bit (keep removing last set bit untill it becomes 0)

N = 84

    1010100
N-1 1010011
    --------
&   1010000

    1010000
    1000000
    -------
&   1000000


    1000000
    0111111
    --------
    0000000
"""


"""
Optimized Approach

n = 11

0   - 000
1   - 001
2   - 010
3   - 011
4   - 100
5   - 101
6   - 110
7   - 111
-----------------
8   -1000
9   -1001
10  -1010
11  -1011

Step1: find largest power of 2 less than 11 #keep checking if 2^0 < 11, 2^1 < 11, 2^2 < 11, 2^3 < 11, 2^4 < 11 break
Step2: now number till 7 has total bits = 4+4+4, 2^2*3 = 2^(x-1) * x
Step3: settle leftmost 1's after 7 = n - (2^x - 1) = n - 2^x + 1
Step4: count for rest using loop n - 2^x

8   -1000 -> 000 = 0
9   -1001 -> 001 = 1
10  -1010 -> 010 = 2
11  -1011 -> 011 = 3 (till 3 i need to count using loop)

Final Formula = (2^(x-1) * x) + (n - 2^x + 1) + countTill(n - 2^x)

"""