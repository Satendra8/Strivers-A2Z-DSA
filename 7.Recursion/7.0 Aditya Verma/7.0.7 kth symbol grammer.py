"""
Q. We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

Example 1:

Input: n = 1, k = 1
Output: 0
Explanation: row 1: 0
Example 2:

Input: n = 2, k = 1
Output: 0
Explanation: 
row 1: 0
row 2: 01
Example 3:

Input: n = 2, k = 2
Output: 1
Explanation: 
row 1: 0
row 2: 01
"""

def kthGrammer(n, k):
    """
    Hypothesis: current row depend on previous one
    Base case: already given in question n=1 and k=1 return 0
    Induction:
        observation 1: for k=1 number of 01 are 2**(n-1)
        observation 2: if ans lies in firsh half then return as it is
        observation 3: if ans lies in second half then return 1s complement of that
    Time Complexity: 2**n
    Space Complexity: logN
    """
    if n == 1 and k == 1:
        return 0
    mid = (2 ** (n-1)) / 2
    if k <= mid:
        return kthGrammer(n-1, k)
    else:
        return int(not(kthGrammer(n-1, k-mid)))
    
n = 2
k = 2
print(kthGrammer(n,k))

"""
n = 2
k = 2

k = 1 0
k = 2 01
"""

