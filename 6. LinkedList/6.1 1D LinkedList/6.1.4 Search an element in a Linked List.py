"""
Q. Given the head of a linked list and an integer value, find out whether the integer is present in the linked list or not. Return true if it is present, or else return false.

Example 1:

Input Format: 0->1->2, val = 2

Result True

Explanation: Since element 2 is present in the list, it will return true.


Example 2:

Input Format: 12->5->8->7, val = 6 

Result False

Explanation: The list does not contain element 6. Therefore, it returns false.

"""


class Node:
    def __init__(self, data1, next1 = None):
        self.data = data1
        self.next = next1

def ArrToLinkedList(arr):
    head = Node(arr[0])
    mover = head

    for i in range(1, len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp
    return head

def checkIfPresent(head, value):
    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    temp = head

    while(temp):
        if temp.data == value:
            return True
        temp = temp.next
    return False


arr = [1,2,3,4,5,6,7]
head = ArrToLinkedList(arr)
print(checkIfPresent(head, 5))