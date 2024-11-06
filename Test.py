def asteroidCollision(asteroids):
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