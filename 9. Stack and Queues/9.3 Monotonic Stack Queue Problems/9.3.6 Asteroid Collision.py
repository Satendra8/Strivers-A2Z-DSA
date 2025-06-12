"""
Q. We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
"""

def asteroidCollision(asteroids):
    """
    Imagine +ve asteroids are moving to --> and -ve moving to <--
    1. iterate till n
    2. if positive element found push in stack
    3. if negative element found keep poping (if -ve element is greater)
    4. if equal element found then also pop
    5. edge case: if there is no element or top element of stack is negative push in stack
    6. Time Complexity: O(N+N)
    6. Space Complexity: O(N)
    """
    n = len(asteroids)

    stack = []

    for i in range(n):
        if asteroids[i] > 0:
            stack.append(asteroids[i])
        else:
            while stack and stack[-1] > 0 and abs(asteroids[i]) > stack[-1]:
                stack.pop()
            if stack and abs(asteroids[i]) == stack[-1]:
                stack.pop()
            elif not stack or stack[-1] < 0:
                stack.append(asteroids[i])
    return stack

asteroids = [-2,-2,1,-2]
print(asteroidCollision(asteroids))