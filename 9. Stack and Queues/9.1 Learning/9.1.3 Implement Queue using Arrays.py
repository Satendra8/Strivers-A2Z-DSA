"""
Q. Implement Queue Data Structure using Array with all functions like pop, push, top, size, etc.


Example:

Input: push(4)
       push(14)
       push(24)
       push(34)
       top()
       size()
       pop()

Output: 

The element pushed is 4
The element pushed is 14
The element pushed is 24
The element pushed is 34
The peek of the queue before deleting any element 4
The size of the queue before deletion 4
The first element to be deleted 4
The peek of the queue after deleting an element 14
The size of the queue after deleting an element 3

"""

class Queue:
    def __init__(self):
        self.start = -1
        self.end = -1
        self.current_size = 0
        self.capacity = 4
        self.arr = [0]*self.capacity

    def push(self, n):
        """
        PUSH
        1. edge case: check is queue is full
        2. edge case: handle circular insert by % (self.end + 1) % self.capacity
        3. edge case: if queue is empty incrment both start and end pointer
        4. edge case: increase current size
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.current_size < self.capacity:
            self.end = (self.end + 1) % self.capacity
            if self.current_size == 0:
                self.start += 1
            self.arr[self.end] = n
            self.current_size += 1
        else:
            print("Stack is full!")


    def pop(self):
        """
        POP
        1. edge case: check if queue is empty
        2. edge case: if there is only 1 element then mark start and end at -1
        3. edge case: handle circular pop (self.start + 1) % self.capacity
        4. edge case: decrease current size
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.current_size == 0:
            print("Stack is empty!")
            return -1

        x = self.arr[self.start]

        if self.current_size == 1:
            self.start = -1
            self.end = -1
        else:
            self.start = (self.start + 1) % self.capacity
        self.current_size -= 1
        return x


    def top(self):
        if self.start == -1:
            print("Queue is empty!")
            return
        print(self.arr[self.start])

    
    def size(self):
        return self.current_size


q = Queue()
q.push(5)
q.push(4)
q.push(3)
q.push(3)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
q.push(2)
q.push(3)
q.top()