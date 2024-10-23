"""
Q. You are given two integers L and R, your task is to find the XOR of elements of the range [L, R].

Example:

Input: 
L = 4, R = 8 
Output:
8 
Explanation:
4 ^ 5 ^ 6 ^ 7 ^ 8 = 8
"""

def findXOR(l, r):
    """
    1. loop over and XOR
    2. Time Complexity: O(N)
    3. Space Complexity: O(1)
    """
    ans = 0
    for i in range(l, r+1):
        ans = ans ^ i
    return ans


   
def findXORoptimal(l, r):
    """
    1. find out XOR of number till 14
    2. make group of 4
    3. try to find pattern
    4. Time Complexity: O(1)
    5. Space Complexity: O(1)
    """
    ans = 0
    if r%4 == 1:
        ans = 1
    elif r%4 == 2:
        ans = r+1
    elif r%4 == 3:
        ans = 0
    else:
        ans = r

    l = l-1

    if l%4 == 1:
        ans = ans ^ 1
    elif l%4 == 2:
        ans = ans ^ (l+1)
    elif l%4 == 3:
        ans = ans ^ 0
    else:
        ans = ans ^ l

    return ans


l = 3
r = 5
print(findXOR(l, r))

"""
1 => 001   1  =  1
2 => 010   1^2  =  3
3 => 011   1^2^3  =  0
4 => 100   1^2^3^4  =  4

5 => 101    1^2...^5  =  1
6 => 110    1^2...^6  =  7
7 => 111    1^2...^7  =  0
8 => 1000   1^2...^8  =  8

9 => 1001    1^2...^9   =  1
10 => 1010   1^2...^10  =  11
11 => 1011   1^2...^11  =  0
12 => 1100   1^2...^12  =  12

13 => 1101   1^2...^13   =  1
14 => 1110   1^2...^14  =  15
"""