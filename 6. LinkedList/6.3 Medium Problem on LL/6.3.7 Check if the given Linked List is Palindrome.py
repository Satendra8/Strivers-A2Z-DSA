"""
Q. Check if the given Linked List is Palindrome


Example 1:

Input Format:

LL: 1  2  3  2  1


Output: True

Explanation: A linked list with values "1 2 3 2 1" is a palindrome because its elements read the same from left to right and from right to left, making it symmetrical and mirroring itself.

Example 2:

Input Format:

LL: 1 2 3 3 2 1 


Output: True

Explanation: A linked list with values "1 2 3 3 2 1" is a palindrome because it reads the same forwards and backwards.

Example 3:

Input Format:

LL: 1 2 3 2 3


Output: False

Explanation: The linked list "1 2 3 2 3" is not a palindrome because it reads differently in reverse order, where "3 2 3 2 1" is not the same as the original sequence "1 2 3 2 3."
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

def reverseLL(head):
    temp = head
    if temp is None:
        return None
    
    if temp.next is None:
        return temp
    
    prev_pointer = None

    while(temp):
        curr = temp
        if curr.next is None:
            curr.next = prev_pointer
            return curr
        next_pointer = curr.next
        curr.next = prev_pointer
        prev_pointer = temp
        temp = next_pointer
    return head


def checkPalindrom(head):
    """
    1. reverse the linked list
    2. then match elements
    3. Time Complexity: O(N)
    4. Space Complexity: O(N)
    """
    temp = head
    reverse = reverseLL(temp)

    while(temp and reverse):
        if temp.data != reverse.data:
            return False
        temp = temp.next
        reverse = reverse.next
    return True


def checkPalindromOptimized(head):
    """
    1. find the middle (do for odd and even both)
    2. reverse the middle half
    3. compare first half and second half
    4. don't forget to reverse second half to make it origional
    5. Time Complexity: O(N)
    5. Space Complexity: O(1) // pointer takes less space
    """
    temp = head
    hare = temp
    tortoise = temp

    while(hare.next and hare.next.next):
        hare = hare.next.next
        tortoise = tortoise.next

    newHead = reverseLL(tortoise.next)
    printLL(newHead)

    first = temp
    second = newHead

    while(second):
        if first.data != second.data:
            reverseLL(newHead)
            return False
        first = first.next
        second = second.next

    reverseLL(newHead)
    return True
    

arr = [1,2,3,2,1]
head = ArrayToDLL(arr)
print(checkPalindromOptimized(head))
