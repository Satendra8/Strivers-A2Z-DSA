"""
Q. Given the head of a linked list, determine the length of a loop present in the linked list; if not present, return 0.

Example 1:

Input Format:

LL: 1  2  3  4  5 

Output: 3
Explanation: A cycle exists in the linked list starting at node 3 -> 4 -> 5 and then back to 3. There are 3 nodes present in this cycle.

Example 2:

Input Format:

LL: 1  2  3  4  9  9

Output: 0

Explanation: In this example, the linked list is linear and does not have a loop hence return 0.
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

def lengthOfLoop(head):
    """
    1. Brute Force Approach
    2. maintain a set
    3. if element is found in set initialize counter
    4. if element is again found stop counter
    5. Time Complexity: O(N)
    6. Space Complexity: O(N)
    """
    temp = head
    s = set()

    while(temp):
        if temp in s:
            #loop detected
            s = set()
            counter = 0
            # count element of loops
            while(temp):
                if temp in s:
                    return counter
                s.add(temp)
                counter += 1
                temp = temp.next
        s.add(temp)
        temp = temp.next
    return 0


def lenghtOfLoopOptimized(head):
    """
    1. Optimal Approach
    2. use hare and tortoise method
    3. move hare 2 step and tortoise 1 step
    4. if hare == tortoise loop found initialize counter
    5. count the element till hare != tortoise
    6. once hare and tortoise are at same position return count
    7. Time Complexity: O(N)
    8. Space Complexity: O(1)
    """
    hare = head
    tortoise = head

    while(hare and hare.next):
        hare = hare.next.next
        tortoise = tortoise.next
        # loop found initialize counter
        if hare == tortoise:
            count = 1
            hare = hare.next.next
            tortoise = tortoise.next
            # count the loop again
            while(hare != tortoise):
                count += 1
                hare = hare.next.next
                tortoise = tortoise.next
            return count
    return 0


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
# head.next.next.next.next.next = head.next.next
# printLL(head)
print(lenghtOfLoopOptimized(head))
