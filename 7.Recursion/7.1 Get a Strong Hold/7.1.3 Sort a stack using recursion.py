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

def insert(stack, element):
    """
    1. base case: if stack is empty or last element is lesser
    2. append the element at last and return
    3. otherwise take last element, insert current element to its correct position
    4. now append last element
    """
    if not stack or stack[-1] < element:
        stack.append(element)
        return stack

    last = stack.pop()
    stack = insert(stack, element)
    stack.append(last)
    return stack

def Sort(stack):
    """
    1. base case: if stack lenght is 1, already sorted
    2. reduce array picking last element and sort rest
    3. now move last element to it's correct position like insertion sort
    4. return stack
    """
    if len(stack) == 1:
        return stack
    element = stack.pop()
    stack = Sort(stack)
    stack = insert(stack, element)
    return stack


stack = [11,2]
Sort(stack)
print(stack)



def merge(stack, element):
    """
    1. using IBH method
    2. Hypothesis: remove last element, then call merge
    3. Base Condition: if arr is empty or last element is greater, then merge element at last
    4. Induction: append the nth element at last
    """
    if len(stack) == 0 or stack[-1] > element:
        stack.append(element)
        return
    last = stack.pop()
    merge(stack, element)
    stack.append(last)
    return


def sort(stack):
    """
    1. Using IBH method
    2. Hypothesis: sort n - 1 elements
    3. Base Condition: if single element in array, then arr is already sorted
    4. Induction: get n-1 sorted and place the nth element at right position
    """
    if len(stack) == 1:
        return
    last = stack.pop()
    sort(stack)
    merge(stack, last)


stack = [3,2,1]
sort(stack)
print(stack)