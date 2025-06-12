def stockSpan(arr):
    n = len(arr)
    stack = []
    ans = []

    for i in range(n):
        if not stack:
            ans.append(i+1)
        elif arr[i] <= stack[-1][0]:
            ans.append(i - stack[-1][1])
        else:
            while stack and arr[i] > stack[-1][0]:
                stack.pop()
            if not stack:
                ans.append(i+1)
            else:
                ans.append(i - stack[-1][1])
        print(stack)
        stack.append((arr[i], i))
    return ans

arr = [120, 100, 60, 80, 90, 110, 115]
print(stockSpan(arr))