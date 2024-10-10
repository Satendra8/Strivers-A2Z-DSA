"""
Q. Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""


def longestPalindrome(s):
    """
    1. Brute Force Approach
    2. generate all substring
    3. check it and it's reverse are same
    4. store max length substr
    5. Time Complexity - O(N^3)
    6. Space Complexity - O(N) for storing substr
    """
    n = len(s)
    ans = ""
    for i in range(n):
        for j in range(n):
            substr = s[i: j+1]
            print("substr =>", substr)
            if substr == substr[::-1]:
                if len(substr) > len(ans):
                    ans = substr

    return ans

s = "babad"
print(longestPalindrome(s))




def longestPalindrome(self, s: str) -> str:
    """
1. Optimal Approach
2. take two variables forward and reverse
3. iterate for all substrings
4. compare forward and reverse and update count
5. Time Complexity - O(N^2)
6. Space Complexity - O(N) for storing substr
    """
    n = len(s)
    ans = ""
    for i in range(n):
        forward = ""
        reverse = ""
        for j in range(i, n):
            forward += s[j]
            reverse = s[j] + reverse
            # print("forward, reverse ====>", forward, reverse)
            if reverse == forward:
                if len(forward) > len(ans):
                    ans = forward
    return ans