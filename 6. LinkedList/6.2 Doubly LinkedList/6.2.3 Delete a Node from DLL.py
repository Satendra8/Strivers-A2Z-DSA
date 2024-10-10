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
    mover = head

    while(mover):
        print(mover.data, end=" ")
        mover = mover.next
    print()


def deleteHead(head):
    #edge case if there is no element or single element
    if head is None or head.next is None:
        return None
    head = head.next
    head.prev = None
    return head


def deleteTail(head):
    #edge case if there is no element or single element
    if head is None or head.Next is None:
        return None
    mover = head

    while(mover.next.next):
        mover = mover.next
    mover.next = None
    return head


def deleteKth(head, index):
    if head is None:
        return None

    mover = head
    i = 0
    while(mover.next):
        if (index == i):
            break
        mover = mover.next
        i += 1

    # if there is a single Node
    if mover.prev is None and mover.next is None:
        return None

    # if it is first Node
    if mover.prev is None:
        mover.next.prev = None
        return mover.next

    # if it is last node
    if mover.next is None:
        mover.prev.next = None
        return head

    # if it is in mid
    mover.next.prev = mover.prev
    mover.prev.next = mover.next
    return head


def deleteNode(node):
    # if there is no node
    if node is None:
        return None
    
    # if this is last node
    if node.next is None:
        node.prev.next = None
        return
    prev = node.prev
    next = node.next

    prev.next = next
    next.prev = prev

arr = [1,2, 3]
head = ArrayToDLL(arr)
deleteNode(head.next.next)
printLL(head)