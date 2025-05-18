import math

def pow(x, n):
    ans = 1
    while n > 1:
        if n%2 == 0:
            x = x * x
            n = n // 2
        else:
            ans = ans * x
            n = n-1
    ans = ans * x
    return ans

x = 2
n = 3
print(pow(x, n))