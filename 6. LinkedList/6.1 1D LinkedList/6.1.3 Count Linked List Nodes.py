"""
Q. Given the head of a linked list, print the length of the linked list.

Example 1:

Input Format: 0->1->2

Result: 3

Explanation: The list has a total of 3 nodes, thus the length of the list is 3.


Example 2:

Input Format: 2->5->8->7

Result: 4

Explanation: Again, the list has 4 nodes, hence, the list length is 4.
"""

class Node:
    def __init__(self, data1, next1 = None):
        self.data = data1
        self.next = next1

def ArrToLinkedList(arr):
    head = Node(arr[0])
    mover = head

    for i in range(1, len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp
    return head


def lenghtOfLL(head):
    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    temp = head
    counter = 0
    while(temp):
        counter += 1
        temp = temp.next
    return counter




arr = [1,2,3,4,5,6,7]
head = ArrToLinkedList(arr)
print(lenghtOfLL(head))
