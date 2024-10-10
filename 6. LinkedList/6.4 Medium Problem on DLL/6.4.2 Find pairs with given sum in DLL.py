"""
Q. Given a sorted doubly linked list of positive distinct elements, the task is to find pairs in a doubly-linked list whose sum is equal to given value target.

Example 1:

Input:  
1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9
target = 7
Output: (1, 6), (2,5)
Explanation: We can see that there are two pairs 
(1, 6) and (2,5) with sum 7.

Example 2:

Input: 
1 <-> 5 <-> 6
target = 6
Output: (1,5)
Explanation: We can see that there is one pairs  (1, 5) with sum 6.

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


def findPairsWithGivenSum(head, target):
    """
    Brute Force
    """
    ans = []
    temp = head
    s = set()

    while(temp):
        rem = target - temp.data
        if (rem) in s:
            ans.append([rem, temp.data])
        s.add(temp.data)
        temp = temp.next
    return ans


def findPairsWithGivenSumOptimal(head, target):
    if head is None:
        return []
    temp = head
    ans = []
    #find last node
    while(temp.next):
        temp = temp.next
    
    right = temp
    left = head

    while(left.data < right.data):
        num = left.data + right.data
        if num == target:
            ans.append([left.data, right.data])
            left = left.next
            right = right.prev
        elif num > target:
            right = right.prev
        else:
            left = left.next
    return ans

arr = [1,5,6]
x = 6
head = ArrayToDLL(arr)
ans = findPairsWithGivenSumOptimal(head, x)
print(ans)

"""
Dry Run 1:

arr = [1,2,4,5,6,8,9]
x = 7


ans = [[2,5], [1,6], ]
s = {1,2,4,5,6,8,9}

1 -> 
2 -> 
4 -> 
5 -> 
6 -> 
8 -> 
9 -> 

"""