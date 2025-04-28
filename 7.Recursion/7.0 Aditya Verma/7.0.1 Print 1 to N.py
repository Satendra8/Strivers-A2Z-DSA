"""
Q. Given an positive integer n, print numbers from 1 to n without using loops.

Implement the function printTillN() to print the numbers from 1 to n as space-separated integers.

Examples

Input: n = 5
Output: 1 2 3 4 5
Explanation: We have to print numbers from 1 to 5.
Input: n = 10
Output: 1 2 3 4 5 6 7 8 9 10
Explanation: We have to print numbers from 1 to 10.
"""

def printTillN(n):
    if n == 1:
        print(n)
        return
    printTillN(n-1)
    print(n)
    return


def printNto1(n):
    if n == 1:
        print(n)
        return
    print(n)
    printNto1(n-1)
    return

n = 5
printNto1(5)