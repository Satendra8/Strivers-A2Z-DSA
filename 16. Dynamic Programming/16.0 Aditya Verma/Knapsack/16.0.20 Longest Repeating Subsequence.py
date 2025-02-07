"""
Q. Given string str, find the length of the longest repeating subsequence such that it can be found twice in the given string.

The two identified subsequences A and B can use the same ith character from string s if and only if that ith character has different indices in A and B. For example, A = "xax" and B = "xax" then the index of the first "x" must be different in the original string for A and B.

Examples :

Input: s = "axxzxy"
Output: 2
Explanation: The given array with indexes looks like
a x x z x y 
0 1 2 3 4 5
The longest subsequence is "xx". It appears twice as explained below.
subsequence A
x x
0 1  <-- index of subsequence A
------
1 2  <-- index of s
subsequence B
x x
0 1  <-- index of subsequence B
------
2 4  <-- index of s
We are able to use character 'x' (at index 2 in s) in both subsequences as it appears on index 1 in subsequence A and index 0 in subsequence B.
Input: s = "axxxy"
Output: 2
Explanation: The given array with indexes looks like
a x x x y 
0 1 2 3 4
The longest subsequence is "xx". It appears twice as explained below.
subsequence A
x x
0 1  <-- index of subsequence A
------
1 2  <-- index of s
subsequence B
x x
0 1  <-- index of subsequence B
------
2 3  <-- index of s
We are able to use character 'x' (at index 2 in s) in both subsequencesas it appears on index 1 in subsequence A and index 0 in subsequence B.
"""

def LongestRepeatingSubsequence(s):
    """
    Variation of LCS
    1. find LCS with the string itself
    2. but there is a catch, don't consider the elements if there indexes are same
    3. if indexes are different but element matches then only consider that
    Time Complexity: O(N*N)
    Space Complexity: O(N*N)
    """
    n = len(s)

    t = [[0]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i-1 != j-1 and s[i-1] == s[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i][j-1], t[i-1][j])
    return t[n][n]

s = "AABEBCDD"
print(LongestRepeatingSubsequence(s))