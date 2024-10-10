"""
Q. Compress string (Eg: aabbccddeeee O/P a2b2c2d2e4)

"""

def compress(string):
    n = len(string)
    count = 1
    prev = string[0]
    ans = ""
    
    for i in range(1, n):
        if prev == string[i]:
            count += 1
        else:
            ans += prev + str(count)
            count = 1

        prev = string[i]
    
    ans += prev + str(count)
    return ans

print(compress("aabbccdfe"))