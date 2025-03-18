"""
Q. Given a string s, which may contain duplicate characters, your task is to generate and return an array of all unique permutations of the string. You can return your answer in any order.

Examples:

Input: s = "ABC"
Output: ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
Explanation: Given string ABC has 6 unique permutations.
Input: s = "ABSG"
Output: ["ABGS", "ABSG", "AGBS", "AGSB", "ASBG", "ASGB", "BAGS", "BASG", "BGAS", "BGSA", "BSAG", "BSGA", "GABS", "GASB", "GBAS", "GBSA", "GSAB", "GSBA", "SABG", "SAGB", "SBAG", "SBGA", "SGAB", "SGBA"]
Explanation: Given string ABSG has 24 unique permutations.
Input: s = "AAA"
Output: ["AAA"]
Explanation: No other unique permutations can be formed as all the characters are same.
"""


def findPermutation (s, ans, l):
    """
    1. If duplicate exist in input string recursion will not work
    2. we need controlled recursion here (BackTracking)
    3. use I/P, O/P method, to create recursion tree
    Time Complexity: O(nxn!)
    Space Complexity: O(nxn!)
    """
    if s == "":
        l.append(ans)
        return
    # ignoring duplicates -> controlled recursion (backtracking)
    st = set()
    for i in range(len(s)):
        if s[i] not in st:
            st.add(s[i])
            findPermutation(s[0:i]+s[i+1:], ans+s[i], l)

s = "ABC"
l = []
findPermutation(s, "", l)
print(l)