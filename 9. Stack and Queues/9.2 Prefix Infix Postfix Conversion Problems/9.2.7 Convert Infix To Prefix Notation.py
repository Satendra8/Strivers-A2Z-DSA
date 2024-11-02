"""
Q. Given an infix expression, Your task is to convert the given infix expression to a prefix expression.

Example 1:
Input: x+y*z/w+u
Output: ++x/*yzwu
Explanation: Infix to prefix

Example 2:
Input: a+b
Output: +ab
Explanation: Infix to prefix
"""

def getPrecedence(c):
    if c == '^':
        return 3
    if c == '*' or c == '/':
        return 2
    if c == '+' or c == '-':
        return 1
    return -1


def infixToPrefix(s):
    """
    1. reverse the string
    2. infix to postfix
    3. reverse the ans
    4. edge case ^^ cannot store 2 powers in stack together
    """
    s = s[::-1]
    ans = ""
    stack = []

    for l in s:
        if (l >= 'A' and l <= 'Z') or (l >= 'a' and l <= 'z') or (l.isdigit()):
            ans += l
        elif l in ['+', '-', '*', '/', '^']:
            if l == '^':
                while stack and getPrecedence(l) <= getPrecedence(stack[-1]):
                    ans += stack.pop()
            else:
                while stack and getPrecedence(l) < getPrecedence(stack[-1]):
                    ans += stack.pop()
            stack.append(l)
        else:
            if l == ')':
                stack.append(l)
            else:
                while stack and stack[-1] != ')':
                    ans += stack.pop()
                stack.pop()
    while stack:
        ans += stack.pop()
    return ans[::-1]


s = "(A+B)*C-D+F"
print(infixToPrefix(s))


"""
s = "(A+B)*C-D+F"
s[::-1] = "F+D-C*)B+A("

l        stack     ans
F                  F
+         +        F
D         +        FD
-         +-       FD
C         +-       FDC
*         +-*      FDC
)         +-*)     FDC
B         +-*)     FDCB
+         +-*)+    FDCB
A         +-*)+    FDCBA
(         +-*      FDCBA+


ans = FDCBA+*-+

ans[::-1] = +-*+ABCDF
"""