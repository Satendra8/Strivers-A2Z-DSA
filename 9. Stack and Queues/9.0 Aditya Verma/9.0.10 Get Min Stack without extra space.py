"""
Q. Given q queries, You task is to implement the following four functions for a stack:

push(x) - Insert an integer x onto the stack.
pop() - Remove the top element from the stack.
peek() - Return the top element from the stack. If the stack is empty, return -1.
getMin() - Retrieve the minimum element from the stack in O(1) time. If the stack is empty, return -1.
Each query can be one of the following:

1 x : Push x onto the stack.
2 : Pop the top element from the stack.
3: Return the top element from the stack. If the stack is empty, return -1.
4: Return the minimum element from the stack.
Examples:

Input: q = 7, queries = [[1, 2], [1, 3], [3], [2], [4], [1, 1], [4]]
Output: [3, 2, 1]
Explanation: 
push(2): Stack is [2]
push(3): Stack is [2, 3]
peek(): Top element is 3
pop(): Removes 3, stack is [2]
getMin(): Minimum element is 2
push(1): Stack is [2, 1]
getMin(): Minimum element is 1
Input: q = 4, queries = [[1, 4], [1, 2], [4], [3]]
Output: [2, 2]
Explanation: 
push(4): Stack is [4]
push(2): Stack is [4, 2]
getMin(): Minimum element is 2
peek(): Top element is 2
Input: q = 5, queries = [[1, 10], [4], [1, 5], [4], [2]]
Output: [10, 5]
Explanation: 
push(10): Stack is [10]
getMin(): Minimum element is 10
push(5): Stack is [10, 5]
getMin(): Minimum element is 5
pop(): Removes 5, stack is [10]
"""

class Stack:
    def __init__(self):
        self.S = []
        self.minEle = -1

    def getMin(self):
        if not self.S:
            return -1
        return self.minEle
    
    def peek(self):
        """
        1. peak element is either present at minElem or top of the stack
        """
        if not self.S:
            return -1
        if self.S[-1] < self.minEle:
            return self.minEle
        return self.S[-1]
    
    def push(self, n):
        """
        1. we are using variable here to keep minElement
        2. if an element is deleted then how to go to prev smaller is a chalange
        3. if this is not smaller then push as it is
        4. we are pushing 2*n-minEle in stack and n in minEle
        """
        if not self.S:
            self.S.append(n)
            self.minEle = n
        elif n < self.minEle:
            self.S.append(2*n-self.minEle)
            self.minEle = n
        else:
            self.S.append(n)
    
    def pop(self):
        """
        1. pop the element, and reset the minEle to prev min
        2. get the prev min using the decode formula 2*minEle - stack.top()
        3. return the poped element
        """
        if not self.S:
            return -1
        x = self.S.pop()
        if x < self.minEle:
            self.minEle = 2 * self.minEle - x
        return x
    

st = Stack()
arr = [18, 19, 29, 15, 16]

st.push(18)
st.push(19)
st.push(29)
st.push(15)
st.push(16)
print(st.getMin())



from queue import LifoQueue

class Stack:
    def __init__(self):
        self.stack = LifoQueue()
        self.minEle = 0

    def push(self, n):
        if self.stack.empty():
            self.stack.put(n)
            self.minEle = n
        
        elif n > self.minEle:
            self.stack.put(n)
        else:
            self.stack.put(2*n-self.minEle)
            self.minEle = n
        return

    def pop(self):
        if self.stack.empty():
            return -1
        if self.stack.queue[-1] > self.minEle:
            return self.stack.get()
        x = self.minEle
        self.minEle = 2*self.minEle - self.stack.get()
        return x

    def top(self):
        if self.stack.empty():
            return -1
        if self.minEle > self.stack.queue[-1]:
            return self.minEle
        return self.self.stack.queue[-1]

    def minElement(self):
        if self.stack.empty():
            return -1
        return self.minEle

st = Stack()
arr = [18, 19, 29, 15, 16]

st.push(18)
st.push(19)
st.push(29)
st.push(15)
st.push(16)
st.pop()
st.pop()
print(st.minElement())