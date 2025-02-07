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

def LCS(text1, text2, m, n):
    t = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])
    return t



def shortestCommonSupersequence(str1, str2):
    """
    Variation of LCS
    1. find LCS
    2. backtrack from last, if element at i,j matches take it once
    3. if not matches then also take
    4. edge case: if still there are elements after the end of loop then append it
    5. at the end reverse and return the ans
    Time Complexity: O(M*N)
    Space Complexity: O(M*N)
    """
    m = len(str1)
    n = len(str2)
    
    t = LCS(str1, str2, m, n)

    i = m
    j = n
    ans = ""

    while i>0 and j>0:
        if str1[i-1] == str2[j-1]:
            ans += str1[i-1]
            i -=1
            j -=1
        else:
            if t[i][j-1] > t[i-1][j]:
                ans += str2[j-1]
                j -= 1
            else:
                ans += str1[i-1]
                i -= 1

    #edge case
    while i>0:
        ans += str1[i-1]
        i -= 1

    while j>0:
        ans += str2[j-1]
        j -= 1
    return ans[::-1]


str1 = "abac"
str2 = "cab"
print(shortestCommonSupersequence(str1, str2))
