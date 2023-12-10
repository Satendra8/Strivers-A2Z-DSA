"""
Q. Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
"""


def is_isomorphic(s, t):
    """
    1. Better Approach
    2. check if lenght not matches return false
    3. loop over and store key and value as s->t, if s[i] already mapped with other value previously return false
    4. loop over again and store key and value as t->s, if t[i] already mapped with other value previously return false
    5. Time Complexity - O(N)
    6. Space Complexity - O(1) # because max dict lenght will be 26 always 
    """
    if len(s) != len(t):
        return False
    n = len(s)
    d = {}
    
    for i in range(n):
        if s[i] in d and d[s[i]] != t[i]:
            return False
        d[s[i]] = t[i]
    d.clear()
    for i in range(n):
        if t[i] in d and d[t[i]] != s[i]:
            return False
        d[t[i]] = s[i]
    return True
s = "badc"
t = "baba"
print(is_isomorphic(s, t))