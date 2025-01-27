"""
Difference from 0/1 Knapcask:


we have 2 options
    1. take      (item can be taken again)
    2. not take  (processed)

In 0/1 knapsack item cannot be taken more than once

But In unbounded knapsack item can be taken multiple times
"""

def knapsack(val, wt, W, n):
    t = [[0]*(W+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, W+1):
            if wt[i-1] <= j:
                t[i][j] = max(val[i-1]+t[i-1][j-wt[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[n][W]

wt = [1,3,4,5]
val = [1,4,5,7]
W = 7
n = len(val)
print(knapsack(val, wt, W, n))


def unboundedKnapsack(val, wt, W, n):
    t = [[0]*(W+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, W+1):
            if wt[i-1] <= j:
                # same value can be taken again
                t[i][j] = max(val[i-1]+t[i][j-wt[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[n][W]