"""
Q. Given an unsorted array, Arr[] of size N and that contains even number of occurrences for all numbers except two numbers. Find the two numbers in decreasing order which has odd occurrences.

Example 1:

Input:
N = 8
Arr = {4, 2, 4, 5, 2, 3, 3, 1}
Output: {5, 1} 
Explanation: 5 and 1 have odd occurrences.

Example 2:

Input:
N = 8
Arr = {1 7 5 7 5 4 7 4}
Output: {7, 1}
Explanation: 7 and 1 have odd occurrences.
"""

def twoOddNum(Arr, N):
    """
    1. Optimal Approach
    2. find xor of all numbers
    3. check right most set bit of xor (or get the number where there is only rightmost bit is set (xor & (xor-1)) ^ xor)
    4. now at that position for all array numbers if bit is set seperate their xor in two variables
    5. now both nums will be in different bucket
    6. Time Complexity: O(N)
    7. Space Complexity: O(1)
    """
    xor = 0
    for num in Arr:
        xor = xor ^ num

    set_bit = (xor & (xor-1)) ^ xor

    bucket1 = 0
    bucket2 = 0
    for num in Arr:
        if (num & set_bit):
            bucket1 = bucket1 ^ num
        else:
            bucket2 = bucket2 ^ num
    
    return bucket1, bucket2

Arr = [4, 2, 4, 5, 2, 3, 3, 1]
N = 8
print(twoOddNum(Arr, N))


def findRightMostSetBit(n):
    for i in range(31):
        if n & (1<<i) > 0:
            return i
    return -1

def f(arr):
    all_xor = 0
    for num in arr:
        all_xor = all_xor ^ num
    
    set_bit = findRightMostSetBit(all_xor)

    xor_0 = 0
    xor_1 = 0
    for num in arr:
        if num & (1 << set_bit) > 0:
            xor_1 = xor_1 ^ num
        else:
            xor_0 = xor_0 ^ num
    first = all_xor ^ xor_0
    second = all_xor ^ xor_1
    return first, second
    

arr = [1, 7, 5, 7, 5, 4, 7, 4]
print(f(arr))