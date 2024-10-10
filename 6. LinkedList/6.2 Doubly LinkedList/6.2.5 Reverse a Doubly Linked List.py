"""
Q. Given a doubly linked list of size 'N' consisting of positive integers, your task is to reverse it and return the head of the modified doubly linked list.

Example 1:

Input Format:

DLL: 1 <-> 2 <-> 3 <-> 4


Result: DLL: 4 <-> 3 <-> 2 <-> 1


Explanation: The doubly linked list is reversed and its last node is returned at the new head pointer.

Example 2:

Input Format:

DLL: 10 <-> 20 <-> 30


Result: DLL: 30 <-> 20 <-> 10


Explanation: In this case, the doubly linked list is reversed and its former tail is returned as its new head.

"""

import copy
class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

    
def ArrayToDLL(arr):
    head = Node(arr[0])
    earlier = head

    for i in range(1, len(arr)):
        curr = Node(arr[i], earlier)
        earlier.next = curr
        earlier = curr
    return head

def printLL(head):
    mover = head

    while(mover):
        print(mover.data, end=" ")
        mover = mover.next
    print()


def reverseDLL(head):
    """
    1. Brute Force Approach
    2. store in Stack LIFO
    3. swap curr and prev
    4. if curr.prev  is None, then make it head
    5. Time Complexity: O(N)
    6. Space Complexity: O(N)
    """
    # null case
    if head is None:
        return None
    
    # single element
    if head.next is None:
        return head

    temp = head
    stack = []

    # insert in stack
    while(temp.next):
        stack.append(temp)
        temp = temp.next
    stack.append(temp)
    print(stack)

    # get from stack LIFO
    while stack:
        curr = stack.pop()
        curr.prev, curr.next = curr.next, curr.prev
        if curr.prev is None:
            head = curr
    return head


def reverseDLLOptimized(head):
    """
    1. Optimal Approach
    2. swap next and prev
    3. keep swapping till tail
    4. make tail as head
    5. Time Complexity: O(N)
    5. Space Complexity: O(1)
    
    """
    # if head is None
    if head is None:
        return None

    # if single element
    if head.next is None:
        return head
    
    temp = head

    while(temp.next):
        curr = temp
        curr.next, curr.prev = curr.prev, curr.next
        temp = temp.prev

    temp.next, temp.prev = temp.prev, temp.next
    return temp

arr = [1,2,3,4,5,6,7]
head = ArrayToDLL(arr)
head = reverseDLLOptimized(head)
printLL(head)
