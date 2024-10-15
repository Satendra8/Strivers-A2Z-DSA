"""
Q. Given a positive integer n, determine whether it is odd or even. Return a string "even" if the number is even and "odd" if the number is odd.

Examples:

Input: n = 15
Output: odd
Explanation: The number is not divisible by 2


Input: n = 44
Output: even
Explanation: The number is divisible by 2
"""

def oddEven(n):
    """
    1. check if last bit is set
    2. 5 => 101
    3. &    001
       ----------
            001
    4. 0 then even
    5. 1 then odd
    6. Time Complexity: O(1)
    7. Space Complexity: O(1)
    """
    if n & 1:
        return "odd"
    return "even"


n = 11
print(oddEven(n))