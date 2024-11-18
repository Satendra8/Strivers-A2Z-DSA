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