"""
Q. Given an array and a sum k, we need to print the length of the longest subarray that sums to k.

Example 1:
Input Format: N = 3, k = 5, array[] = {2,3,5}
Result: 2
Explanation: The longest subarray with sum 5 is {2, 3}. And its length is 2.

Example 2:
Input Format: N = 5, k = 10, array[] = {2,3,5,1,9}
Result: 3
Explanation: The longest subarray with sum 10 is {2, 3, 5}. And its length is 3.

"""


def longestSubarrayWithGivenSum(arr, k):
    """
    Brute Force Approach
    1. Generate all possible subarray
    2. add them and match with k
    
    Time Complexity: O(n^3)
    Space Complexity: O(1)
    
    """
    n = len(arr)
    length = 0
    
    for i in range(n):
        for j in range(i, n):
            
            if sum(arr[i:j+1]) == k:
                print(arr[i:j+1])
                length = max(length, j-i+1)
    return length


def longestSubarrayWithGivenSum(arr, k):
    """
    Brute Force Approach
    1. Generate all possible subarray
    2. add them and match with k
    3. here i am adding the same j loop for summ
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    
    """
    n = len(arr)
    length = 0
    
    for i in range(n):
        summ = 0
        for j in range(i, n):
            summ += arr[j]
            if summ == k:
                print(arr[i:j+1])
                length = max(length, j-i+1)
    return length



def findLongestSubarrayOptimized(arr, k):
    """
    Optimal Approach
    1. loop over all numbers
    2. add them and check if == k or the remaining number exist in d.
    3. update length accordingly
    4. update summ if not in d along with index
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    """
    
    n = len(arr)
    d = {}
    summ = 0
    length = 0
    
    for i,j in enumerate(arr):
        summ += j
        remaining = summ-k
        
        if summ == k:
            length = max(length, i+1)
        elif remaining in d:
            length = max(length, i - d[remaining])

        if summ not in d: 
            d[summ] = i
    return length

arr = [1,1,1]
k = 4
print(findLongestSubarrayOptimized(arr, k))  