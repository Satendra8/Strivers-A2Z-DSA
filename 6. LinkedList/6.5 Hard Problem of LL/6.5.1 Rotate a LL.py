"""
Q. Given the head of a singly linked list containing integers, shift the elements of the linked list to the right by k places and return the head of the modified list. Do not change the values of the nodes, only change the links between nodes.

Examples:
Input: head -> 1 -> 2 -> 3 -> 4 -> 5, k = 2

Output: head -> 4 -> 5 -> 1 -> 2 -> 3

Explanation:

List after 1 shift to right: head -> 5 -> 1 -> 2 -> 3 -> 4.

List after 2 shift to right: head -> 4 -> 5 -> 1 -> 2 -> 3.

Input: head -> 1 -> 2 -> 3 -> 4 -> 5, k = 4

Output: head -> 2 -> 3 -> 4 -> 5 -> 1

Explanation:

List after 1 shift to right: head -> 5 -> 1 -> 2 -> 3 -> 4.

List after 2 shift to right: head -> 4 -> 5 -> 1 -> 2 -> 3.

List after 3 shift to right: head -> 3 -> 4 -> 5 -> 1 -> 2.

List after 4 shift to right: head -> 2 -> 3 -> 4 -> 5 -> 1.
"""

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
    temp = head
    while(temp):
        print(temp.data, end=" ")
        temp = temp.next
    print()


def countLL(head):
    temp = head
    counter = 0

    while(temp):
        counter += 1
        temp = temp.next
    return counter

def rotate(head, k):
    """
    1. find count of LL
    2. do k = k%N to find actual rotation 0 < k < N
    3. base case, if k = 0 return head as it is
    3. find the node after which rotation performed, make it's next new_head
    4. mark tail of new_head pointing to head
    5. return new head
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    N = countLL(head)
    k = k % N

    if k == 0:
        return head
    
    node_after = N - k
    temp = head

    count = 0

    while temp:
        count += 1
        if count == node_after:
            break
        temp = temp.next
    
    new_head = temp.next
    new_temp = new_head
    temp.next = None

    while new_temp.next:
        new_temp = new_temp.next
    new_temp.next = head
    return new_head


arr = [1,2,3,4,5]
head = ArrayToDLL(arr)
head = rotate(head, 6)
printLL(head)