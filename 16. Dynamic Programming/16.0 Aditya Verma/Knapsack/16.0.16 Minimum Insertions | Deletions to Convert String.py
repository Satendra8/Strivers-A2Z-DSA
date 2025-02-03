"""
Q. Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4
"""


def LCS(text1, text2, m, n):
    t = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])
    return t[m][n]

def minDistance(word1, word2):
    """
    Variation of LCS
    1. find longest common subsequence
    2. insertion = m - LCS
    3. deletion = n - LCS
    Time Complexity: O(M*N)
    Space Complexity: O(M*N)
    """
    m = len(word1)
    n = len(word2)

    l = LCS(word1, word2, m, n)
    insertion = m - l
    deletion = n - l
    return insertion + deletion


word1 = "leetcode"
word2 = "etco"
print(minDistance(word1, word2))