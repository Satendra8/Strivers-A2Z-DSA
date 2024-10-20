def divide(dividend, divisor):
    """
    1. Brute Force Approach
    2. keep adding divisor to reachs dividend
    3. Time Complexity: O(dividend)
    4. Space Complexity: O(1)
    """

    counter = 0
    summ = 0

    while(summ <= dividend):
        summ += divisor
        counter += 1

    return counter - 1


def divideOptimal(dividend, divisor):
    """
    Eg: dividend = 22, divisor = 3
        3 + 3 + 3 + 3 + 3 + 3 + 3
        3 * 7
        3 * (2^2 + 2^1 + 2^0)
        (3*2^2) + (3*2^1) + (3*2^0)
        formula = divisor*
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

now dividend = 10

can i remove
3*2^0 = 3
3*2^1 = 6
3*2^2 = 12 (no so subtract 6)

now dividend = 4

can i remove
3*2^0 = 3
3*2^1 = 6 (no so subtract 3)

now dividend = 1

can i remove
3*2^0 = 3 (no so return)

base case = if divisor*2^i > dividend return
"""