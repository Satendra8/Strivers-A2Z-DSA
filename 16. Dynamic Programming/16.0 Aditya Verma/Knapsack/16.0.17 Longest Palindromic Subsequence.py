"""
Q. Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
"""

def LCS(text1, text2, m, n):
    t = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])
    return t[m][n]



def longestPalindromeSubseq(s):
    """
    1. Variation of LCS
    2. reverse the string to make it second input string for LCS
    3. count LCS
    Time Complexity: O(N*N)
    Space Complexity: O(N*N)
    """
    n = len(s)
    text2 = s[::-1]

    return LCS(s, text2, n, n)

s = "cbbd"
print(longestPalindromeSubseq(s))