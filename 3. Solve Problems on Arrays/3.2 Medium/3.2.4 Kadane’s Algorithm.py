"""
Q. Given an integer array arr, find the contiguous subarray (containing at least one number) which
has the largest sum and returns its sum and prints the subarray.

Example 1:

Input: arr = [-2,1,-3,4,-1,2,1,-5,4] 

Output: 6 

Explanation: [4,-1,2,1] has the largest sum = 6. 

Examples 2: 

Input: arr = [1] 

Output: 1 

Explanation: Array has only one element and which is giving positive sum of 1. 

"""

def maxSum(arr):
    """
    Brute Force Approach
    1. Generate all possible subarray
    2. Use 3 nested loop
    3. (i, j+1) and on loop k for adding element b/w these indexes.

    Time Complexity: O(n^3)
    Space Complexity: O(1)
    """

    n = len(arr)
    max_sum = 0
    
    for i in range(n):
        for j in range(i,n):
            summ = 0
            for k in range(i,j+1):
                summ += arr[k]
            max_sum = max(max_sum, summ)

    return max_sum


def maxSum(arr):
    """
    Better Force Approach
    1. Generate all possible subarray
    2. Use 2 nested loop
    3. The sum will be pre_sum + arr[j], this reduces a loop

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    n = len(arr)
    max_sum = 0
    
    for i in range(n):
        summ = 0
        for j in range(i,n):
            summ += arr[j]
            max_sum = max(max_sum, summ)

    return max_sum


def kadanesAlgorithm(arr):
    """
    Optimal Approach
    1. Use Kadane's Algorithm
    2. add consequtive elements
    3. if summ < 0, no need to consider the element, make summ = 0
    4. update the maxSum

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    n = len(arr)
    summ = 0
    maxSum = 0
    for i in arr:
        
        if summ < 0:
            summ = 0
        summ += i
        maxSum = max(summ, maxSum)
    return maxSum
arr = [-2,-3,4,-1,-2,1,5,-3]
print(kadanesAlgorithm(arr))


"""
Follow-Up Question

There might be more than one subarray with the maximum sum. We need to print any of them.

"""
import sys
def kadanesAlgorithmFollowUp(arr):
    """
    Optimal Approach
    1. Use Kadane's Algorithm
    2. add consequtive elements
    3. if summ < 0, no need to consider the element, make summ = 0 and first = i
    4. update the maxSum
    5. update last = i
    6. print elements from first to last
    """
    n = len(arr)
    
    summ = 0
    maxSum = -sys.maxsize - 1
    first = 0
    last = 0
    
    for i in range(n):

        if summ < 0:
            first = i
            summ = 0
        summ += arr[i]
        
        if summ > maxSum:
            last = i
            maxSum = summ
    for i in range(first, last + 1):
        print(arr[i], end=" ")

arr = [-2,1,-3,4,-1,2,1,-5,4]
kadanesAlgorithmFollowUp(arr)