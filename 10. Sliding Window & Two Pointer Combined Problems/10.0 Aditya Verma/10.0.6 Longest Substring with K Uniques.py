"""
Q. Given a string s, you need to print the size of the longest possible substring with exactly k unique characters. If no possible substring exists, print -1.

Examples:

Input: s = "aabacbebebe", k = 3
Output: 7
Explanation: "cbebebe" is the longest substring with 3 distinct characters.
Input: s = "aaaa", k = 2
Output: -1
Explanation: There's no substring with 2 distinct characters.
Input: s = "aabaaab", k = 2
Output: 7
Explanation: "aabaaab" is the longest substring with 2 distinct characters.
"""


def longestKSubstr(s, k):
    """
    Sliding Window Variable
    1. keep expanding window till unique characters len become k
    2. if len == k, then uppdate len
    3. if len exceeds then remove from left and slide the window
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n = len(s)
    ans = -1
    i = 0
    j = 0
    d = {}

    while j < n:
        if s[j] in d:
            d[s[j]] += 1
        else:
            d[s[j]] = 1
        if len(d) == k:
            ans = max(ans, j-i+1)
        elif len(d) > k:
            while len(d) > k:
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    del d[s[i]]
                i += 1
            if len(d) == k:
                ans = max(ans, j-i+1)
        j += 1
    return ans


s = "aabaaab"
k = 2
print(longestKSubstr(s, k))

"""
s = "aabacbebebe"
k = 3
n = 11
j = 5
i = 0
d = {a:0, b:1, c:1, e:1}
ans = 6
"""