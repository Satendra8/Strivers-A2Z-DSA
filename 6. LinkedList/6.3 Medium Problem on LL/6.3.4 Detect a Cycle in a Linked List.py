"""
Q. Detect a Cycle in a Linked List

Examples
Example 1:

Input Format:

LL: 1 2 3 4 5


Result: True

Explanation: The last node with the value of 5 has its 'next' pointer pointing back to a previous node with the value of 3. This has resulted in a loop, hence we return true.

Example 2:

Input Format:

LL: 1 2 3 4 9 9


Result: False

Explanation: : In this example, the linked list does not have a loop hence returns false.

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


def detectLoop(head):
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
            return True
        s.add(temp)
        temp = temp.next
    print(s)
    return False


def detectLoopHareTortoise(head):
    """
    1. Optimal Approach
    2. user hare and tortoise method
    3. add check if head is null
    4. return true if hare and tortoise is at same position
    5. move hare 2 step and tortoise 1 step
    6. Time Complexity: O(N)
    7. Space Complexity: O(1)
    """

    if head is None:
        return None
    hare = head.next
    tortoise = head

    while(hare and hare.next):
        if hare == tortoise:
            return True
        hare = hare.next.next
        tortoise = tortoise.next
    return False





head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = head.next.next
# printLL(head)
print(detectLoopHareTortoise(head))
