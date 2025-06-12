"""
Q. Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""

def minWindow(s, t):
    """
    1. Sliding Window variable
    2. expand the window until all characters are covered
    3. once all covered shrink the window by incrementing i
    4. keep updating the ans
    5. once any character is missing move the j pointer
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n = len(s)
    i = 0
    j = 0
    d = {}
    count = len(t)
    ans = ""
    for c in t:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    while j < n:
        if s[j] in d:
            d[s[j]] -= 1
            if d[s[j]] >= 0:
                count -= 1
            if count == 0:
                while count == 0:
                    if ans == "" or len(ans) > j-i+1:
                        ans = s[i:j+1]
                    if s[i] in d:
                        d[s[i]] += 1
                        if d[s[i]] >= 1:
                            count += 1
                    i += 1
        j += 1
    return ans

s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))


"""
s = "ADOBECODEBANC"
t = "ABC"
j = 0
i = 0
d = {}
count = 3
ans = 0
"""
