"""
Q. Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
"""

def solve(s, output, ans):
    """
    1. IP-OP method
    2. choices
        i. if char is digit add it as it is
        ii. take char once in upper case
        iii. take char once in lower case
    3. ans will be found at leaf node
    """
    if not s:
        ans.append(output)
        return
    if s[0].isdigit():
        solve(s[1:], output+s[0], ans)
    else:
        solve(s[1:], output+s[0].upper(), ans)
        solve(s[1:], output+s[0].lower(), ans)
    return

s = "a1b2"
ans = []
solve(s, '', ans)
print(ans)