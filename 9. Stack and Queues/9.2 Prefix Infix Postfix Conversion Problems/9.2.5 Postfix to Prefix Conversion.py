"""
Q. You are given a string that represents the postfix form of a valid mathematical expression.
   Convert it to its prefix form.


Example 1:

Input: 
ABC/-AK/L-*
Output: 
*-A/BC-/AKL
Explanation: 
The above output is its valid prefix form.

Example 2:

Input: 
ab+
Output: 
+ab
Explanation: 
The above output is its valid prefix form.
"""


def postfixToPrefix(s):
    """
    1. if operand push to stack
    2. if operator pop 2 elements do -AB and insert back to stack
    3. Time Complexity: O(N)
    4. Space Complexity: O(N)
    """
    stack = []
    for letter in s:
        if (letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z') or (letter.isdigit()):
            stack.append(letter)
        else:
            second = stack.pop()
            first = stack.pop()
            stack.append(f'{letter}{first}{second}')
    return stack[0]

s = "AB-DE+F*/"
print(postfixToPrefix(s))

"""
s = "AB-DE+F*/"

i              stack
A              A
B              AB
-              -AB
D              -AB, D
E              -AB, D, E
+              -AB, +DE
F              -AB, +DE, F
*              -AB, *+DEF
/              /-AB*+DEF

"""
