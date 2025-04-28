"""
Q. Given a stack, the task is to sort it such that the top of the stack has the greatest element.

Example 1:

Input:
Stack: 3 2 1
Output: 3 2 1
Example 2:

Input:
Stack: 11 2 32 3 41
Output: 41 32 11 3 2
"""

def insert(stack, val):
    if len(stack) == 0 or stack[-1] <= val:
        stack.append(val)
        return
    last = stack.pop()
    insert(stack, val)
    stack.append(last)
    return

def sort(stack):
    if len(stack) == 1:
        return
    last = stack.pop()
    sort(stack)
    insert(stack, last)

stack = [5,2,3,1]
sort(stack)
print(stack)