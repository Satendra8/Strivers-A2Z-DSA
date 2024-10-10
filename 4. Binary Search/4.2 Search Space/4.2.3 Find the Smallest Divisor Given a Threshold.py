"""
Q. You are given an array of integers 'arr' and an integer i.e. a threshold value 'limit'. Your task is to find the smallest positive integer divisor, such that upon dividing all the elements of the given array by it, the sum of the division's result is less than or equal to the given threshold value.

Example 1:
Input Format:
 N = 5, arr[] = {1,2,3,4,5}, limit = 8
Result:
 3
Explanation:
 We can get a sum of 15(1 + 2 + 3 + 4 + 5) if we choose 1 as a divisor. 
The sum is 9(1 + 1 + 2 + 2 + 3)  if we choose 2 as a divisor. Upon dividing all the elements of the array by 3, we get 1,1,1,2,2 respectively. Now, their sum is equal to 7 <= 8 i.e. the threshold value. So, 3 is the minimum possible answer.

Example 2:
Input Format:
 N = 4, arr[] = {8,4,2,3}, limit = 10
Result:
 2
Explanation:
 If we choose 1, we get 17 as the sum. If we choose 2, we get 9(4+2+1+2) <= 10 as the answer. So, 2 is the answer.



Point to remember:

While dividing the array elements with a chosen number, we will always take the ceiling value. And then we will consider their summation. For example, 3 / 2 = 2.
Observation: 

Minimum possible divisor: We can easily consider 1 as the minimum divisor as it is the smallest positive integer.
Maximum possible divisor: If we observe, we can conclude the maximum element in the array i.e. max(arr[]) is the maximum possible divisor. Any number > max(arr[]), will give the exact same result as max(arr[]) does. This divisor will generate the minimum possible result i.e. n(1 for each element), where n = size of the array.
With these observations, we can surely say that our answer will lie in the range 
[1, max(arr[])].
"""


def ceil_alternative(x):
    return int(x) if x == int(x) else int(x) + 1

def smallestDivisor(nums, threshold):
    """
    1. Brute Force Approach
    2. iterate over 1 to max(arr)
    3. divide and add all numbers and check if it is less than equal to target
    4. Time Complexity: O(max(arr) * N)
    5. Space Complexity: O(1)
    """
    left = 1
    right = max(nums)

    for i in range(left, right+1):
        summ = 0
        for j in nums:
            summ += ceil_alternative(j/i)
        if summ <= threshold:
            return i
    return -1

nums = [44,22,33,11,1]
threshold = 5
print(smallestDivisor(nums, threshold))

"""
nums = [1,2,5,9]
threshold = 6
possible numbers = [1,2,3,4,5,6,7,8,9]

1 = 1+2+5+9 = 17
2 = 1+1+3+5 = 10
3 = 1+2+2+3 = 8
4 = 1+1+2+3 = 7
5 = 1+1+1+2 = 5
"""





def ceil_alternative(x):
    return int(x) if x == int(x) else int(x) + 1

def smallestDivisor(nums, threshold):
    """
    1. Optimal Approach
    2. Use binary search for range [1 to max(N)]
    3. trim left if summ > threshold
    4. trim right if if summ <= threshold and keep storing mid
    5. Time Complexity: O(NlogN)
    6. Space Complexity: O(1)
    """
    left = 1
    right = max(nums)
    ans = -1

    while left <= right:
        mid = (left+right) // 2
        summ = 0
        for j in nums:
            summ += ceil_alternative(j/mid)
        if summ > threshold:
            left = mid + 1
        else:
            ans = mid
            right = mid - 1
    return ans


nums = [1,2,5,9]
threshold = 6
print(smallestDivisor(nums, threshold))

"""
nums = [1,2,5,9]
threshold = 6
possible numbers = [1,2,3,4,5,6,7,8,9]    left=1, right=9, mid=5
                                          left=1, right=4, mid=2
                                          left=3, right=4, mid=3
                                          left=4, right=4, mid=4
                                          left=5, right=4, mid=4

1 = 1+2+5+9 = 17
2 = 1+1+3+5 = 10
3 = 1+2+2+3 = 8
4 = 1+1+2+3 = 7
5 = 1+1+1+2 = 5

ans = 5
"""