"""
Q. Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target. Each number in candidates may only be used once in the combination.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8

Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]]


Explanation: These are the unique combinations whose sum is equal to target.
 
Example 2:

Input: candidates = [2,5,2,1,2], target = 5

Output: [[1,2,2],[5]]

Explanation: These are the unique combinations whose sum is equal to target.
"""

def combination(candidates, index, target, ans, l, n):
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
        ans.sort()
        if ans not in l:
            l.append(ans)
        return
    
    if target < 0 or index >= n:
        return

    #not pick
    combination(candidates, index+1, target, ans, l, n)
    #pick
    combination(candidates, index+1, target-candidates[index], ans + [candidates[index]], l, n)
    return



def combinationOptimal(candidates, index, target, ans, l, n):
    """
    1. Optimal Approach
    2. base case: if target == 0, add it to ans
    3. base case: if target < 0, return
    4. pick each element, don't consider duplicate
    5. call for each element
    6. Time Complexity: 2^t * k (where t is target, k = average lenght of ans)
    7. Space Complexity: O(k*x) (x is number of combinations)
    """
    if target == 0:
        l.append(ans)
        return
    
    if target < 0:
        return
    for i in range(index, n):
        #remove duplicates
        #i > index this is used to allow duplicates in different positions of our combination, [1,1,2] is a valid combination even though 1 appears twice
        if i > index and candidates[i-1] == candidates[i]:
            continue
        if candidates[i] <= target:
            combinationOptimal(candidates, i+1, target - candidates[i], ans + [candidates[i]], l, n)
    return

candidates = [1,1,1,2,2]
candidates.sort()
target = 4
l = []
n = len(candidates)
combinationOptimal(candidates, 0, target, [], l, n)
print(l)
