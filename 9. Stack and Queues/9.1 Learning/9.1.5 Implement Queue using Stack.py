"""
Q. Given a Stack having some elements stored in it. Can you implement a
Queue using the given Stack?

Queue: A Queue is a linear data structure that works on the basis of FIFO(First in First out). This means the element added at first will be removed first from the Queue.
"""

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        push operation is O(N)
        1. move all elements to stack2
        2. insert element in stack1
        3. move back elements to stack1 again
        4. Time Complexity: O(N)
        5. Space Complexity: O(N)
        """
        for i in range(len(self.s1)):
            self.s2.append(self.s1.pop())

        self.s1.append(x)

        for i in range(len(self.s2)):
            self.s1.append(self.s2.pop())
    
    def pop(self):
        return self.s1.pop()
    
    def peek(self):
        return self.s1[-1]
    
    def empty(self):
        return len(self.s1) == 0


class Queue1:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)
    
    def Pop(self):
        """
        pop operation is O(N)
        1. move s1 -> s2
        2. pop from s2
        3. move back s2 -> s1
        4. Time Complexity: O(N)
        5. Space Complexity: O(N)
        """
        for i in range(len(self.s1)):
            self.s2.append(self.s1.pop())
        x = self.s2.pop()
        for i in range(len(self.s2)):
            self.s1.append(self.s2.pop())
        return x

    def peek(self):
        """
        peak operation is O(N)
        1. move s1 -> s2
        2. store top element
        3. move back s2 -> s1
        4. Time Complexity: O(N)
        5. Space Complexity: O(N)
        """
        for i in range(len(self.s1)):
            self.s2.append(self.s1.pop())
        x = self.s2[-1]
        for i in range(len(self.s2)):
            self.s1.append(self.s2.pop())
        return x

    def empty(self):
        return len(self.s1) == 0

 
q = Queue1()
q.push(3)
q.push(4)
q.push(1)
print(q.s1)
print(q.peek())
q.Pop()
print(q.peek())



from queue import LifoQueue

class Queue:
    def __init__(self):
        self.stack1 = LifoQueue()

    def push(self, n):
        stack2 = LifoQueue()
        for i in range(self.stack1._qsize()):
            stack2.put(self.stack1.get())
        self.stack1.put(n)
        for i in range(stack2._qsize()):
            self.stack1.put(stack2.get())

    def pop(self):
        return self.stack1.get()

    def top(self):
        return self.stack1.queue[-1]
    
    def size(self):
        return self.stack1._qsize()

S = Queue()
S.push(4)
S.push(9)
S.push(2)
S.push(5)
print(S.top()) #4
print(S.pop()) #4
print(S.pop()) #9
print(S.pop()) #2
print(S.top()) #5
S.push(1)
print(S.top()) #5