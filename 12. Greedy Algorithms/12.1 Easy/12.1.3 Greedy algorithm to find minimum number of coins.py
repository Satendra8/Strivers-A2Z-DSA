"""
Q. Given an array of coins[] of size n and a target value sum, where coins[i] represent the coins of different denominations. You have an infinite supply of each of the coins. The task is to find the minimum number of coins required to make the given value sum. If it’s not possible to make a change, return -1.


Input: coins[] = [25, 10, 5], sum = 30
Output: 2
Explanation : Minimum 2 coins needed, 25 and 5  


Input: coins[] = [9, 6, 5, 1], sum = 19
Output: 3
Explanation: 19 = 9 + 9 + 1


Input: coins[] = [5, 1], sum = 0
Output: 0
Explanation: For 0 sum, we do not need a coin


Input: coins[] = [4, 6, 2], sum = 5
Output: -1
Explanation: Not possible to make the given sum.
"""

def minimumCoins(coins, summ):
    """
    1. Sort the array in reverse order
    2. pick the larger coin and keep subtracting it from number
    3. keep counting the coins
    4. if summ becomes 0 return ans
    5. return -1 if coins not fulfill summ
    Time Complexity: O(NlogN)
    Space Complexity: O(1)
    """
    coins.sort(reverse = True)
    ans = 0
    for coin in coins:
        while summ >= coin:
            summ -= coin
            ans += 1
    if summ == 0:
        return ans
    return -1


coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
summ = 49
print(minimumCoins(coins, summ))