"""
Q. Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".


** Code will be same for deletion **
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


def minInsertions(s):
    """
    Variation of LCS
    1. generate the second input string by revervsing the string
    2. find LCS
    3. subtract LCS from length of string
    Time Complexity: O(M*N)
    Space Complexity: O(M*N)
    """
    n = len(s)
    text2 = s[::-1]
    l = LCS(s, text2, n, n)
    return n - l

s = "leetcode"
print(minInsertions(s))



"""
s = leetcode
reverse(s) = edocteel

LCS = ece

LCS - len(s) = 8-3 = 5

mbadm
mdabm

LCS = mam

LCS - len(s) = 5 - 3 = 2
"""