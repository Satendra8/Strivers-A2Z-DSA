"""
Q. Implement a Stack using a single Queue.

Explanation: 
push(): Insert the element in the stack.
pop(): Remove and return the topmost element of the stack.
top(): Return the topmost element of the stack
size(): Return the size of the stack
"""

from queue import Queue
class MyStackBrute:

    def __init__(self):
        self.q = Queue()

    def push(self, x):
        """
        PUSH
        1. Brute Force Approach
        2. use a tempreary queue to transfer elements
        3. Time Complexity: O(N)
        4. Space Complexity: O(N)
        """
        temp_q = Queue()
        temp_q.put(x)
        for i in range(self.q.qsize()):
            temp_q.put(self.q.get())
        
        for j in range(temp_q.qsize()):
            self.q.put(temp_q.get())

    def pop(self):
        return self.q.get()

    def top(self):
        return self.q.queue[0]

    def empty(self):
        return self.q.empty()



class MyStack:
    def __init__(self):
        self.q = Queue()

    def push(self, x):
        """
        PUSH
        1. Optimal Approach
        2. insert one element and move n-1 elements to right side
        3. Time Complexity: O(N)
        4. Space Complexity: O(1)
        """
        self.q.put(x)
        for i in range(self.q.qsize()-1):
            self.q.put(self.q.get())

    def pop(self):
        return self.q.get()

    def top(self):
        return self.q.queue[0]

    def empty(self):
        return self.q.empty()

S = MyStack()
S.push(4)
S.push(9)
S.push(2)
S.push(5)
print(S.top())
S.pop()
S.pop()
S.pop()
print(S.top())
S.push(1)
print(S.top())