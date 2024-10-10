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


def insertBeforeHead(head, val):
    new = Node(val, None, head)
    head.prev = new
    return new


def insertBeforeTail(head, val):
    # if it is head
    if head.next is None:
        return insertBeforeHead(head, val)
    mover = head
    while(mover.next):
        mover = mover.next
    print(mover.data)
    new  = Node(val, mover.prev, mover)
    mover.prev.next = new
    mover.prev = new
    return head

def insertBeforeKth(head, k, val):
    #if before head
    if k == 1:
        return insertBeforeHead(head, val)
    i = 1
    mover = head

    while (mover.next):
        if i == k:
            break
        mover = mover.next
        i += 1

    new = Node(val, mover.prev, mover)
    mover.prev.next = new
    mover.prev = new
    return head


def insertBeforeNode(node, val):
    new = Node(val, node.prev, node)
    node.prev.next = new
    node.prev = new
    

def printLL(head):
    mover = head

    while(mover):
        print(mover.data, end=" ")
        mover = mover.next
    print()

arr = [1,2,3,4,5]
head = ArrayToDLL(arr)
insertBeforeNode(head.next.next, 100)
printLL(head)