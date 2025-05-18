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



def insert(stack, element):
    """
    1. using IBH Method
    2. Hypothesis: remove last element and try to insert the element
    3. Base Condition: if len of stack is 0, that is the begining, insert the element
    4. Induction: insert the last element at the end
    """
    if len(stack) == 0:
        stack.append(element)
        return
    last = stack.pop()
    insert(stack, element)
    stack.append(last)
    return


def reverse(stack):
    """
    1. using IBH Method
    2. Hypothesis: reverse n-1 element, then insert the nth element at beginning
    3. Base Condition: if len of stack is 1, it is already sorted
    4. Induction: insert the nth element at begining
    """
    if len(stack) == 1:
        return
    last = stack.pop()
    reverse(stack)
    insert(stack, last)
    return

st = [3,2,1,7,6]
reverse(st)
print(st)