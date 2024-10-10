"""
Q. Given a linked list, delete the tail of the linked list and print the updated linked list.

Example 1:

Examples:

Input Format: 0->1->2

Result: 0->1


Explanation: The tail of the list is the last node. After removing the tail, and updating the linked list, this result is what we get.

Example 2:

Input Format: 12->5->8->7

Result: 12->5->8

Explanation: Again, after deleting the tail and updating the linked list, the list ends at the second last node, which is the new tail.

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

def deleteLastNode(head):

    if head is None:
        return None
    
    if head.next is None:
        return None
    
    curr = head
    prev = head
    while(curr.next):
        prev = curr
        curr = curr.next
    prev.next = None
    return head


arr = [2,5,7,8]
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])
head.next.next.next = Node(arr[3])
printLL(head)
head = deleteLastNode(head)
printLL(head)


def leetCodeDeleteNode(node):
    """
    1. here we don't have access to head
    2. also we don't have access to previous node
    3. so there is a one single option copy next node to current node
    4. curr.value = next.value
    5. curr.next = next.next
    6. Time Complexity: O(1)
    7. Space Complexity: O(1)
    """

    node.data = node.next.data
    node.next = node.next.next