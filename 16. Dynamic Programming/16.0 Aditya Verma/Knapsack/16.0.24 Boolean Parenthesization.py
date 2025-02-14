"""
Q. Given a boolean expression s with following symbols.
    'T' ---> true
    'F' ---> false
and following operators between symbols
   &   ---> boolean AND
    |   ---> boolean OR
   ^   ---> boolean XOR
Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.

Note: The answer is guaranteed to fit within a 32-bit integer.

Examples:

Input: s = "T|T&F^T"
Output: 4
Explaination: The expression evaluates to true in 4 ways: ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T) and (T|((T&F)^T)).
Input: s = "T^F|F"
Output: 2
Explaination: The expression evaluates to true in 2 ways: ((T^F)|F) and (T^(F|F)).
"""

def solve(s, i, j, isTrue):
    if i > j:
        return 0
    if i == j:
        if isTrue == True:
            if s[i] == 'T':
                return 1
            else:
                return 0
        else:
            if s[i] == 'F':
                return 1
            else:
                return 0
    
    ans = 0
    for k in range(i+1, j, 2):
        lt = solve(s, i, k-1, True)
        lf = solve(s, i, k-1, False)
        rt = solve(s, k+1, j, True)
        rf = solve(s, k+1, j, False)

        if s[k] == '|':
            if isTrue == True:
                ans += lt * rf + lf * rt + lt * rt
            else:
                ans += lf * rf
        elif s[k] == '&':
            if isTrue == True:
                ans += lt * rt
            else:
                ans += lt * rf + rf * rt + lf * rf
        elif s[k] == '^':
            if isTrue == True:
                ans += lt * rf + lf * rt
            else:
                ans += lf * rf + lt * rt
    return ans


def countWays(s):
    """
    Variation of MCM
    1. find i and j: operation on whole string i = 0, j = n-1
    2. base case: if string is empty 0 count
    3. base case: if single char, if we need True and char is 'T' return 1 else 0, same for False case
    4. k loop: k loop running for operand, so k (i+1, j) and k + 2 jump to get operand
    5. partition: (i, k-1) k(opernad) (k+1, j) # partitioning at k (operand)
    6. only 3 operand (|, &, ^) possible, using their truth table
    7. main edge case: we need to count the ways to False as well, because T ^ F = T
    """
    n = len(s)
    return solve(s, 0, n-1, True)


def solveMemoization(s, i, j, isTrue, mp):
    if i > j:
        return 0
    if i == j:
        if isTrue == True:
            if s[i] == 'T':
                return 1
            else:
                return 0
        else:
            if s[i] == 'F':
                return 1
            else:
                return 0
    key = f'{i}_{j}_{isTrue}'
    if key in mp:
        return mp.get(key)
    ans = 0
    for k in range(i+1, j, 2):
        lt = solveMemoization(s, i, k-1, True, mp)
        lf = solveMemoization(s, i, k-1, False, mp)
        rt = solveMemoization(s, k+1, j, True, mp)
        rf = solveMemoization(s, k+1, j, False, mp)

        if s[k] == '|':
            if isTrue == True:
                ans += lt * rf + lf * rt + lt * rt
            else:
                ans += lf * rf
        elif s[k] == '&':
            if isTrue == True:
                ans += lt * rt
            else:
                ans += lt * rf + rf * rt + lf * rf
        elif s[k] == '^':
            if isTrue == True:
                ans += lt * rf + lf * rt
            else:
                ans += lf * rf + lt * rt
    mp[key] = ans
    return ans


def countWaysMemoization(s):
    """
    Variation of MCM
    1. find i and j: operation on whole string i = 0, j = n-1
    2. base case: if string is empty 0 count
    3. base case: if single char, if we need True and char is 'T' return 1 else 0, same for False case
    4. k loop: k loop running for operand, so k (i+1, j) and k + 2 jump to get operand
    5. partition: (i, k-1) k(opernad) (k+1, j) # partitioning at k (operand)
    6. only 3 operand (|, &, ^) possible, using their truth table
    7. main edge case: we need to count the ways to False as well, because T ^ F = T
    8. table formation: here i, j and isTrue are changing, so 3D matrix is required
    9. 3D matrix is difficult to imagine, using map instead
    """
    n = len(s)
    mp = dict()
    return solveMemoization(s, 0, n-1, True, mp)

s = "T^F|F"
print(countWaysMemoization(s))


"""
use @lru_cache(None) for optimization
"""