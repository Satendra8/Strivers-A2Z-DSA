"""
Q. Given the head of a linked list of integers, delete the middle node of the linked list and return the modified head. However, if the linked list has an even number of nodes, delete the second middle node.

Example 1:

Input Format:

LL: 1  2  3  4  5 

Output: 1 2 4 5

Explanation: Node with value 3 is at the middle node and deleted.



Example 2:

Input Format:

LL: 1  2  3  4

Output: 1 2 4

Explanation: In this example, the linked list has an even number of nodes hence we return the second middle node which is 3.

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

def deleteMiddleNode(head):
    """
    1. count length of LL
    2. find mid
    3. goto the mid node and make temp.next = temp.next.next
    4. Time Complexity: O(N)
    5. Space Complexity: O(1)
    """
    count = countLL(head)
    mid = count // 2

    if head.next is None:
        return None
    temp = head
    i = 0
    while(temp):
        i += 1
        if(i == mid):
            break
        temp = temp.next
    temp.next = temp.next.next
    return head



def deleteMiddleNodeOptimal(head):
    """
    1. use hare and tortoise method
    2. move hare 2 step and tortoise 1 step
    3. now tortoise is at the mid point
    4. tortoise.next = tortoise.next.next
    5. Time Complexity: O(N)
    6. Space Complexity: O(1)
    """
    temp = head

    if head is None:
        return None
    hare = temp.next
    tortoise = temp

    if hare is None:
        return None

    while(hare.next and hare.next.next):
        hare = hare.next.next
        tortoise = tortoise.next
    tortoise.next = tortoise.next.next
    return temp

arr = [1,3,4,7,1,2]
head = ArrayToDLL(arr)
head = deleteMiddleNodeOptimal(head)
printLL(head)



def deleteMiddleNode(head):
    if not head:
        return head
    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow 
        slow = slow.next
        fast = fast.next.next
    prev.next = slow.next
    return head