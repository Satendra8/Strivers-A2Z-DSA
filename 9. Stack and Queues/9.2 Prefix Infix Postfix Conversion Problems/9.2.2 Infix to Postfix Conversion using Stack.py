"""
Q. Given an infix expression, Your task is to convert the given infix expression to a postfix expression.

Example 1:
Input: a+b*(c^d-e)^(f+g*h)-i
Output: abcd^e-fgh*+^*+i-
Explanation: Infix to postfix

Example 2:
Input: (p+q)*(m-n)
Output: pq+mn-*
Explanation: Infix to postfix
"""

def getPrecedence(s):
    if s == '^':
        return 3
    if s == '*' or s == '/':
        return 2
    if s == '+' or s == '-':
        return 1
    return -1

def InfixtoPostfix(exp):
    """
    1. Iterate over exp
    2. append operand directly to ans
    3. push operator in stack.
    4. if operator with less precedence found then remove higher precedence operator from stack and add to ans
    5. if closing bracket found pop all operators of brackets and add to ans
    6. Time Complexity: O(N+N)
    7. Space Complexity: O(N)
    """
    ans = ""
    stack = []

    for letter in exp:
        if (letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z') or (letter.isdigit()):
            ans += letter
        elif letter == '+' or letter == '-' or letter == '*' or letter == '/' or letter == '^':
            if not stack:
                stack.append(letter)
                continue
            
            while stack and getPrecedence(letter) <= getPrecedence(stack[-1]):
                ans += stack.pop()
            stack.append(letter)
        else:
            if letter == '(':
                stack.append(letter)
            else:
                while stack and stack[-1] != '(':
                    ans += stack.pop()
                stack.pop()

    while stack:
        ans += stack.pop()
    return ans

exp = "a+b*(c^d-e)^(f+g*h)-i"
print(InfixtoPostfix(exp))


"""
exp = "(p+q)*(m-n)"

i      stack      ans

(       (
p       (        p
+       (+       p
q       (+       pq
)                pq+
*        *       pq+
(        *(      pq+
m        *(      pq+m
-        *(-     pq+m
n        *(-     pq+mn
)        *(-)    pq+mn-

         *       pq+mn-*
"""