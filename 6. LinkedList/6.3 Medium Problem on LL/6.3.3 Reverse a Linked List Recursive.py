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
    def __init__(self, data1, next1 = None):
        self.data = data1
        self.next = next1

def ArrayToLL(arr):
    head = Node(arr[0])
    mover = head

    for i in range(1, len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp
    return head

def printLL(head):
    temp = head
    while(temp):
        print(temp.data, end=" ")
        temp = temp.next
    print()


def reverseLLRecursive(head):
    """
    1. Base case: curr or next node is null
    2. solve for 1 node (just return)
    3. solve for 2 nodes: return new_head and front node point to head and head.next = None
    """
    if not head or not head.next:
        return head
    
    front = head.next
    new_head = reverseLLRecursive(front)
    front.next = head
    head.next = None
    return new_head


arr = [1,2,3,4,5,6,7,8]
head = ArrayToLL(arr)
head = reverseLLRecursive(head)
printLL(head)