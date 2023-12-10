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