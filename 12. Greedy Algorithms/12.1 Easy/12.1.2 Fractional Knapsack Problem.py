"""
Q. The weight of N items and their corresponding values are given. We have to put these items in a knapsack of weight W such that the total value obtained is maximized.

Note: We can either take the item as a whole or break it into smaller units.

Example:

Input: N = 3, W = 50, values[] = {100,60,120}, weight[] = {20,10,30}.

Output: 240.00

Explanation: The first and second items  are taken as a whole  while only 20 units of the third item is taken. Total value = 100 + 60 + 80 = 240.00

"""

def fractionalknapsack(val, wt, capacity):
    """
    1. Calculate the unit price
    2. sort the array of unit price in descending order
    3. pick element with highest unit price first and keep reducing the capacity
    4. when weight is more than capacity take required fraction and make capacity 0
    5. return summ of profit
    Time Complexity: O(NlogN+N)
    Space Complexity: O(N)
    """
    n = len(val)
    maxx = 0
    profit = []
    for i in range(n):
        profit.append((val[i]/wt[i], i))
    profit.sort(reverse=True)
    for j in range(len(profit)):
        index = profit[j][1]
        if capacity <= 0:
            break
        if wt[index] > capacity:
            maxx += round(val[index]/wt[index],6) * capacity
            capacity = 0
        else:
            maxx += val[index]
            capacity -= wt[index]

    return maxx

val = [1, 5, 7, 2, 7, 10]
wt = [4, 9, 6, 3, 7, 3]
capacity = 24
print(fractionalknapsack(val, wt, capacity))