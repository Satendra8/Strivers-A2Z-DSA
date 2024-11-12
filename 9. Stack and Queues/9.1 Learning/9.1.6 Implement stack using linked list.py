"""
Q. Implement stack using linked list

"""

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    
class Stack:
    """
    1. initialize top and size
    2. Functions
        i. push
        ii. Top
        iii. pop
        iv. Size
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data, self.top)
        self.top = node
        self.size += 1

    def pop(self):
        """
        1. edge case: null check
        """
        if self.top is None:
            print("Stack is empty!")
            return -1
        x = self.top.data
        self.top = self.top.next
        self.size -= 1
        return x
    
    def Top(self):
        """
        1. edge case: null check
        """
        if self.top is None:
            print("Stack is empty!")
            return -1
        return self.top.data
    
    def Size(self):
        return self.size
    

s = Stack()
s.push(4)
s.push(2)
s.push(3)
s.push(1)
print(s.Top())
print(s.pop())
s.push(7)
print(s.Size())
print(s.Top())