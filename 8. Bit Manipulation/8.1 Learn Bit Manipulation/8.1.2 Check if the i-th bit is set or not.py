"""
Q. Given a number n and a bit number k, check if kth index bit of n is set or not. A bit is called set if it is 1. Position of set bit '1' should be indexed starting with 0 from LSB side in binary representation of the number.
Note: Index is starting from 0. You just need to return true or false, driver code will take care of printing "Yes" and "No".

Examples : 

Input: n = 4, k = 0
Output: No
Explanation: Binary representation of 4 is 100, in which 0th index bit from LSB is not set. So, return false.
Input: n = 4, k = 2
Output: Yes
Explanation: Binary representation of 4 is 100, in which 2nd index bit from LSB is set. So, return true.
Input: n = 500, k = 3
Output: No
Explanation: Binary representation of 500 is 111110100, in which 3rd index bit from LSB is not set. So, return false.

"""

def convert2Binary(n):
    ans = ""
    while(n>1):
        rem = n % 2
        n = n//2
        ans = str(rem) + ans
    if n == 1:
        ans = str(n) + ans
    if n == 0:
        ans = str(n) + ans
    return ans


def checkIfithBitisSet(n, i):
    """
    1. Brute Force Approach
    2. convert number into binary
    3. then iterate and check nth bit
    4. Time Complexity: O(logN)s
    5. Space Complexity: O(logN) to store binary representation
    """
    binary = convert2Binary(n)

    index = 0
    for c in range(len(binary)-1, -1, -1):
        if index == i:
            if binary[c] == '1':
                return True
            else:
                return False
        index += 1
    return False


def checkIfithBitisSetOptimal(n, i):
    """
    1. Optimal Approach
    2. 1 << i (left shift 1 by i)
    3. then and with number
    4. if number > 0 (set)
    5. if num == 0 (not set)
    6. Time Complexity: O(1)
    7. Space Complexity: O(1)
    """
    # USING >> (left shift)

    if (n & (1 << i) != 0):
        return True
    return False

    # USING >> (right shift)

    if ((n >> i) & 1 == 1):
        return True
    return False

n = 13 #1101
i = 2
print(checkIfithBitisSetOptimal(13, i))


"""
>> (right shift)

13 - 1101
     0011
    &0001
    ------
     0001s
"""