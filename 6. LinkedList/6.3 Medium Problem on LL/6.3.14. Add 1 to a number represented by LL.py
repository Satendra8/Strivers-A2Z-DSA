"""
Q. You are given a linked list where each element in the list is a node and have an integer data. You need to add 1 to the number formed by concatinating all the list node numbers together and return the head of the modified linked list. 

Note: The head represents the first element of the given array.

Input: LinkedList: 4->5->6
Output: 457

Explanation: 4->5->6 represents 456 and when 1 is added it becomes 457.

Input: LinkedList: 1->2->3
Output: 124
 
Explanation:  1->2->3 represents 123 and when 1 is added it becomes 124. 

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


def insert_at_beginning(head, val):
    new = Node(val)
    if head is None:
        return new
    
    new.next = head
    return new


def AddOne(head):
    temp = head

    num = 0
    while(temp):
        num = (num*10) + temp.data
        temp = temp.next
    num += 1

    new_head = None
    while(num):
        rem = num % 10
        new_head = insert_at_beginning(new_head, rem)
        num = num // 10
    return new_head


def reverse(head):
    if head is None or head.next is None:
        return head
    temp = head

    prev = None
    while(temp):
        next_pointer = temp.next
        temp.next = prev
        prev = temp
        temp = next_pointer

    return prev



def AddOneBetter(head):
    """
    1. reverse the LL
    2. iterate over and add carry like we do in addition
    3. reverse the LL again to get the number
    4. edge case [9,9,9] + 1 = [1,0,0,0]
    5. if carry is still one create a new node make it head
    6.Time Complexity: O(3N)
    7. Space Complexity: O(1)
    """
    r1 = reverse(head)
    temp = r1
    carry = 1

    while(temp):
        num = temp.data + carry
        if num == 10:
            carry = 1
            temp.data = 0
        else:
            temp.data = num
            carry = 0
        temp = temp.next

    r2 = reverse(r1)
    if carry == 1:
        new = Node(1)
        new.next = r2
        return new

    return r2


def helper(head):
    """
    1. using recursion
    2. base case when head is null, return carry 1
    3. if num == 10 replace node data with 0 and return carry 1
    """
    if head is None:
        return 1
    
    carry = helper(head.next)
    num = head.data + carry
    if num == 10:
        head.data = 0
        return 1
    else:
        head.data = num
        return 0

def AddOneOptimal(head):
    """
    4. edge case [9,9,9] + 1 = [1,0,0,0]
    5. if carry is still one create new node and return it as head
    6. Time Complexity: O(N)
    7. Space Complexity: O(N) for storing recursive call stack
    """
    carry = helper(head)
    if carry == 1:
        new = Node(1)
        new.next = head
        return new
    return head


arr1 = [9, 9, 9]
head = ArrayToDLL(arr1)
head = AddOneOptimal(head)

"""
Better Approach

arr1 = [1, 9, 9]
r1 = [9, 9, 1]


1. reverse the LL
2. iterate over and add carry like we do in addition
3. reverse the LL again to get the number
4. edge case [9,9,9] + 1 = [1,0,0,0]
5. if carry is still one create a new node make it head
6. Time Complexity: O(N)
7. Space Complexity: O(N) for storing recursive call stack


"""
