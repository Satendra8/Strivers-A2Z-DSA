"""
Q. Given the head of a linked list that may contain a cycle, return the starting point of that cycle. If there is no cycle in the linked list return null.

Example 1:
Input: LL: 1  2  3  4  5 

Output: 3
Explanation: This linked list contains a loop of size 3 starting at node with value 3.
Example 2:
Input: LL: LL: 1 -> 2 -> 3 -> 4 -> 9 -> 9
                

Output: NULL
Explanation:  This linked list does not contain  a loop hence has no starting point.
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


def findStartingPosition(head):
    """
    1. Brute Force Approach
    2. use set and push all node in set
    3. if a node alrady exist, return true
    4. if no duplicate node return false
    5. Time Complexity: O(N)
    6. Space Complexity: O(N)
    """

    s = set()
    temp = head

    while(temp):
        if temp in s:
            return temp.data
        s.add(temp)
        temp = temp.next
    return None


def findStartingPositionpHareTortoise(head):
    """
    1. detect cycle using hare and tortoise
    2. if hare and tortoise collides
    3. move tortoise to head and then move hare and tortoise 1 step
    4. return the node the collides
    5. Time Complexity: O(N)
    5. Space Complexity: O(1)
    """

    if head is None:
        return head

    hare = head
    tortoise = head

    while(hare and hare.next):
        #detect the loop
        hare = hare.next.next
        tortoise = tortoise.next
        if hare == tortoise:
            tortoise = head
            #reset tortoise and move hare and tortoise to 1 step
            while(hare != tortoise):
                hare = hare.next
                tortoise = tortoise.next
            return hare.data
    return None


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = head.next.next
# printLL(head)
print(findStartingPositionpHareTortoise(head))
