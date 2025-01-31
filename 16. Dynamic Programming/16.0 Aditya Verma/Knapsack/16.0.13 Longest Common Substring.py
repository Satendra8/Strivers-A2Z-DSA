"""
Q. You are given two strings s1 and s2. Your task is to find the length of the longest common substring among the given strings.

Examples:

Input: s1 = "ABCDGH", s2 = "ACDGHR"
Output: 4
Explanation: The longest common substring is "CDGH" with a length of 4.
Input: s1 = "abc", s2 = "acb"
Output: 1
Explanation: The longest common substrings are "a", "b", "c" all having length 1.
Input: s1 = "YZ", s2 = "yz"
Output: 0
"""

def longestCommonSubstr(s1, s2):
    """
    LCS variation
    1. initialization: similar to LCS
    2. variation: if char not matches then discontinue the counting
    3. keep updating the value in max variable
    Time Complexity: O(M*N)
    Space Complexity: O(M*N)
    """
    m = len(s1)
    n = len(s2)

    t = [[0] * (n+1) for _ in range(m+1)]

    max_length = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
                max_length = max(max_length, t[i][j])
            else:
                t[i][j] = 0

    print(t)
    return max_length


s1  = "abcde"
s2  = "abfce"
print(longestCommonSubstr(s1, s2))


"""
      0  1  2  3  4  5

0    [0, 0, 0, 0, 0, 0]
1    [0, 1, 0, 0, 0, 0]
2    [0, 0, 2, 0, 0, 0]
3    [0, 0, 0, 0, 1, 0]
4    [0, 0, 0, 0, 0, 0]
5    [0, 0, 0, 0, 0, 1]
"""