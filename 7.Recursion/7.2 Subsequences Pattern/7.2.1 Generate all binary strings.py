"""
Q. Given an integer, K. Generate all binary strings of size k without consecutive 1's.

Examples: 

Input : K = 3  
Output : 000 , 001 , 010 , 100 , 101 
Input : K  = 4 
Output :0000 0001 0010 0100 0101 1000 1001 1010

"""


def binary(n, ans):
    """
    1. base case: if n == 0 print ans (ans is present at leaf node)
    2. make choice for 0
    3. make choice for 1, only if prev element is not 1
    """

    if n == 0:
        print(ans)
        return

    binary(n-1, ans + "0")
    if not ans or ans[-1] != "1":
        binary(n-1, ans + "1")
    return

n = 4
binary(n, "")