"""
Q. You are given two strings s and t. Now your task is to print all longest common sub-sequences in lexicographical order.

Note -  A Sub-sequence is derived from another string by deleting some or none of the elements without changing the order of the remaining elements.

Example 1:

Input: s = abaaa, t = baabaca
Output: aaaa abaa baaa
Explanation - Length of lcs is 4, in lexicographical order they are aaaa, abaa, baaa

Example 2:

Input: s = aaa, t = a
Output: a
"""

def LCS(s, t, m, n):
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = 1+ dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp

def all_longest_common_subsequences(s, t):
    """
    Variation of LCS
    1. do normal LCS
    2. do similar to back tracking, start from last if match go diagonal i-1, j-1
    3. if not matches compare adjacent and pick the maximum one
    4. return the ans in reverse order
    Time Complexity: O(M*N)
    Space Complexity: O(M*N)
    """
    m = len(s)
    n = len(t)
    dp = LCS(s, t, m, n)

    ans = ""
    i = m
    j = n

    while i>0 and j>0:
        if s[i-1] == t[j-1]:
            ans += s[i-1]
            i -= 1
            j -= 1
        else:
            if dp[i][j-1] > dp[i-1][j]:
                j -= 1
            else:
                i -= 1
    return ans[::-1]

s = "abaaa"
t = "baabaca"
print(all_longest_common_subsequences(s, t))