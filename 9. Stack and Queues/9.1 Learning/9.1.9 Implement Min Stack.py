"""
Q. Implement Min Stack | O(2N) and O(N) Space Complexity. Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Input Format:["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
[
[ ], [-2], [0], [-3], [ ], [ ], [ ], [ ]
]

Result: [null, null, null, null, -3, null, 0, -2]
Explanation: 
stack < long long > st
st.push(-2); Push element in stack
st.push(0); Push element in stack
st.push(-3); Push element in stack
st.getMin(); Get minimum element fromstack
st.pop(); Pop the topmost element
st.top(); Top element is 0
st.getMin(); Minimum element is -2
"""

class MinStackBrute:
    """
    Use two stacks to store nums and minimums
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        PUSH
        1. use 2 stack 1 to store numbers and 1 for minimums
        2. if min stack is empty or lesser number found insert in min stack
        3. Time Complexity: O(1)
        4. Space Complexity: O(2N)
        """
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        """
        POP
        1. if normal stack and min stack are same top are same pop both
        2. Time Complexity: O(1)
        3. Space Complexity: O(2N)
        """
        if not self.stack:
            print("Stack is empty")
            return
        x = self.stack.pop()
        if self.min_stack and x == self.min_stack[-1]:
            self.min_stack.pop()
        return x
    
    def top(self):
        if not self.stack:
            print("Stack is empty")
            return
        return self.stack[-1]

    def getMin(self):
        if not self.min_stack:
            print("min Stack is empty")
            return
        return self.min_stack[-1]
    

class MinStackBetter:
    """
    Use pair to store number and min
    """
    def __init__(self):
        self.stack = []

    def push(self, x):
        """
        PUSH
        1. use pair to store num and minimum [(-2,-2), (0, -2), (-3, -3)]
        2. Time Complexity: O(1)
        3. Space Complexity: O(2N)
        """
        if not self.stack:
            self.stack.append((x,x))
        else:
            minimum = min(x, self.stack[-1][1])
            self.stack.append((x, minimum))

    def pop(self):
        """
        POP
        1. pop element
        2. Time Complexity: O(1)
        3. Space Complexity: O(2N)
        """
        if not self.stack:
            print("Stack is empty")
            return
        x = self.stack.pop()
        return x[0]
    
    def top(self):
        if not self.stack:
            print("Stack is empty")
            return
        return self.stack[-1][0]

    def getMin(self):
        if not self.stack:
            print("min Stack is empty")
            return
        return self.stack[-1][1]


class MinStackOptimal:
    """
    Use 2 * x - min = (combination of x and min)
    """
    def __init__(self):
        self.stack = []
        self.min = 10**9

    def push(self, x):
        """
        PUSH
        1. store combination of min and val in stack use formula 2 * x - self.min
        2. if val < min then update min with value and store combination in stack
        2. Time Complexity: O(1)
        3. Space Complexity: O(N)
        """
        if not self.stack:
            self.stack.append(x)
            self.min = x
        else:
            if x < self.min:
                n = 2 * x - self.min
                self.stack.append(n)
                self.min = x
            else:
                self.stack.append(x)

    def pop(self):
        """
        POP
        1. pop the element
        2. if x < self.min then regenerate the min
        3. by using reverse formula 2 * self.min - x
        2. Time Complexity: O(1)
        3. Space Complexity: O(N)
        """
        if not self.stack:
            print("Stack is empty")
            return
        x = self.stack.pop()
        if x < self.min:
            self.min = 2 * self.min - x
        return x
    
    def top(self):
        if not self.stack:
            print("Stack is empty")
            return
        if self.stack[-1] < self.min:
            return self.min
        return self.stack[-1]

    def getMin(self):
        if not self.stack:
            print("min Stack is empty")
            return
        return self.min




s = MinStackOptimal()
s.push(-2)
s.push(0)
s.push(-3)
print(s.getMin())
print(s.pop())
print(s.getMin())