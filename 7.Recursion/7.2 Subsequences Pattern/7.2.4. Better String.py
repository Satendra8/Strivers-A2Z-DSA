"""
Q. Given a pair of strings of equal lengths, Geek wants to find the better string. The better string is the string having more number of distinct subsequences.
If both the strings have equal count of distinct subsequence then return str1.

Example 1:

Input:
str1 = "gfg", str2 = "ggg"
Output: "gfg"
Explanation: "gfg" have 6 distinct subsequences whereas "ggg" have 3 distinct subsequences. 
Example 2:

Input: str1 = "a", str2 = "b"
Output: "a"
Explanation: Both the strings have only 1 distinct subsequence. 

"""

def subset(s, ans, set1):
    if s == "":
        if ans:
            set1.add(ans)
        return

    subset(s[1:], ans + s[0], set1)
    subset(s[1:], ans, set1)
    return

def subsetCount(s1, s2):
    """
    1. Brute Force Approach
    2. generate all subsequences of both string
    3. compare lenght
    4. return string having larger lenght
    5. Time Complexity: O(2^n)
    6. Space Complexity: O(n (depth of recursion tree) + 2*(all distint string elements))
    """
    set1 = set()
    set2 = set()

    subset(s1, "", set1)
    subset(s2, "", set2)

    if len(set1) >= len(set2):
        return s1
    else:
        return s2


"""Optimal Solution Can be done Using DP"""


s1 = 'gfg'
s2 = 'ggg'
print(subsetCount(s1, s2))