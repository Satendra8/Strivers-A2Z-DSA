"""
Q. Implement Queue using Singly LinkedList

Operations Associated with queue are :

Enqueue     (Insert Node at Rare End )
Dequeue     (Delete Node from Front ) 
Peek            (Return value of Front Node without Dequing)
Empty         (Returns True when queue is empty else False)
Size             (Returns size of Queue) 

"""

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class Queue:
    """
    1. initialize start, end and size
    2. Functions
        i. push
        ii. Top
        iii. pop
        iv. Size
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0

    def push(self, data):
        node = Node(data, None)
        if self.size == 0:
            self.start = node
        else:
            self.end.next = node
        self.end = node
        self.size += 1


    def pop(self):
        if self.size == 0:
            print("Queue is empty!")
            return -1

        x = self.start.data
        if self.size == 1:
            self.end = None
        self.start = self.start.next
        self.size -= 1
        return x

    def Top(self):
        if self.size == 0:
            print("Queue is empty!")
            return -1
        return self.start.data
    
    def Size(self):
        return self.size

q = Queue()
q.push(4)
q.push(2)
print(q.pop())
print(q.pop())
q.push(5)
print(q.Top())