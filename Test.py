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