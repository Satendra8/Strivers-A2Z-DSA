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

def subset(arr, ans, output):
    """
    1. IP-OP method
    2. base case: ans will be at leaf node, if input become empty
    3. make choices
        i. take arr[0] in output
        ii. not take arr[0]
    """
    if not arr:
        ans.append(output.copy())
        return
    subset(arr[1:], ans, output)
    output.append(arr[0])
    subset(arr[1:], ans, output)
    output.pop()
    return

arr = [1, 2, 3]
ans = []
subset(arr, ans, [])
ans.sort()
print(ans)