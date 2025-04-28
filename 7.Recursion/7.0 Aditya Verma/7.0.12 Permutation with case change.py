"""
Q. Permutation with case change.

Input: s = ab

Output: ab
        aB
        Ab
        AB
"""

def solve(s, output):
    """
    1. IP-OP method
    2. choices
        i. take char once in smallcase
        ii. take char once in uppercase
    3. base case: ans will be found at leaf node
    """
    if not s:
        print(output)
        return
    solve(s[1:], output+s[0])
    solve(s[1:], output+s[0].upper())


s = 'ab'
solve(s, '')