"""
Q. Given an array arr[] which represents dimensions of sequence of matrices where the ith matrix has the dimensions (arr[i-1] x arr[i]) for i>=1., find the most efficient way to multiply these matrices together. The efficient way is the one that involves the least number of multiplications.

Examples:

Input: arr[] = [2, 1, 3, 4]
Output: 20
Explanation: There are 3 matrices of dimensions 2 × 1, 1 × 3, and 3 × 4, Let the input 3 matrices be M1, M2, and M3. There are two ways to multiply: ((M1 x M2) x M3) and (M1 x (M2 x M3)), note that the result of (M1 x M2) is a 2 x 3 matrix and result of (M2 x M3) is a 1 x 4 matrix. 
((M1 x M2) x M3)  requires (2 x 1 x 3)  + (0) +  (2 x 3 x 4) = 30 
(M1 x (M2 x M3))  requires (0)  + (1 x 3 x 4) +  (2 x 1 x 4) = 20. 
The minimum of these two is 20.
Input: arr[] = [1, 2, 3, 4, 3]
Output: 30
Explanation: There are 4 matrices of dimensions 1 × 2, 2 × 3, 3 × 4, 4 × 3. Let the input 4 matrices be M1, M2, M3 and M4. The minimum number of multiplications are obtained by ((M1 x M2) x M3) x M4). The minimum number is (1 x 2 x 3) + (1 x 3 x 4) + (1 x 4 x 3) = 30.
Input: arr[] = [3, 4]
Output: 0
Explanation: As there is only one matrix so, there is no cost of multiplication.
"""


def solve(arr, i, j, t):
    if i >= j:
        return 0
    if t[i][j] != -1:
        return t[i][j]

    ans = float('inf')
    for k in range(i, j):
        temp = solve(arr, i, k, t) + solve(arr, k+1, j, t) + arr[i-1] * arr[k] * arr[j]
        ans = min(temp, ans)
    t[i][j] = ans
    return t[i][j]


def matrixMultiplication(arr):
    """
           0  1  2  3
    arr = [2, 1, 3, 4]
    A1 = 2 x 1 = arr[i-1] x arr[i]
    A2 = 1 x 3
    A3 = 3 x 4
    1. find i, j: i will be 1 to n
    2. base condition: i >= j (multiplication is not possible with single arr element)
    3. find k loop scheme: breaking into (i, k) (k+1, j) (loop i to j-1)
    4. find extra cost: arr[i-1] * arr[k] * arr[j] = first element * breaking point element * last element
    5. update minimum
    """
    n = len(arr)
    t = [[-1] * (n+1) for _ in range(n+1)]
    return solve(arr, 1, n-1, t)




def matrixMultiplicationRecursive(arr, i, j):
    """
           0  1  2  3
    arr = [2, 1, 3, 4]
    A1 = 2 x 1 = arr[i-1] x arr[i]
    A2 = 1 x 3
    A3 = 3 x 4
    1. find i, j: i will be 1 to n
    2. base condition: i >= j (multiplication is not possible with single arr element)
    3. find k loop scheme: breaking into (i, k) (k+1, j) (loop i to j-1)
    4. find extra cost: arr[i-1] * arr[k] * arr[j] = first element * breaking point element * last element
    5. update minimum
    """

    if i >= j:
        return 0
    
    ans = float('inf')
    for k in range(i, j):
        temp = matrixMultiplicationRecursive(arr, i, k) + matrixMultiplicationRecursive(arr, k+1, j) + arr[i-1] * arr[k] * arr[j]
        ans = min(temp, ans)
    return ans


arr = [1, 2, 3, 4, 3]
print(matrixMultiplication(arr))
