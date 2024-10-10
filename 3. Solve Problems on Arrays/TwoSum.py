"""
Q. Given an array of integers arr[] and an integer target.

1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.

2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.

Note: You are not allowed to use the same element twice. Example: If the target is equal to 6 and num[1] = 3, then nums[1] + nums[1] = target is not a solution.

Example 1:
Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 14
Result: YES (for 1st variant)
       [1, 3] (for 2nd variant)
Explanation: arr[1] + arr[3] = 14. So, the answer is “YES” for the first variant and [1, 3] for 2nd variant.

Example 2:
Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 15
Result: NO (for 1st variant)
	[-1, -1] (for 2nd variant)
Explanation: There exist no such two numbers whose sum is equal to the target.

"""


def TwoSum(arr, target):
    """
    Brute Force Approach
    1. get all pairs using nested for loop
    2. check if sum of pair == k
    3. return -1,-1 if not pair exist

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return arr[i], arr[j]
    
    return -1, -1



def TwoSumBetter(arr, target):
    """
    Better Approach
    1. store previous element in a set
    2. if target - number found in set return both
    3. add the current element in set

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(arr)
    prevSet = set()
   
    for num in arr:
        
        rem = target - num
        if rem in prevSet:
           return num, rem

        prevSet.add(num)
    
    print(prevSet)
    return -1,-1



def TwoSumOptimized(arr, target):
    """
    Optimized Approach
    1. sort the array
    2. take 2 pointer left and right
    3. if sum = k return the numbers
    4. if sum < k move left pointer, if sum > k move right pointer
    Time Complexity: O(nlogn)
    Space Complexity: O(1)
    """
    
    n = len(arr)
    arr.sort()
    left = 0
    right = n-1
    
    while left < right:
        summ = arr[left] + arr[right]
    
        if summ == target:
            return left, right
        elif summ < target:
            left += 1
        else:
            right -= 1
    
    return -1,-1


arr = [3,2,4]
target = 6
print(TwoSumBetter(arr, target))