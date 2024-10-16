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

dividend = 10
divisor = 3
print(divide(dividend, divisor))