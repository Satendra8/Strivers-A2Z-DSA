"""
Q. You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
def fib(n, dp):
    if n <= 1: return 1
    if dp[n] != -1: return dp[n]

    dp[n] = fib(n-1, dp) + fib(n-2, dp)
    return dp[n]

def climbStairs(n):
    """
    Using Dynamic Programming
    1. Try to represent the problems in terms of index
    2. Do all possible steps for that index according to problem statement
    3. sum of all stuffs -> count all ways
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    dp = [-1]*(n+1)
    return fib(n, dp)

n = 3
print(climbStairs(n))