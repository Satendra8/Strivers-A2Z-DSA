"""
Q. Given an array arr[], partition it into two subsets(possibly empty) such that each element must belong to only one subset. Let the sum of the elements of these two subsets be sum1 and sum2. Given a difference d, count the number of partitions in which sum1 is greater than or equal to sum2 and the difference between sum1 and sum2 is equal to d. 

Examples :

Input: arr[] =  [5, 2, 6, 4], d = 3
Output: 1
Explanation: There is only one possible partition of this array. Partition : {6, 4}, {5, 2}. The subset difference between subset sum is: (6 + 4) - (5 + 2) = 3.
Input: arr[] = [1, 1, 1, 1], d = 0 
Output: 6 
Explanation: We can choose two 1's from indices {0,1}, {0,2}, {0,3}, {1,2}, {1,3}, {2,3} and put them in sum1 and remaning two 1's in sum2.
Thus there are total 6 ways for partition the array arr. 
Input: arr[] = [1, 2, 1, 0, 1, 3, 3], d = 11
Output: 2
"""
import math
def countSubSetSum(arr, target):
    n = len(arr)
    t = [[0] * (target+1) for _ in range(n+1)]

    for i in range(n+1):
        t[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, target+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][target]


def countPartitions(arr, d):
    """
    1. arr is partitioned into s1 and s2
    2. sum(s1) - sum(s2) = d ------ eq1
 +  3. sum(s1) + sum(s2) = sum(arr) ------ eq2
    -------------------------------------------
    4. sum(s1) = d + sum(arr)
                --------------
                     2
    5. edge case: if (d+sum(s1)) is not divisible by 2 then partition is not possible
    6. problem is boiled down into count subset with given sum
    Time Complexity: O(n*target)
    Space Complexity: O(n*target)
    """
    target = d + sum(arr)

    if target % 2 == 1:
        return 0
    target = target//2
    return countSubSetSum(arr, target)

arr = [1, 3, 3, 2, 1]
d = 5
print(countPartitions(arr, d))