"""
Q. Given an array of distinct integers and a target, you have to return the list of all unique combinations where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from the given array an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:

Input: array = [2,3,6,7], target = 7

Output: [[2,2,3],[7]]

Explanation: 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
             7 is a candidate, and 7 = 7.
             These are the only two combinations.


Example 2:

Input: array = [2], target = 1

Output: []

Explaination: No combination is possible.
"""


def combination(candidates, index, target, ans, s, n):
    """
    1. base case: if target becomes 0 that is the ans
    2. base case: if target becomes 0 or index exceeds the return
    3. base case: if index exceeds return false
    4. make choice for a[index], pick and move forward
    5. make choice for a[index], not pick and move forward
    6. make choice for a[index], pick and not move forward
    7. ** if i skip pick and move forward part then also it will work correctly
    8. Time Complexity: 2^t * k (where t is target, k = average lenght of ans)
    9. Space Complexity: O(k*x) (x is number of combinations)
    """
    if target == 0:
        # if ans not in l:
        #     l.append(ans) 
        l.append(ans)
        return
    
    if target < 0 or index >= n:
        return
    
    #pick and move forward
    # combination(candidates, index+1, target-candidates[index], ans + [candidates[index]], s, n)
    #not pick and move forward
    combination(candidates, index+1, target, ans, s, n)
    #pick and not move forward
    combination(candidates, index, target-candidates[index], ans + [candidates[index]], s, n)
    return

"""Optimal Solution Can be done Using DP"""
candidates = [2,3,6,7]
target = 7
l = []
n = len(candidates)
combination(candidates, 0, target, [], l, n)
print(l)
