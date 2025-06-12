"""
Q. Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def lengthOfLongestSubstring(s):
    """
    Sliding Window Variable
    1. if len(d) and window size matches, that can be possible ans
    2. if len(d) < window size, it means repeating character exists, slide the window till duplicate removed
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n = len(s)
    ans = 0
    i = 0
    j = 0
    d = {}

    while j < n:
        if s[j] in d:
            d[s[j]] += 1
        else:
            d[s[j]] = 1
        
        if len(d) == j-i+1:
            ans = max(ans, j-i+1)
            j += 1
        elif len(d) < j-i+1:
            d[s[i]] -= 1
            if d[s[i]] == 0:
                del d[s[i]]
            if len(d) == j-i+1:
                ans = max(ans, j-i+1)
            i += 1
            j += 1
    return ans

s = "pwwkew"
print(lengthOfLongestSubstring(s))