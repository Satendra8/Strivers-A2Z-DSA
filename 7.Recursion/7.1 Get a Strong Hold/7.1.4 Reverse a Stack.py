"""
Q. You are given a stack St. You have to reverse the stack using recursion.

Example 1:

Input:
St = {3,2,1,7,6}
Output:
{6,7,1,2,3}
Explanation:
Input stack after reversing will look like the stack in the output.
Example 2:

Input:
St = {4,3,9,6}
Output:
{6,9,3,4}
Explanation:
Input stack after reversing will look like the stack in the output.

"""


def reverse(stack):
    """
    1. base case: if stack len is 1, it is already reversed
    2. pick first element
    3. reverse rest elements
    4. append first element at last
    """

    if len(stack) == 1:
        return stack

    first = stack.pop(0)
    stack = reverse(stack)
    stack.append(first)
    return stack

stack = [3,2,1,7,6]
reverse(stack)
print(stack)
