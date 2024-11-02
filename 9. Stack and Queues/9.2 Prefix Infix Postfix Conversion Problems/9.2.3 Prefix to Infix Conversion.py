"""
Q. You are given a string S of size N that represents the prefix form of a valid mathematical expression.
The string S contains only lowercase and uppercase alphabets as operands and the operators are +, -, *, /, %, and ^.Convert it to its infix form.

Example 1:

Input: 
*-A/BC-/AKL
Output: 
((A-(B/C))*((A/K)-L))
Explanation: 
The above output is its valid infix form.
"""

def prefixToInfix(s):
    """
    1. iterate from last
    2. push operand in stack
    3. for operator, pop 2 elements do (A+B) and push back to stack
    4. Time Complexity: O(N)
    5. Space Complexity: O(N)
    """
    stack = []
    for i in range(len(s)-1, -1, -1):
        if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z') or (s[i].isdigit()):
            stack.append(s[i])
        else:
            first = stack.pop()
            second = stack.pop()
            stack.append(f'({first}{s[i]}{second})')
    return stack[0]

s = "*+PQ-MN"
print(prefixToInfix(s))

"""
s = "*+PQ-MN"

i            stack
N            N
M            N, M
-            (M-N)
Q            (M-N), Q
P            (M-N), Q, P
+            (M-N), (P+Q)
*            ((M-N)*(P+Q))
"""