"""
Q. You are given the weights and values of items, and you need to put these items in a knapsack of capacity capacity to achieve the maximum total value in the knapsack. Each item is available in only one quantity.

In other words, you are given two integer arrays val[] and wt[], which represent the values and weights associated with items, respectively. You are also given an integer capacity, which represents the knapsack capacity. Your task is to find the maximum sum of values of a subset of val[] such that the sum of the weights of the corresponding subset is less than or equal to capacity. You cannot break an item; you must either pick the entire item or leave it (0-1 property).

Examples :

Input: capacity = 4, val[] = [1, 2, 3], wt[] = [4, 5, 1] 
Output: 3
Explanation: Choose the last item, which weighs 1 unit and has a value of 3.
Input: capacity = 3, val[] = [1, 2, 3], wt[] = [4, 5, 6] 
Output: 0
Explanation: Every item has a weight exceeding the knapsack's capacity (3).
Input: capacity = 5, val[] = [10, 40, 30, 50], wt[] = [5, 4, 6, 3] 
Output: 50
Explanation: Choose the last item (value 50, weight 3) for a total value of 50.
"""

def knapsackRecursive(capacity, val, wt, n):
    """
    Recursive Approach
    1. write base case for smallest input here n==0, capacity 0
    2. either choose that product either not
    3. keep reducing the input size, here reducing the array
    4. choosing max
    Time Complexity: O(2^N)
    Space Complexity: O(N)
    """
    if n == 0 or capacity == 0:
        return 0
    
    if wt[n-1] <= capacity:
        return max(val[n-1] + knapsackRecursive(capacity-wt[n-1], val, wt, n-1),
                    knapsackRecursive(capacity, val, wt, n-1))
    else:
        return knapsackRecursive(capacity, val, wt, n-1)


def knapsackMemoization(capacity, val, wt, n, t):
    """
    Memoizarion Approach
    1. Same as reursion just storing prev results in a matrix
    Time Complexity: O(N*capacity)
    Space Complexity: O(N*capacity) + O(N) (recursion stack space)
    """
    if n == 0 or capacity == 0:
        return 0
    
    if t[n-1][capacity] != -1:
        return t[n-1][capacity]

    if wt[n-1] <= capacity:
        t[n-1][capacity] = max(val[n-1] + knapsackMemoization(capacity-wt[n-1], val, wt, n-1, t),
                    knapsackMemoization(capacity, val, wt, n-1, t))
        return t[n-1][capacity]
    else:
        t[n-1][capacity] = knapsackMemoization(capacity, val, wt, n-1, t)
        return t[n-1][capacity]


def knapsackTopDownApproach(capacity, val, wt, n):
    """
    Top Down Approach (Derived from Recursive solution)
    1. create 2D matrix for changing variables n, capacity in this case
    1. Initialize first row and col with 0 (replacement of base case)
    2. same as recusrion either choose current element or not
    3. wrap in nested loops and replace n with i and capacity with j
    Time Complexity: O(N*capacity)
    Space Complexity: O(N*capacity)
    """
    t = [[-1] * (capacity+1) for _ in range(n+1)]
    for i in range(n+1):
        t[i][0] = 0
    for j in range(capacity+1):
        t[0][j] = 0
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            if wt[i-1] <= j:
                t[i][j] = max(val[i-1]+t[i-1][j-wt[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[n][capacity]

capacity = 5
val = [10, 40, 30, 50]
wt = [5, 4, 6, 3]
n = 4
print(knapsackTopDownApproach(capacity, val, wt, n))