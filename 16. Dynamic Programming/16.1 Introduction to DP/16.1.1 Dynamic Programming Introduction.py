"""
Fibonacci Series: 0 1 1 2 3 5 8 13 21 .......
1. Recursion


"""

def fib(n):
    """
    Recursive Approach
    Time Complexity: O(2^n-1)
    Space Complexity: O(2^n-1)
    """
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


def fibMemoization(n, dp):
    """
    Dynamic Programming (Memoization) (Top Down Approach) required ans -----> base case
    Time Complexity: O(N)
    Space Complexity: O(N) + O(N)
    """
    if n <= 1:
        return n
    if dp[n] != -1: return dp[n]
    dp[n] = fibMemoization(n-1, dp) + fibMemoization(n-2, dp)
    return dp[n]


def fibTabulation(n, dp):
    """
    Dynamic Programming (Tabulation Format) (Bottom Approach) base case -----> required ans
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def fibOptimal(n):
    """
    Iterative Approach (More space optimization)
    1. take 2 variable to keep previous instead array
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    prev1 = 0
    #edge case
    if n == 0:
        return 0
    prev2 = 1

    for i in range(2, n+1):
        temp = prev1
        prev1 = prev2
        prev2 = prev2 + temp
    return prev2


n = 0
dp = [-1]*(n+1)
print(fibOptimal(n))