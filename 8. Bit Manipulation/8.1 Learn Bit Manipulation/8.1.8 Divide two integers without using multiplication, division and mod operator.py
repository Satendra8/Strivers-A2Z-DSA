"""
Q. Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 
Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
"""


def divide(dividend, divisor):
    """
    1. Brute Force Approach
    2. keep adding divisor to reachs dividend
    3. Time Complexity: O(dividend)
    4. Space Complexity: O(1)
    """

    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    if dividend == divisor:
        return 1

    sign = True
    if dividend < 0 and divisor < 0:
        dividend = -dividend
        divisor = -divisor
    elif dividend < 0:
        dividend = -dividend
        sign = False
    elif divisor < 0:
        divisor = -divisor
        sign = False

    counter = 0
    summ = 0

    while(summ <= dividend):
        summ += divisor
        counter += 1

    counter = counter - 1

    if not sign:
        counter = -counter
    
    if counter < INT_MIN:
        return INT_MIN
    
    if counter > INT_MAX:
        return INT_MAX

    return counter


def divideOptimal(dividend, divisor):
    """
    Eg: dividend = 22, divisor = 3
        3 + 3 + 3 + 3 + 3 + 3 + 3
        3 * 7
        3 * (2^2 + 2^1 + 2^0)
        (3*2^2) + (3*2^1) + (3*2^0)
    1. find the max element <= 3*2^x
    2. now subtract it from dividend
    3. ans will be ans + 2^x
    4. Time Complexity: logN * logN
    5. Space Complexity: O(1)
    """
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    if dividend == divisor:
        return 1

    sign = True
    if dividend < 0 and divisor < 0:
        dividend = -dividend
        divisor = -divisor
    elif dividend < 0:
        dividend = -dividend
        sign = False
    elif divisor < 0:
        divisor = -divisor
        sign = False

    count = 0
    while dividend >= divisor:
        i = 0
        while((divisor << (i+1)) <= dividend):
            i += 1

        dividend -= (divisor << i)
        count += (1<<i)
    
    if not sign:
        count = -count
    
    if count < INT_MIN:
        return INT_MIN
    
    if count > INT_MAX:
        return INT_MAX

    return count


dividend = 7
divisor = -3
print(divideOptimal(dividend, divisor))

"""
Do reverse engineering
dividend = 22, divisor = 3

can i remove
3*2^0 = 3
3*2^1 = 6 (3<<1) = (011<<1 = 110)
3*2^2 = 12 (3 * 1<<2) = (3<<2) = (011<<2 = 1100)
3*2^3 = 24 (no so subtract 12)
ans = 2^2 = 4

now dividend = 10

can i remove
3*2^0 = 3
3*2^1 = 6
3*2^2 = 12 (no so subtract 6)
ans = 4 + 2^1 = 6

now dividend = 4

can i remove
3*2^0 = 3
3*2^1 = 6 (no so subtract 3)
ans = 6 + 2^0 = 7

now dividend = 1

can i remove
3*2^0 = 3 (no so return)

base case = if divisor*2^i > dividend return
"""