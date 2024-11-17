"""
Q. Given an array of integers and an integer k, return the total number of subarrays whose sum equals k.

Example 1:
Input Format: N = 4, array[] = {3, 1, 2, 4}, k = 6
Result: 2
Explanation: The subarrays that sum up to 6 are [3, 1, 2] and [2, 4].

Example 2:
Input Format: N = 3, array[] = {1,2,3}, k = 3
Result: 2
Explanation: The subarrays that sum up to 3 are [1, 2], and [3].

"""


def subarray_sum(arr, k):
    """
    1. Brute Force Approach
    2. Find all subarrays
    3. Match sum with k and count
    """
    n = len(arr)
    counter = 0
    for i in range(n):
        sum_ = arr[i]
        if sum_ == k:
            counter += 1
        for j in range(i+1, n):
            sum_ += arr[j]
            if sum_ == k:
                counter += 1
    return counter
arr = [3,1,2,4]
k = 6
print(subarray_sum(arr, k))


def subarray_sum(arr, k):
    """
    1. Optimal Approach (if numbers are positive)
    2. Check if sum exceeds then check if sum == k, increment counter, and shrink from left
    3. Else Sum and move to right
    4. Time Complexity O(N)
    5. Space Complexity O(1)
    """
    n = len(arr)
    sum_ = 0
    counter = 0
    i = 0
    j = 0
    
    while i<n:
        if arr[i] + sum_ > k:
            if sum_ == k:
                counter += 1
            sum_ -= arr[j]
            j += 1
        else:
            sum_ += arr[i]
            i += 1
           
    if sum_ == k:
        counter += 1

    return counter
arr = [3,1,2,4]
k = 4
print(subarray_sum(arr,k))



def subarray_sum_strivers(arr, k):
    """
    1. Strivers Approach (only for positive elements)
    2. loop right pointer to n
    3. shrink left pointer untill sum > k and left <= right
    4. if sum == k , increase counter
    5. increate right pointer and add next element is right < n
    6. Time Complexity - O(2N)
    7. Space Complexity - O(N)
    """
    n = len(arr)
    sum_ = arr[0]
    counter = 0
    right = 0
    left = 0
    
    while right < n:
        while(left <=right and sum_ > k):
            sum_ -= arr[left]
            left += 1
        
        if sum_ == k:
            counter += 1
    
        right += 1
        print(right, left)
        if(right < n):
            sum_ += arr[right]

    return counter
arr = [3,1,2,4]
k = 4
print(subarray_sum_strivers(arr,k))



def subarray_sum_with_negative(arr, k):
    """
1. Optimal Approach (including negative)
2. Add array element as prev_sum
3. Apply the logic if someone has to be 7 (prev_sum), someone needs to be 4 (in case of k=3)
4. check if needed elemnt is in dictionary, also check if pre_sum = k
5. insert previous sum in dictionary for future reference
6. Time Complexity - O(N)
7. Space Complecity - O(N)
    """
    n = len(arr)
    
    counter = 0
    prev_sum = 0
    d = {}
    for index, elem in enumerate(arr):
        print(index, elem)
        prev_sum += elem
        if prev_sum - k in d:
            counter += 1
        if prev_sum == k:
            counter += 1
        d[prev_sum] = index
    return counter
        
arr = [1,0,1,0,1]
k = 2
print(subarray_sum_with_negative(arr,k))