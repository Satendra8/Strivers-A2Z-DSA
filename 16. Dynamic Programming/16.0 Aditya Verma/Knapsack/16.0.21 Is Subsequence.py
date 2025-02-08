"""
Q. Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""

def LCS(text1, text2, m, n):
    t = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i][j-1], t[i-1][j])
    return t[m][n]



def isSubsequence(s, t):
    """
    Variation of LCS
    1. find LCS
    2. check if the LCS and first string length matches then return true
    3. Time Complexity: O(M*N)
    4. Space Complexity: O(M*N)
    """
    m = len(s)
    n = len(t)

    l = LCS(s, t, m, n)

    return l == m

s = "axc"
t = "ahbgdc"
print(isSubsequence(s, t))