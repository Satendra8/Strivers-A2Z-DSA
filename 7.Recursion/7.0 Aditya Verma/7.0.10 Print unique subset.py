"""
Q. Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""

def subset(s, output, ans):
    """
    1. IP-OP method
    2. base case: ans will be at leaf node, if input become empty
    3. make choices
        i. take arr[0] in output
        ii. not take arr[0]
    """
    if not s:
        ans.add(output)
        return
    subset(s[1:], output, ans)
    subset(s[1:], output+s[0], ans)
    return

s = 'aab'
ans = set()
subset(s, '', ans)
print(ans)