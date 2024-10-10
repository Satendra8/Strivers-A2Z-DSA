"""
Q. You are given a positive integer n. Your task is to find and return its square root. If 'n' is not a perfect square, then return the floor value of 'sqrt(n)'.

Note: The question explicitly states that if the given number, n, is not a perfect square, our objective is to find the maximum number, x, such that x squared is less than or equal to n (x*x <= n). In other words, we need to determine the floor value of the square root of n.

Example 1:
Input Format:
 n = 36
Result:
 6
Explanation:
 6 is the square root of 36.

Example 2:
Input Format:
 n = 28
Result:
 5
Explanation:
 Square root of 28 is approximately 5.292. So, the floor value will be 5.
"""


def sqrt(num):
    """
    1. Brute Force Approach
    2. loop over 1 to n//2
    3. check if i*i <= num
    4. Time Complexity; O(N)
    5. Space Complexity: O(1)
    """
    ans = 1
    for i in range(1, num//2):
        if i*i <= num:
            ans = i
    return ans



num = 28
print(sqrt(num))


def sqrt(n):
    """
    1. Optimal Approach
    2. if mid * mid == n, then this is the answer
    3. trim right half if mid * mid > n
    4. else trim left half
    5. Time Complexity: O(logN)
    6. Space Complexity: O(1)
    """
    ans = 1
    left = 1
    right = n

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == n:
            return mid
        elif mid * mid > n:
            right = mid - 1
        else:
            ans = mid
            left = mid + 1
    return ans

n = 5
print(sqrt(n))

"""
[1,2,3,4,5,6,7,8,9,10,11,12,13,14] left=1, right=28, mid=14
                                   left=1, right=13, mid=7
                                   left=1, right=6, mid=3
                                   left=4, right=6, mid=5
                                   left=6, right=6, mid=6
                                   left=7, right=6, mid=6



"""
