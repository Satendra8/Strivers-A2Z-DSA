"""
Q. You are given the head_ref of a doubly Linked List and a Key. Your task is to delete all occurrences of the given key if it is present and return the new DLL.

Example1:

Input: 
2<->2<->10<->8<->4<->2<->5<->2
2
Output: 
10<->8<->4<->5
Explanation: 
All Occurences of 2 have been deleted.

Example2:

Input: 
9<->1<->3<->4<->5<->1<->8<->4
9
Output: 
1<->3<->4<->5<->1<->8<->4
Explanation: 
All Occurences of 9 have been deleted.
"""

class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


def printLL(head):
    mover = head
    while(mover):
        print(mover.data, end=" ")
        mover = mover.next
    print()


def ArrayToDLL(arr):
    if not arr:
        return None
    head = Node(arr[0])
    earlier = head

    for i in range(1, len(arr)):
        curr = Node(arr[i], earlier)
        earlier.next = curr
        earlier = curr
    return head


def countLL(head):
    temp = head
    counter = 0

    while(temp):
        counter += 1
        temp = temp.next
    return counter


def deleteAllOccuranceOfX(head, x):
    """
    1. Optimal Approach
    2. handle head: mark prev of next element to null and mark next element as head
    3. handle tail: mark next of prev element to null
    4. handle mid element: make the prev node points to next and next to prev
    5. Time Complexity: O(N)
    6. Space Complexity: O(1)
    """
    temp = head
    if head is None:
        return None

    while(temp):
        next_pointer = temp.next
        if temp.data == x:
            #handle head
            if temp.prev is None:
                if head.next is None:
                    return None
                temp.next.prev = None
                head = temp.next
            #handle tail
            elif temp.next is None:
                temp.prev.next = None
            else:
                temp.next.prev,  temp.prev.next = temp.prev, temp.next
        temp = next_pointer
    return head

arr = [1,6,6,6,6,3]
x = 6
head = ArrayToDLL(arr)
head = deleteAllOccuranceOfX(head, x)
printLL(head)

"""
Dry Run 1:

arr = [5,6,4,9,6]
x = 6

5 -> [5]
6 -> [5,4]
4 -> [5,4,]
9 -> [5,4,9]
6 -> [5,4,9]

"""


def deleteNode(node):
    if node.next:
        node.next.prev = node.prev
    if node.prev:
        node.prev.next = node.next


def deleteAllOccurance(head, x):
    if not head:
        return None

    new_head = Node(-1)
    new_head.next = head
    head.prev = new_head

    temp = new_head

    while temp:
        if temp.data == x:
            deleteNode(temp)
        temp = temp.next
    return new_head.next