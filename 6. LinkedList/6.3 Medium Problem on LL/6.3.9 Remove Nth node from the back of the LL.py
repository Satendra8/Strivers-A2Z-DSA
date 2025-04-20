"""
Q. Given a linked list and an integer N, the task is to delete the Nth node from the end of the linked list and print the updated linked list.

Example 1:

Input Format: 5->1->2, N=2

Result: 5->2


Explanation: The 2nd node from the end of the linked list is 1. Therefore, we get this result after removing 1 from the linked list.

Example 2:

Input Format: 1->2->3->4->5, N=3

Result: 1->2->4->5

Explanation: The 3rd node from the end is 3, therefore, we remove 3 from the linked list.

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


def removeNth(head, n):
    """
    1. Brute Force Approach
    2. count lenght for LL
    3. get node to be deleted by lenght - n
    4. lenght - n = 0 then need to delete the head, return head.next
    5. find the node to be delete and mark temp.next = temp.next.next
    6. Time Complexity: O(N) + O(N-n)
    7. Space Complexity: O(1)
    """
    total = countLL(head)

    count = total - n
    i = 0
    temp = head

    if(head.next is None and n == 1):
        return None

    if(count == 0):
        return head.next

    while(temp):
        i += 1
        if(i == count):
            break
        temp = temp.next
    temp.next = temp.next.next
    return head
    

def removeNthHareAndTortoise(head, n):
    """
    1. Optimal Approach
    2. use two pointers slow and fast
    3. start slow pointer from head
    4. start fast pointer from nth node
    5. move fast and slow pointer 1 step
    6. mark slow.next = slow.next.next
    7. Time Complexity: O(N)
    8. Space Complexity: O(1)
    """
    temp = head

    slow = temp
    i = 0
    while(temp):
        i += 1
        if(i == n):
            break
        temp = temp.next        
    fast = temp.next

    if fast is None:
        return head.next

    while(fast.next):
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head

arr = [1,2,3,4,5]
head = ArrayToDLL(arr)
head = removeNthHareAndTortoise(head, 1)
printLL(head)


def deleteNthNode(head, n):
    slow = head
    fast = head
    prev = None

    for i in range(n):
        fast = fast.next

    while fast:
        prev = slow
        slow = slow.next
        fast = slow
        for i in range(n):
            fast = fast.next
    if not prev:
        return head.next
    prev.next = slow.next
    return head