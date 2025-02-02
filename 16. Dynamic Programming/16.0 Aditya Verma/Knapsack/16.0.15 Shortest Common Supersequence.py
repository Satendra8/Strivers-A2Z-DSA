"""
Q. Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"
"""


def LCS(s1, s2, m, n):
    t = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])
    return t[m][n]



def shortestCommonSupersequence(s1, s2):
    """
    Variation of LCS
    1. The basic idea is take common string only once
    2. largest possible string that contains both s1 and s2 is s1+s2
    3. find the LCS
    4. subtract it from LCS to consider common strings only once
    Time Complexity: O(M*N)
    Space Complexity: O(M*N)
    """
    m = len(s1)
    n = len(s2)

    common = LCS(s1, s2, m, n)

    return (m+n) - common


s1 = "AGGTAB"
s2 = "GXTXAYB"
print(shortestCommonSupersequence(s1, s2))