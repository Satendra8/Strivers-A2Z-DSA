"""
Q. Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
"""

def LCSRecursive(text1, text2, m, n):
    """
    1. Base case: think of smallest valid input which is "" empty string
    2. choice diagram: if last char of both match, we have 1 choice
    3. if not match we have 2 choices take text1 full and text2 n-1
    4. take text2 full and text1 n-1
    5. Time Complexity: O(2^N)
    6. Space Complexity: O(2^N)
    """
    if n == 0 or m == 0:
        return 0
    
    if text1[m-1] == text2[n-1]:
        return 1 + LCSRecursive(text1, text2, m-1, n-1)
    else:
        return max(LCSRecursive(text1, text2, m-1, n), LCSRecursive(text1, text2, m, n-1))


def longestCommonSubsequenceRecursive(text1, text2):
    m = len(text1)
    n = len(text2)
    return LCSRecursive(text1, text2, m, n)

def LCS(text1, text2, m, n, t):
    """
    1. Base case: think of smallest valid input which is "" empty string
    2. choice diagram: if last char of both match, we have 1 choice
    3. if not match we have 2 choices take text1 full and text2 n-1
    4. take text2 full and text1 n-1
    5. problems are overlapping so memoization is required
    6. m, n are changing so matrix should be of size m*n
    5. Time Complexity: O(M*N)
    6. Space Complexity: O(M*N) + O(M*N) #stack space
    """
    if n == 0 or m == 0:
        return 0
    
    if t[m][n] != -1:
        return t[m][n]

    if text1[m-1] == text2[n-1]:
        t[m][n] =  1 + LCS(text1, text2, m-1, n-1, t)
    else:
        t[m][n] = max(LCS(text1, text2, m-1, n, t), LCS(text1, text2, m, n-1, t))
    return t[m][n]


def longestCommonSubsequence(text1, text2):
    m = len(text1)
    n = len(text2)
    t = [[-1] * (n+1) for _ in range(m+1)]
    return LCS(text1, text2, m, n, t)



def LCSTabulation(text1, text2):
    """
    1. initialization: as per recursion base case first row and col will be 0
    2. same as recursive code: m will be i and n will be j
    Time Complexity: O(M*N)
    Space Complexity: O(M*N)
    """
    m = len(text1)
    n = len(text2)

    t = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])
    return t[m][n]


text1 = "abcde"
text2 = "ace" 
print(LCSTabulation(text1, text2))