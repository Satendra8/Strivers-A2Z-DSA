"""
Q. You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
"""


def countSubSetSum(arr, target):
    n = len(arr)
    t = [[0] * (target+1) for _ in range(n+1)]

    for i in range(n+1):
        t[i][0] = 1

    for i in range(1, n+1):
        for j in range(target+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][target]

def findTargetSumWays(nums, target):
    """
    nums = [1, 1, 2, 3], target = 1
        +1, -1, -2, +3
              /   \
             /     \
        -1, -2    +1, +3
          s1         s2
    s1 - s2 = target (Problem is boiled down into Count the number of subset with given difference)
    edge case: count 0 too
    edge case: susbset sum cannot be 0, so check target < 0
    Time Complexity: O(n*target)
    Space Complexity: O(n*target)
    """
    target = target + sum(nums)

    if target % 2 == 1 or target < 0:
        return 0
    target = abs(target//2)
    print(target)
    return countSubSetSum(nums, target)

nums = [100, 100]
target = -400
print(findTargetSumWays(nums, target))