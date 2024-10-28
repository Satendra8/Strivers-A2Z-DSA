"""
Q. Implement a stack using an array.
"""

class Stack:

    def __init__(self):
        self.top = -1
        self.size = 10
        self.arr = [0]*self.size
    
    def push(self, n):
        # Time Complexity: O(1)
        self.top += 1
        self.arr[self.top] = n

    def Top(self):
        # Time Complexity: O(1)
        if self.top == -1:
            print("stack is empty!")
            return
        return self.arr[self.top]

    def pop(self):
        # Time Complexity: O(1)
        if self.top == -1:
            print("stack is empty!")
            return
        x = self.arr[self.top]
        self.top -= 1
        return x

    def Size(self):
        # Time Complexity: O(1)
        return self.top + 1


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.Top())
s.pop()
print(s.Top())
s.pop()
s.pop()
print(s.Size())