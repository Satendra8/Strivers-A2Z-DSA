"""
Q. Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""

def generate(open, close, output, ans):
    if open == 0 and close == 0:
        ans.append(output)
        return
    if open > 0:
        generate(open-1, close, output+'(', ans)
    if close > open:
        generate(open, close-1, output+')', ans)
    return


n = 3
ans = []
open = n
close = n
generate(open, close, '', ans)
print(ans)