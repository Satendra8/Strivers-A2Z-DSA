"""
Q. Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]


Example 2:

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
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


def segregate(head):
    """
    1. Brute force Striver Sheet
    2. check if number is odd add it to odd LL
    3. check if number is even add it to even LL
    4. mark even.next = odd_head
    5. Time Complexity: O(N)
    5. Space Complexity: O(N)
    
    """
    temp = head
    odd = None
    even = None

    while(temp):
        new_node = Node(temp.data)
        if temp.data % 2 == 1:
            if odd:
                odd.next = new_node
            else:
                odd_head = new_node
            odd = new_node
        else:
            if even:
                even.next = new_node
            else:
                even_head = new_node
            even = new_node
        temp = temp.next 
    even.next = odd_head
    return even_head


def insert_at_end(head, val):
    new = Node(val)
    temp = head

    if head is None:
        return new
    while(temp.next):
        temp = temp.next
    temp.next = new
    return head


def leetcodeSegregateBrute(head):
    """
    1. Brute Force Approach
    2. save all number in arr
    3. take oddLL and evenLL
    4. put even node to evenLL
    5. put odd node to oddLL
    6. point odd.next = even_head
    7. Time Complexity: O(N^2)
    8. Space Complexity: O(N)
    """
    temp = head
    arr = []

    while(temp):
        arr.append(temp.data)
        temp = temp.next

    odd_head = None
    even_head = None
    for index, value in enumerate(arr, 1):
        if index % 2 == 1:
            odd_head = insert_at_end(odd_head, value)
        else:
            even_head = insert_at_end(even_head, value)

    temp_odd = odd_head
    while(temp_odd.next):
        temp_odd = temp_odd.next
    temp_odd.next = even_head
    
    return odd_head


def leectcodeSegregateBetter(head):
    """
    1. Better Approach
    2. create an array of odd indexes value
    3. now add even indexes value at last in same array
    4. now create arr to LL
    5. Time Complexity: O(N)
    6. Space Complexity: O(N)
    """

    temp = head
    arr = []
    while(temp and temp.next):
        arr.append(temp.data)
        temp = temp.next.next

    if temp:
        arr.append(temp.data)
    temp = head.next
    while(temp and temp.next):
        arr.append(temp.data)
        temp = temp.next.next
    if temp:
        arr.append(temp.data)
    head = ArrayToDLL(arr)
    return head



def leetcodeSegregateOptimal(head):
    """
    1. Optimal Approach
    2. take odd = head and even = head.next
    3. mark odd.next = odd.next.next and make odd = odd.next
    4. mark even.next = even.next.next and make even = even.next
    5. odd last will be pointing to even head
    6. Time Complexity: O(N)
    6. Space Complexity: O(1)
    """
    temp = head

    odd_head = temp
    even_head = temp.next
    odd = odd_head
    even = even_head

    while(odd and odd.next and even and even.next):
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next

    odd.next = even_head
    
    return odd_head


arr = [2,1,3,5,6,4,7]
head = ArrayToDLL(arr)
head = leectcodeSegregateBetter(head)
printLL(head)
