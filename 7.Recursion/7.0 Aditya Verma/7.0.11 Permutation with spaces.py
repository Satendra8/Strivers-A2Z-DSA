"""
Q. Given a string s, you need to print all possible strings that can be made by placing spaces (zero or one) in between them. The output should be printed in sorted increasing order of strings.

Example 1:

Input:
s = "ABC"
Output: (A B C)(A BC)(AB C)(ABC)
Explanation:
ABC
AB C
A BC
A B C
These are the possible combination of "ABC".
Example 2:

Input:
s = "BBR"
Output: (B B R)(B BR)(BB R)(BBR)
"""

def solve(s, output, ans):
    """
    1. IP-OP method
    2. add next letter with space
    3. don't add next letter with space
    4. base case: ans will be found at leaf node
    """
    if not s:
        ans.append(output)
        return
    solve(s[1:], output+s[0], ans)
    if output:
        solve(s[1:], output+" "+s[0], ans)
    return

s = "BBR"
ans = []
solve(s, '', ans)
print(ans)