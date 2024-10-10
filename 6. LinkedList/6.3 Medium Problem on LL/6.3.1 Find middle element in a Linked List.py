"""
Q. Given the head of a linked list of integers, determine the middle node of the linked list. However, if the linked list has an even number of nodes, return the second middle node.

Example 1:
Input: LL: 1  2  3  4  5 

Output: 3
Explanation: Node with value 3 is the middle node of this linked list.
Example 2:
Input: LL: 1  2  3  4  5  6
                

Output: 4
Explanation:  In this example, the linked list has an even number of nodes hence we return the second middle node which is 4.
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


def findMiddle(head):
    """
    1. find the length of LL
    2. return the element at count // 2 + 1
    3. Time Complexity: O(N)
    4. Space Complexity: O(1)
    """
    if head is None:
        return None

    count = 0
    temp = head
    while (temp):
        count += 1
        temp = temp.next

    index = (count // 2) + 1

    curr = head
    curr_count = 0
    while(curr):
        curr_count += 1
        if curr_count == index:
            return curr.data
        curr = curr.next


def findMiddleHareTortoise(head):
    """
    1. use hare and tortoise
    2. move tortoise 1 step and hare 2 step
    3. Time Complexity: O(N/2)
    4. Space Complexity: O(1)
    """
    tortoise = head
    hare = head

    while(hare and hare.next):
        hare = hare.next.next
        tortoise = tortoise.next
    return tortoise.data


arr = [1,2,3,4,5,6]
head = ArrayToDLL(arr)
print(findMiddleHareTortoise(head))
# printLL(head)
