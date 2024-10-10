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

arr = [1,2,3,4,5,6,7]
head = ArrToLinkedList(arr)