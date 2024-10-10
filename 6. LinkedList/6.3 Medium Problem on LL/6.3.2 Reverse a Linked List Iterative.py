"""
Q. Given the head of a singly linked list, write a program to reverse the linked list, and return the head pointer to the reversed list.

Example 1:
Input Format:

LL: 1   3   2   4 

Output: 3


Explanation: After reversing the linked list, the new head will point to the tail of the old linked list.
Example 2:
Input Format:

LL: 4


Output: 4


Explanation: In this example, the linked list contains only one node hence reversing this linked list will result in the same list as the original.
"""

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

 
def reverseLL(head):
    """
    1. use a stack to push elements
    2. pop the element and point its next to previous node
    3. make the last node point to null otherwise cycle will be created
    4. Time Complexity: O(N)
    5. Space Complexity: O(N)
    """
    if head is None:
        return None
    
    if head.next is None:
        return head

    temp = head

    stack = []
    while(temp):
        stack.append(temp)
        temp = temp.next

    old = stack.pop()
    new_head = old

    while(stack):
        curr = stack.pop()
        old.next = curr
        old = curr
    # make the last node point to null otherwise cycle will be created
    old.next = None
    return new_head


def reverseLLOptimized(head):
    """
    1. flip the pointers to point its prev element
    2. save next_node and curr in a variable
    3. update the prev and next node
    4. if it is the last node assign it's prev pointer to next and make it head
    4. Time Complexity: O(N)
    5. Space Complexity: O(1)
    """
    if head is None:
        return None
    
    if head.next is None:
        return head
    
    temp = head
    prev = None

    while(temp):
        curr = temp
        next_node = curr.next
        if next_node is None:
            curr.next  = prev
            return curr
        curr.next = prev
        prev = curr
        temp = next_node

    return temp


arr = [1,2,3,4,5,6]
head = ArrayToDLL(arr)
head = reverseLLOptimized(head)
printLL(head)
