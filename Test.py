def shortest_distance(matrix):
    """
    Floyd Warshall Algorithm
    1. mark -1 to inf
    2. formula
    A[i][j] = max(A[i][j], A[i][k] + A[k][j])
    3. do this for all vertices
    4. it will use 3 loops
    5. mark inf to -1
    Time Complexity: O(N^3)
    Space Complexity: O(N^2) // we are updating the matrix
    """
    n = len(matrix)
    # mark -1 to inf
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == -1:
                matrix[i][j] = float('inf')

    for via in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][via]+matrix[via][j])

    # mark inf to -1
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == float('inf'):
                matrix[i][j] = -1

    return matrix


mat = [[0, 25], [-1, 0]]
print(shortest_distance(mat))