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


def findLongestSubarray(arr, k):
    """
    Optimized Solution
    1. Use 2 pointers i and j
    2. check if summ is overflow
    3. check summ with k and update length
    4. shrink the left pointer, and decrease summ
    5. if not overflow keep adding in summ and increment i

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    
    n = len(arr)
    i=j=summ=length=0
    while i<n:
        if summ + arr[i] > k:
            if summ == k:
                length = max(length, i-j)

            summ = summ - arr[j]
            j += 1
        else:
            summ += arr[i]
            i += 1

    if summ == k:
        length = max(length, i-j)
    return length

arr = [1,3,1,2]
k = 6
print(findLongestSubarray(arr, 5))










#Revisit
def subarray(arr, k):
    n = len(arr)
    i = 0
    j = 0
    max_lenght = 0
    sum_ = 0
    
    while(i<=j):
        
        
        if sum_ < k:
            sum_ += arr[j]
            j += 1
        
        elif sum_ > k:
            sum_ -= arr[i]
            i += 1
        else:
            max_lenght = max(max_lenght, j-i)
            j += 1

    return max_lenght  
