"""
Q. Given a positive integer n. Your task is to generate a string list of all n-bit binary numbers where, for any prefix of the number, there are more or an equal number of 1's than 0's. The numbers should be sorted in decreasing order of magnitude.

Example 1:

Input:  
n = 2
Output: 
{"11", "10"}
Explanation: Valid numbers are those where each prefix has more 1s than 0s:
11: all its prefixes (1 and 11) have more 1s than 0s.
10: all its prefixes (1 and 10) have more 1s than 0s.
So, the output is "11, 10".
Example 2:

Input:  
n = 3
Output: 
{"111", "110", "101"}
Explanation: Valid numbers are those where each prefix has more 1s than 0s.
111: all its prefixes (1, 11, and 111) have more 1s than 0s.
110: all its prefixes (1, 11, and 110) have more 1s than 0s.
101: all its prefixes (1, 10, and 101) have more 1s than 0s.
So, the output is "111, 110, 101".
"""

def solve(n, one, zero, output, ans):
    """
    1. IP-OP method
    2. choices either take 0 or 1
    3. we can't take 0 as prefix as said in question
    4. if one > zero then only we can take 0
    5. choice for 1 is always available
    """
    if n == 0:
        ans.append(output)
        return
    solve(n-1, one+1, zero, output+'1', ans)
    if one > zero:
        solve(n-1, one, zero+1, output+'0', ans)
    return

n = 3
ans = []
one = 0
zero = 0
solve(n, one, zero, '', ans)
print(ans)