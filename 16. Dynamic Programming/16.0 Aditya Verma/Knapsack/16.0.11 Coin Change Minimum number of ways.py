"""
Q. You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
"""


def coinChange(coins, amount):
    """
    Unbounded Knapsack Variation
    1. Initialization
        -> initialize first row with Infinite,
           because it is impossible to pick elements from empty arr
        -> initialize first col expect i=0 with 0
           because if i want sum=0, i will get it by not choosing any coin
    2. There is a edge case if we have coin with value 3 and we want sum 4 then
        this is not achievable hence infinite
    3. This problem requires initialization of second col, due to above exception
    4. min (1 + call for n elements, call for n-1 elements)
    Time Complexity: O(n * amount)
    Space Complexity: O(n * amount)
    """
    n = len(coins)
    t = [[-1] * (amount+1) for _ in range(n+1)]
    INT_MAX = float('inf') - 1 # adding 1 will make -ve

    for i in range(n+1):
        t[i][0] = 0

    for j in range(amount+1):
        t[0][j] = INT_MAX

    for j in range(1, amount+1):
        if j % coins[0] == 0:
            t[1][j] = j // coins[0]
        else:
            t[1][j] = INT_MAX
    

    for i in range(1, n+1):
        for j in range(1, amount+1):
            if coins[i-1] <= j:
                t[i][j] = min(1+ t[i][j-coins[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]

    for i in range(n+1):
        for j in range(amount+1):
            if t[i][j] == float('inf'):
                t[i][j] = -1
    return t[n][amount]


coins = [1]
amount = 3
print(coinChange(coins, amount))