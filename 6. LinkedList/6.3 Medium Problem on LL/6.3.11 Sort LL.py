"""
Q. Given a linked list, sort its nodes based on the data value in them. Return the head of the sorted linked list.

Example 1:
Input:Linked List: 3 4 2 1 5

Output:Sorted List: 1 2 3 4 5

Explanation:  The input linked list when sorted from [3, 4, 2, 1, 5] results in a linked list with values: [1, 2, 3, 4, 5].


                
Example 2:
Input:List: 40 20 60 10 50 30

Output: Sorted List: 10 20 30 40 50 60

Explanation:  The input linked list when sorted from [40, 20, 60, 10, 50, 30] results in a linked list with values: [10, 20, 30, 40, 50, 60].
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



def Sort(head):
    """
    1. Brute Force Approach
    2. Create an Array From LinkedList
    3. sort the array
    4. Replace the soted array numbers to LinkedList
    5. Time Complexity: O(Nlogn)
    6. Space Complexity: O(N)
    """
    temp = head

    arr = []
    while(temp):
        arr.append(temp.data)
        temp = temp.next
    arr.sort()
    return ArrayToDLL(arr)


def findMidOfLL(head):
    temp = head
    hare = temp.next
    tortoise = temp

    while(hare and hare.next):
        hare = hare.next.next
        tortoise = tortoise.next
    return tortoise

def merge(head1, head2):
    if head1 is None and head2 is None:
        return None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.data <= head2.data:
        sorted_head = head1
        head1 = head1.next
    else:
        sorted_head = head2
        head2 = head2.next

    curr_head = sorted_head
    while(head1 and head2):
        if head1.data <= head2.data:
            curr_head.next = head1
            curr_head = curr_head.next
            head1 = head1.next

        else:
            curr_head.next = head2
            curr_head = curr_head.next
            head2 = head2.next

    while head1:
        curr_head.next = head1
        curr_head = head1
        head1 = head1.next

    while head2:
        curr_head.next = head2
        curr_head = head2
        head2 = head2.next

    return sorted_head


def SortOptimal(head):
    """
    Think of merge sort Algorithm
    1. Find middle of LL
    2. Sort the left part
    3. Sort the right part
    4. merge left and right sorted parts
    5. Time Complexity: O(Nlogn)
    6. Space Complexity: O(N)
    """
    if head is None or head.next is None:
        return head
    temp = head
    mid = findMidOfLL(temp)
    right = mid.next
    mid.next = None

    leftPart = SortOptimal(temp)
    rightPart = SortOptimal(right)
    return merge(leftPart, rightPart)

arr = [4,2,1,6,7,5]
head = ArrayToDLL(arr)
head = SortOptimal(head)
printLL(head)




def merge(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    if not head1 and not head2:
        return None

    new_head = Node(-1)
    temp = new_head
    left = head1
    right = head2

    while left and right:
        if left.data < right.data:
            temp.next = left
            temp = left
            left = left.next
        else:
            temp.next = right
            temp = right
            right = right.next

    while left:
        temp.next = left
        temp = left
        left = left.next
        
    while right:
        temp.next = right
        temp = right
        right = right.next

    return new_head.next
        
def midNode(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def sort(head):
    if head is None or head.next is None:
        return head

    mid = midNode(head)
    left = head
    right = mid.next
    mid.next = None
    printLL(left)

    leftNode = sort(left)
    rightNode = sort(right)

    return merge(leftNode, rightNode)



