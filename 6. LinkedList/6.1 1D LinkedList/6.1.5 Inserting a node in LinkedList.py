"""
Q. Given a linked list and an integer value val, insert a new node with that value at the beginning (before the head) of the list and return the updated linked list.

Example 1:

Input Format: 0->1->2, val = 5

Result: 5->0->1->2


Explanation: We need to insert the value 5 before the head of the given Linked List.

Example 2:

Input Format:12->5->8->7, val = 100

Result: 100->12->5->8->7

Explanation: Again, we need to insert the value 100 before the head of the Linked List.

"""

class Node:
    def __init__(self, data1, next1 = None):
        self.data = data1
        self.next = next1

def printLL(head):
    mover = head

    while(mover):
        print(mover.data, end=" ")
        mover = mover.next
    print()

def insertNode(self,head,x):
    mover = head

    new = Node(x)
    if (head is None):
        return new
    while(mover.next):
        mover = mover.next
    mover.next = new
    return head

    
head = Node(5)
insertNode(head, 2)
insertNode(head, 3)
insertNode(head, 7)
insertNode(head, 1)
insertNode(head, 2)
printLL(head)