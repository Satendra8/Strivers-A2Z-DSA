def postfixToInfix(s):
    """
    1. for operand push in stack
    2. for operator pop 2 elements then do (A+B) and push back to stack
    3. Time Complexity: O(N)
    4. Space Complexity: O(N)
    """
    stack = []
    for l in s:
        if (l >= 'a' and l <= 'z') or (l >= 'A' and l <= 'Z') or (l.isdigit()):
            stack.append(l)
        else:
            second = stack.pop()
            first = stack.pop()
            stack.append(f'({first}{l}{second})')
    return stack[0]

s = "AB-DE+F*/"
print(postfixToInfix(s))

"""
s = "AB-DE+F*/"

i               stack
A               A
B               AB
-               (A-B)
D               (A-B), D
E               (A-B), DE
+               (A-B), (D+E)
F               (A-B), (D+E), F
*               (A-B), ((D+E)*F)
/               ((A-B)/((D+E)*F))
"""