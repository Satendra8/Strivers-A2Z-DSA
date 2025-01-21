def subsetSumRecusive(arr, target, n):
    """
    Variation of 0-1 knapsack (DP)
    1. base case: if target is 0 then we can return true as we can make empty subset by not choosing any element
    2. if no elements left but target > 0 then return false
    3. if element <= target, either choose element either not choose
    4. if element > target not choose element
    Time Complexity: O(2^N)
    Space Complexity: O(N)
    """
    if n == 0 and target == 0:
        return True
    if n == 0:
        return False
    if target == 0:
        return True
    
    if arr[n-1] <= target:
        return subsetSumRecusive(arr, target-arr[n-1], n-1) or subsetSumRecusive(arr, target, n-1)
    else:
        return subsetSumRecusive(arr, target, n-1)



def subsetSumMemoization(arr, target, n, t):
    """
    Variation of 0-1 knapsack (DP)
    1. base case: if target is 0 then we can return true as we can make empty subset by not choosing any element
    2. if no elements left but target > 0 then return false
    3. if element <= target, either choose element either not choose
    4. if element > target not choose element
    5. storing the previous element
    Time Complexity: O(target*N)
    Space Complexity: O(target*N)
    """
    if n == 0 and target == 0:
        return True
    if n == 0:
        return False
    if target == 0:
        return True
    
    if t[n-1][target] != -1:
        return t[n-1][target]

    if arr[n-1] <= target:
        t[n-1][target] = subsetSumRecusive(arr, target-arr[n-1], n-1) or subsetSumRecusive(arr, target, n-1)
        return t[n-1][target]
    else:
        t[n-1][target] = subsetSumRecusive(arr, target, n-1)
        return t[n-1][target]


def subsetSumTopDownApproach(arr, target, n, t):
    """
    Top Down Approach: just replace n with i and target with j
    1. initialization: first row will be false because we cannot get 1,2,3... with n=0 (empty array)
    2. first column will be true because we can get target 0 by not choosing any element
    3. use nested loop and simply convert memoization into Top Down
    Time Complexity: O(target*N)
    Space Complexity: O(target*N) # removing recursion stack space here
    
    """
    for j in range(target+1):
        t[0][j] = False
    for i in range(n+1):
        t[i][0] = True

    for i in range(1, n+1):
        for j in range(1, target+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]

    return t[n][target]

arr = [3, 34, 4, 12, 5, 2]
target = 12
n = len(arr)
t = [[-1] * (target+1) for _ in range(n+1)]
print(subsetSumTopDownApproach(arr, target, n, t))