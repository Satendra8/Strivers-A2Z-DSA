"""
Q. Swap given two numbers and print them. (Try to do it without a temporary variable.) and return it.

Example 1:

Input: a = 13, b = 9
Output: 9 13
Explanation: after swapping it
becomes 9 and 13.
Example 2:


Input: a = 15, b = 8
Output: 8 15
Explanation: after swapping it
becomes 8 and 15.

"""

def get(a, b):
    """
    Explaination:

    a = a ^ b
    b = a ^ b = (a ^ b) ^ b = a
    a = a ^ b = (a ^ b) ^ a = b
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


a = 13
b = 9
print(get(a, b))

