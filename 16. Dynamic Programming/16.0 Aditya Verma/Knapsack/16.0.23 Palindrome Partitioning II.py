"""
Q. Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
.

Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1
"""

def isPalindrom(s, i, j):
    if i >= j:
        return True
    
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1 
    return True


def solveRcursive(s, i, j):
    if i >= j:
        return 0
    
    if isPalindrom(s, i, j):
        return 0

    ans = float('inf')

    for k in range(i, j):
        temp = solveRcursive(s, i, k) + solveRcursive(s, k+1, j) + 1
        ans = min(ans, temp)
    return ans


def minCutRecursive(s):
    n = len(s)
    return solveRcursive(s, 0, n-1)


def solve(s, i, j, t):
    if i >= j:
        return 0
    
    if isPalindrom(s, i, j):
        return 0

    if t[i][j] != -1:
        return t[i][j]

    ans = float('inf')

    for k in range(i, j):
        temp = solve(s, i, k, t) + solve(s, k+1, j, t) + 1
        t[i][j] = min(ans, temp)
        ans = t[i][j]
    return t[i][j]

def solveOptimized(s, i, j, t):
    if i >= j:
        return 0
    
    if isPalindrom(s, i, j):
        return 0

    if t[i][j] != -1:
        return t[i][j]

    ans = float('inf')

    for k in range(i, j):
        if t[i][k] != -1:
            left = t[i][k]
        else:
            left = solveOptimized(s, i, k, t)

        if t[k+1][j] != -1:
            right = t[k+1][j]
        else:
            right = solveOptimized(s, k+1, j, t)

        temp = left + right + 1
        t[i][j] = min(ans, temp)
        ans = t[i][j]
    return t[i][j]


def minCut(s):
    """
    Multiplication Chain Multiplication Variation
    1. find i & j: i = 0, j = n-1, take whole string
    2. base condition: if signle element or no element then partition not possible
    3. base condition: if string is already palindrom then no need to partition
    4. k loop: k => i to j-1, partition of str = (i, k), (k+1, j) if we consider k==j then no patririon possible
    5. we need to find min and extra cost will be 1 because we have already partitioned once 
    Time Complexity: O(N*N)
    Space Complexity: O(N*N)
    """
    n = len(s)
    t = [[-1] * (n+1) for _ in range(n+1)]
    return solveOptimized(s, 0, n-1, t)



s = "nitik"
print(isPalindrom(s, 1, 3))

