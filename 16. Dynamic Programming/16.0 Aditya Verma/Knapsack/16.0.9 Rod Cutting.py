"""
Q. Given a rod of length n(size of price) inches and an array of prices, price. price[i] denotes the value of a piece of length i. Determine the maximum value obtainable by cutting up the rod and selling the pieces.

Example:

Input: price[] = [1, 5, 8, 9, 10, 17, 17, 20]
Output: 22
Explanation: The maximum obtainable value is 22 by cutting in two pieces of lengths 2 and 6, i.e., 5+17=22.

Input: price[] = [3, 5, 8, 9, 10, 17, 17, 20]
Output: 24
Explanation: The maximum obtainable value is 24 by cutting the rod into 8 pieces of length 1, i.e, 8*price[1]= 8*3 = 24.

Input: price[] = [1, 10, 3, 1, 3, 1, 5, 9]
Output: 40
"""

def cutRodRecursive(price, length, target, n):
    """
    Variation of Unbound Knapsack
    1. same item can be selected multiple times
    2. if lenght of current element is less then target
        i. select (this can be selected again, so don't reduce n)
        ii. not select
    3. if target exceeds, don't select
    Time Complexity: O(2^n)
    Space Complexity: O(n)
    """
    if n==0 or target == 0:
        return 0
    
    if length[n-1] <= target:
        return max(price[n-1] + cutRodRecursive(price, length, target-length[n-1], n), cutRodRecursive(price, length, target, n-1))
    else:
        return cutRodRecursive(price, length, target, n-1)


def cutRod(price):
    """
    Variation of Unbound Knapsack
    1. same item can be selected multiple times
    2. if lenght of current element is less then target
        i. select (this can be selected again, so don't reduce n)
        ii. not select
    3. if target exceeds, don't select
    Time Complexity: O(n*n)
    Space Complexity: O(n*n)
    """
    n = len(price)
    length = [i for i in range(1, n+1)]
    target = n

    t = [[0] * (target+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, target+1):
            if length[i-1] <= j:
                t[i][j] = max(price[i-1] + t[i][j - length[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[n][target]


price = [3, 5, 8, 9, 10, 17, 17, 20]
n = len(price)
length = [i for i in range(1, n+1)]
print(cutRod(price))