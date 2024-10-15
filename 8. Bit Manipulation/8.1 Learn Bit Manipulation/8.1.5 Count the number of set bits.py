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

def countSetBitsUsingRemoveLastSetBit(n):
    counter = 0

    while (n>0):
        counter += 1
        n = n & n-1

    return counter


def countSetBits(n):
    """
    1. Remove Last Set Bit (keep removing last set bit untill it becomes 0)

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
    2. Time Complexity: n * (no of set bits)
    3. Space Complexity: O(1)
    """
    count = 0
    for i in range(1, n+1):
        count += countSetBitsUsingRemoveLastSetBit(i)
    return count

n = 4
print(countSetBits(n))


"""
001
010
011
100
101
110




"""