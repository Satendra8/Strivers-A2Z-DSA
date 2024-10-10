"""
Q. You are given an array 'A' of 'N' integers. You have to return true if there exists a subset of elements of 'A' that sums up to 'K'. Otherwise, return false.

For Example
'N' = 3, 'K' = 5, 'A' = [1, 2, 3].
Subset [2, 3] has sum equal to 'K'.
So our answer is True.

Sample Input 1 :
4 13
4 3 5 2
Sample Output 1 :
No
Sample Input 2 :
5 14
4 2 5 6 7
Sample Output 2 :
Yes

"""

def subset(a, index, summ, n, k):
    """
    1. base case: if summ == k return true
    2. base case: if summ > k return false
    3. base case: if index exceeds return false
    4. make choice for a[0], add to sum
    5. make choice for a[0], don't add
    6. if true found at any moment return it
    """
    if summ == k:
        return True

    if summ > k:
        return False
    
    if index >= n:
        return False

    first = subset(a, index+1, summ, n, k)
    if first:
        return first
    second = subset(a, index+1, summ+a[index], n, k)
    if second:
        return second
    return False

def isSubsetPresent(n, k, a):
    return subset(a, 0, 0, n, k)

"""Optimal Solution Can be done Using DP"""

a = [4,2,5,6,7]
N = len(a)
K = 14
print(isSubsetPresent(N, K, a))