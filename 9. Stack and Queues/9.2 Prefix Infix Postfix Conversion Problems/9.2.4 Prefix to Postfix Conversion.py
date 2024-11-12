"""
Q. You are given a string that represents the prefix form of a valid mathematical expression.
   Convert it to its postfix form.

Example:

Input: 
*-A/BC-/AKL
Output: 
ABC/-AK/L-*
Explanation: 
The above output is its valid postfix form.
"""

def prefixToPostfix(pre_exp):
    """
    1. iterate from last
    2. push operand in stack
    3. for operator, pop 2 elements AB+
    4. Time Complexity: O(N)
    5. Space Complexity: O(N)
    """
    stack = []

    for i in range(len(pre_exp)-1, -1, -1):
        if (pre_exp[i] >= 'a' and pre_exp[i] <= 'z') or (pre_exp[i] >= 'A' and pre_exp[i] <= 'Z') or (pre_exp[i].isdigit()):
            stack.append(pre_exp[i])
        else:
            first = stack.pop()
            second= stack.pop()
            stack.append(f'{first}{second}{pre_exp[i]}')
    return stack[0]

s = "/-AB*+DEF"
print(prefixToPostfix(s))

"""
s = "/-AB*+DEF"

i                stack
F                F
E                F, E
D                F, E, D
+                F, DE+
*                DE+F*
B                DE+F*, B
A                DE+F*, B, A
-                DE+F*, AB-
/                AB-DE+F*/


"""