"""
Q. You are given k identical eggs and you have access to a building with n floors labeled from 1 to n.

You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.

Each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.

Return the minimum number of moves that you need to determine with certainty what the value of f is.

Example 1:

Input: k = 1, n = 2
Output: 2
Explanation: 
Drop the egg from floor 1. If it breaks, we know that f = 0.
Otherwise, drop the egg from floor 2. If it breaks, we know that f = 1.
If it does not break, then we know f = 2.
Hence, we need at minimum 2 moves to determine with certainty what the value of f is.
Example 2:

Input: k = 2, n = 6
Output: 3
Example 3:

Input: k = 3, n = 14
Output: 4
"""



def superEggDrop(k, n):
    """
    Variation of MCM
    1. base case 1: if not egg we can't determine
    2. base case 2: if 1 egg we need to make n attempets to determine ans in worst case
    3. base case 3: if 0 floor need 0 attemp, if 1 floor we need 1 attempt
    4. k loop: 1 to n (we need to check at all floors from bottom to top)
    5. problem breakdown in subproblem:
        i. egg break: solve(remaining eggs, floor below f)
        ii. egg not break: solve(eggs, floor above f)
    6. add 1 because making 1 attempt
    7. use min to find minimum no of attempts
    8. use max function: we have to find the laast floor where egg doesn't break, (consider the worst case)
    """
    if k == 1:
        return n
    if n == 0 or n == 1:
        return n

    ans = float('inf')
    for f in range(1, n):
        temp = 1 + max(superEggDrop(k-1, f-1), superEggDrop(k, n-f))
        ans = min(ans, temp)
    return ans

def solveOptimized(k, n, t):
    if k == 1:
        return n
    if n == 0 or n == 1:
        return n
    if t[k][n] != -1:
        return t[k][n]
    ans = float('inf')
    for f in range(1, n):
        if t[k-1][f-1] != -1:
            lf = t[k-1][f-1]
        else:
            lf = solve(k-1, f-1, t)
            t[k-1][f-1] = lf

        if t[k][n-f] != -1:
            rf = t[k][n-f]
        else:
            rf = solve(k, n-f, t)
            t[k][n-f] = rf
        temp = 1 + max(lf, rf)
        ans = min(ans, temp)
    t[k][n] = ans
    return t[k][n]


def solve(k, n, t):
    if k == 1:
        return n
    if n == 0 or n == 1:
        return n
    if t[k][n] != -1:
        return t[k][n]
    ans = float('inf')
    for f in range(1, n):
        temp = 1 + max(solve(k-1, f-1, t), solve(k, n-f, t))
        ans = min(ans, temp)
    t[k][n] = ans
    return t[k][n]


def superEggDropMemoization(k, n):
    """
    Variation of MCM
    1. base case 1: if not egg we can't determine
    2. base case 2: if 1 egg we need to make n attempets to determine ans in worst case
    3. base case 3: if 0 floor need 0 attemp, if 1 floor we need 1 attempt
    4. k loop: 1 to n (we need to check at all floors from bottom to top)
    5. problem breakdown in subproblem:
        i. egg break: solve(remaining eggs, floor below f)
        ii. egg not break: solve(eggs, floor above f)
    6. add 1 because making 1 attempt
    7. use min to find minimum no of attempts
    8. use max function: we have to find the laast floor where egg doesn't break, (consider the worst case)
    9. k and n are variable so make matrix t[k][n]
    """
    t = [[-1] * (n+1) for _ in range(k+1)]
    return solve(k, n, t)
    

k = 2
n = 6
print(superEggDropMemoization(k, n))



"""
Example:

Let’s say you have:

    k = 2 eggs

    n = 4 floors

You want to find the minimum number of attempts needed to determine the critical floor.
Step 1: Drop an egg from floor 2.

    If the egg breaks:

        You now have 1 egg left.

        You need to check floors 1 (below floor 2).

        This will take 1 attempt.

    If the egg doesn't break:

        You still have 2 eggs.

        You need to check floors 3 and 4 (above floor 2).

        This will take 2 attempts.

Now, the max function compares the two scenarios:

    If the egg breaks: 1 attempt.

    If the egg doesn't break: 2 attempts.

The worst-case scenario is 2 attempts (if the egg doesn't break). So, the max function returns 2.
Step 2: Add 1 for the current attempt.

    You dropped the egg from floor 2, so you add 1 to the result of the max function.

    Total attempts: 1 + 2 = 3.
"""