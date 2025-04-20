"""
Q. Given a linked list where nodes can contain values 0s, 1s, and 2s only. The task is to segregate 0s, 1s, and 2s linked list such that all zeros segregate to the head side, 2s at the end of the linked list, and 1s in the middle of 0s and 2s.

Input: LinkedList: 1->2->2->1->2->0->2->2
Output: 0->1->1->2->2->2->2->2
Explanation: All the 0s are segregated to the left end of the linked list, 2s to the right end of the list, and 1s in between.

Input: LinkedList: 2->2->0->1
Output: 0->1->2->2
Explanation: After arranging all the 0s,1s and 2s in the given format, the output will be 0 1 2 2.

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

def insert_at_last(head, val):
    new = Node(val)
    if head is None:
        return new
    
    temp = head
    while(temp.next):
        temp = temp.next
    temp.next = new
    return head


def sortList(node):
    """
    1. Brute Force Approach
    2. Create 3 LL for 0,1 and 2
    3. insert 0 in node0, 1 in node1 and 2 in node2
    4. make node0 as head, and mark last node of node0 point to head of node1
    5. mark last node of node1 point to head of node2
    6. Time Complexity: O(N^2)
    7. Space Complexity: O(N)
    """
    temp = node
    node0 = None
    node1 = None
    node2 = None

    while(temp):
        if temp.data == 0:
            node0 = insert_at_last(node0, 0)
        elif temp.data == 1:
            node1 = insert_at_last(node1, 1)
        else:
            node2 = insert_at_last(node2, 2)
        temp = temp.next
    final_head = node0
    while(node0.next):
        node0 = node0.next
    node0.next = node1

    while(node1.next):
        node1 = node1.next
    node1.next = node2
    return final_head

def insert_at_begining(head, val):
    new = Node(val)

    if head is None:
        return new
    new.next = head
    return new


def sortListBetter(head):
    """
    1. Better Approach
    2. Create 3 LL for 0,1 and 2
    3. insert 0 in node0, 1 in node1 and 2 in node2
    4. make node0 as head, and mark last node of node0 point to head of node1
    5. mark last node of node1 point to head of node2
    6. Time Complexity: O(N^2)
    7. Space Complexity: O(N)
    """
    temp = head
    node0 = None
    node1 = None
    node2 = None

    while(temp):
        if temp.data == 0:
            node0 = insert_at_begining(node0, 0)
        elif temp.data == 1:
            node1 = insert_at_begining(node1, 1)
        else:
            node2 = insert_at_begining(node2, 2)
        temp = temp.next

    if node0 is None and node1 is None:
        return node2
    
    if node0 is None:
        final_head = node1
        while(node1.next):
            node1 = node1.next
        node1.next = node2
        return final_head

    if node1 is None:
        final_head = node0
        while(node0.next):
            node0 = node0.next
        node0.next = node2
        return final_head

    final_head = node0
    while(node0.next):
        node0 = node0.next
    if node0:
        node0.next = node1
    else:
        final_head = node1

    while(node1.next):
        node1 = node1.next
    node1.next = node2
    return final_head


def sortListStriver(head):
    """
    1. Brute Force Approach
    2. count number of 0, 1 and 2
    3. form a LL
    4. Time Complexity: O(2N)
    5. Space Complexity: O(N)
    """
    count0 = 0
    count1 = 0
    count2 = 0
    temp = head

    while(temp):
        if temp.data == 0:
            count0 += 1
        elif temp.data == 1:
            count1 += 1
        else:
            count2 += 1
        temp = temp.next
    
    temp = head

    while(temp):
        if count0 > 0:
            temp.data = 0
            count0 -= 1
        elif count1 > 0:
            temp.data = 1
            count1 -= 1
        else:
            temp.data = 2
            count2 -= 1
        temp = temp.next

    return head

def sortListStriverOptimal(head):
    """
    1. Optimal Approach
    2. Create 3 dummy node for 0,1 and 2
    3. insert 0 in node0, 1 in node1 and 2 in node2
    4. make node0 as head, and mark last node of node0 point to head of node1
    5. mark last node of node1 point to head of node2
    6. Time Complexity: O(N)
    7. Space Complexity: O(N)
    """
    if head is None or head.next is None:
        return head
    temp = head

    # taking dummy node
    head0 = Node(-1)
    head1 = Node(-1)
    head2 = Node(-1)

    zero = head0
    one = head1
    two = head2

    while(temp):
        if temp.data == 0:
            zero.next = temp
            zero = zero.next
        elif temp.data == 1:
            one.next = temp
            one = one.next
        else:
            two.next = temp
            two = two.next
        temp = temp.next

    zero.next = head1.next if head1.next else head2.next
    one.next = head2.next
    two.next = None
    return head0.next

arr1 = [0,0,2,2,2]
head1 = ArrayToDLL(arr1)
# head = sortList(head)
head = sortListStriverOptimal(head1)
printLL(head)


"""

zero = -1 -> 0 -> 0 -> 0
one = -1 -> 1 -> 1
two = -1 -> 2 -> 2 -> 2

if not 1s, zero will be point to 2
if not 0s, then zero.next id already pointing to 1s next
if not 2s, fine one.next already pointing to null
if all three present one.next points to head2.next
** never forget to make two.next NULL

"""

def sort(head):
    zero_head = Node(-1)
    one_head = Node(-1)
    two_head = Node(-1)

    zero = zero_head
    one = one_head
    two = two_head

    temp = head

    while temp:
        if temp.data == 0:
            zero.next = temp
            zero = temp
        elif temp.data == 1:
            one.next = temp
            one = temp
        else:
            two.next = temp
            two = temp
        temp = temp.next

    two.next = None
    if not zero_head.next:
        one.next = two_head.next
        return one_head.next
    if not one_head.next:
        zero.next = two_head.next
    else:
        zero.next = one_head.next
        one.next = two_head.next


    return zero_head.next