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

def insert(stack, num):
    if len(stack) == 0:
        stack.append(num)
        return
    last = stack.pop()
    insert(stack, num)
    stack.append(last)
    return


def reverse(stack):
    if len(stack) == 1:
        return
    last = stack.pop()
    reverse(stack)
    insert(stack, last)
    return


stack = [1,2,3,4,5]
reverse(stack)
print(stack)