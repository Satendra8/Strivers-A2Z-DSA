"""
Q. You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1
"""

def change(amount, coins):
    """
    Unbounded Knapsack variation
    1. similar as subset sum count
    2. initialize with first row 0 and first col 1
    3. add up all choices
    Time Complexity: O(n*amout)
    Space Complexity: O(n*amout)
    """
    n = len(coins)
    t = [[0] * (amount+1) for _ in range(n+1)]

    for i in range(n+1):
        t[i][0] = 1
    
    for i in range(1, n+1):
        for j in range(amount+1):
            if coins[i-1] <= j:
                t[i][j] = t[i][j-coins[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][amount]


amount = 3
coins = [2]
print(change(amount, coins))
