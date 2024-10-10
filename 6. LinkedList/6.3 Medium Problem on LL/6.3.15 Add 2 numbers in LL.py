"""
Q. Given the heads of two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

Input Format: 
(Pointer/Access to the head of the two linked lists)

num1  = 243, num2 = 564

l1 = [2,4,3]
l2 = [5,6,4]

Result: sum = 807; L = [7,0,8]

Explanation: Since the digits are stored in reverse order, reverse the numbers first to get the or
original number and then add them as → 342 + 465 = 807. Refer to the image below.


Input Format: 
(Pointer/Access to the head of the two linked lists)

l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]

Result: [8,9,9,9,0,0,0,1]

Explanation: Since the digits are stored in reverse order, reverse the numbers first to get the
original number and then add them as → 9999999 + 9999 = 8999001. Refer to the image below.
"""



class Node:
    def __init__(self, val, prev=None, next=None):
        self.prev = prev
        self.val = val
        self.next = next


def printLL(head):
    mover = head
    while(mover):
        print(mover.val, end=" ")
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


def AddTwoNumbersLeetcode(l1, l2):
    if l1 is None and l2 is None:
        return None
    
    if l1 is None:
        return l2
    
    if l2 is None:
        return l1

    temp1 = l1
    temp2 = l2
    temp1_prev = None
    temp2_prev = None
    count1 = countLL(l1)
    count2 = countLL(l2)

    ans_head = l1 if count1 > count2 else l2

    carry = 0
    while(temp1 and temp2):
        num  = temp1.val + temp2.val + carry
        if num > 9:
            rem = num % 10
            carry = 1
            ans_head.val = rem
        else:
            carry = 0
            ans_head.val = num

        ans_head = ans_head.next
        temp1_prev = temp1
        temp2_prev = temp2
        temp1 = temp1.next
        temp2 = temp2.next

    while(temp1):
        num  = temp1.val + carry
        if num > 9:
            rem = num % 10
            carry = 1
            ans_head.val = rem
        else:
            carry = 0
            ans_head.val = num

        ans_head = ans_head.next
        temp1_prev = temp1
        temp1 = temp1.next

    while(temp2):
        num  = temp2.val + carry
        if num > 9:
            rem = num % 10
            carry = 1
            ans_head.val = rem
        else:
            carry = 0
            ans_head.val = num

        ans_head = ans_head.next
        temp2_prev = temp2
        temp2 = temp2.next


    if count1 > count2:
        if carry == 1:
            new = Node(1)
            temp1_prev.next = new
        return l1
    else:
        if carry == 1:
            new = Node(1)
            temp2_prev.next = new
        return l2
        

def AddTwoNumbers(l1, l2):
    if l1 is None and l2 is None:
        return None
    
    if l1 is None:
        return l2
    
    if l2 is None:
        return l1

    temp1 = l1
    temp2 = l2
    count1 = countLL(l1)
    count2 = countLL(l2)

    ans_head = l1 if count1 > count2 else l2

    carry = 0
    while(temp1 and temp2):
        num  = temp1.data + temp2.data + carry
        if num > 9:
            rem = num % 10
            carry = 1
            ans_head.data = rem
        else:
            carry = 0
            ans_head.data = num

        ans_head = ans_head.next
        temp1 = temp1.next
        temp2 = temp2.next

    while(temp1):
        num  = temp1.data + carry
        if num > 9:
            rem = num % 10
            carry = 1
            ans_head.data = rem
        else:
            carry = 0
            ans_head.data = num

        ans_head = ans_head.next
        temp1 = temp1.next

    while(temp2):
        num  = temp2.data + carry
        if num > 9:
            rem = num % 10
            carry = 1
            ans_head.data = rem
        else:
            carry = 0
            ans_head.data = num

        ans_head = ans_head.next
        temp2 = temp2.next

    if count1 > count2:
        ans1 = reverse(l1)
        if carry == 1:
            new = Node(1)
            new.next = ans1
            return new
        return ans1
    else:
        ans2 = reverse(l2)
        if carry == 1:
            new = Node(1)
            new.next = ans1
            return new
        return ans2
        


def AddTwoNumbersStriver(l1, l2):
    if l1 is None and l2 is None:
        return None
    
    if l1 is None:
        return l2
    
    if l2 is None:
        return l1

    temp1 = l1
    temp2 = l2
    carry = 0
    dummy_head = Node(-1)
    dummy = dummy_head
    
    while(temp1 or temp2):
        num = 0
        if temp1:
            num += temp1.data
            temp1 = temp1.next

        if temp2:
            num += temp2.data
            temp2 = temp2.next

        num += carry
        if num > 9:
            carry = 1
            num = num % 10
        else:
            carry = 0
        new = Node(num)
        dummy.next = new
        dummy = new

    if carry == 1:
        new = Node(1)
        dummy.next = new
        dummy = new

    return dummy_head.next


arr1 = [2,4,9]
arr2 = [5,6,4,9]
head1 = ArrayToDLL(arr1)
head2 = ArrayToDLL(arr2)
head = AddTwoNumbersStriver(head1, head2)
printLL(head)

"""
Dry Run 1:
    arr1 = [2,4,3]
    arr2 = [5,6,4]

    5 -> arr2 = [7], carry=0
    6 -> arr2 = [7,0], carry=1
    4 -> arr2 = [7,0,8], carry=0

    reverse = [8,0,7]

Dry Run 2:

    arr1 = [9,9,9,9,9,9,9]
    arr2 = [9,9,9,9]

9 -> = arr1 = [8,], carry=1
9 -> = arr1 = [8,9], carry=1
9 -> = arr1 = [8,9,9], carry=1
9 -> = arr1 = [8,9,9,9], carry=1

arr2 = ends

9 -> = arr1 = [8,9,9,9,0], carry=1
9 -> = arr1 = [8,9,9,9,0], carry=1
9 -> = arr1 = [8,9,9,9,0,0], carry=1
9 -> = arr1 = [8,9,9,9,0,0,0], carry=1

reverse = [0,0,0,9,9,9,8]

create new node [1]

ans1 = [1,0,0,0,9,9,9,8]



"""


"""
l1 = [2,4,9]
l2 = [5,6,4,9]

[7,0,4,]



"""