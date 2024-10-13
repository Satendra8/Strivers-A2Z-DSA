"""
Q. Given a doubly linked list of n nodes sorted by values, the task is to remove duplicate nodes present in the linked list.


Example 1:

Input:
n = 6
1<->1<->1<->2<->3<->4
Output:
1<->2<->3<->4
Explanation:
Only the first occurance of node with value 1 is 
retained, rest nodes with value = 1 are deleted.
Example 2:

Input:
n = 7
1<->2<->2<->3<->3<->4<->4
Output:
1<->2<->3<->4
Explanation:
Only the first occurance of nodes with values 2,3 and 4 are 
retained, rest repeating nodes are deleted.

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
    if not arr:
        return None
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


def removeDuplicates(head):
    """
    1. Optimal Approach
    2. handle duplicate at first node (move head 1 furthur to check match with prev element)
    3. if prev and current match then make prev to point next and next to prev
    4. handle duplicate at last node (point next to prev if this is node last node)
    5. Time Complexity: O(N)
    6. Space Complexity: O(1)
    """
    if head is None or head.next is None:
        return head
    # handle duplicate at first node
    temp = head.next

    while(temp):
        if temp.prev.data == temp.data:
            temp.prev.next = temp.next
            if temp.next:
                #handle duplicate at last node
                temp.next.prev = temp.prev
        temp = temp.next

    return head


arr = [1,1,1,2,3,4,4]
head = ArrayToDLL(arr)
head = removeDuplicates(head)
printLL(head)

"""
Dry Run 1:

arr = [1,1,1,2,3,4]

1 -> [1,1,1,2,3,4]
1 -> [1,1,2,3,4]
1 -> [1,2,3,4]
2 -> [1,2,3,4]
3 -> [1,2,3,4]
4 -> [1,2,3,4]


arr = [1,1,1,2,3,4,4]

1 -> [1,1,1,2,3,4,4]
1 -> [1,1,2,3,4,4]
1 -> [1,2,3,4,4]
2 -> [1,2,3,4,4]
3 -> [1,2,3,4,4]
4 -> [1,2,3,4,4]
4 -> [1,2,3,4,4]


"""