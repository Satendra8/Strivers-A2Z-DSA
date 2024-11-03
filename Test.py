def prevSmallerBrute(arr):
    n = len(arr)
    ans = []

    for i in range(n-1, -1, -1):
        not_found = True

        for j in range(i-1, -1, -1):
            if arr[i] > arr[j]:
                not_found = False
                ans.append(arr[j])
                break
        if not_found:
            ans.append(-1)
    return ans[::-1]


def prevSmaller(arr):
    stack = []
    ans = []

    for num in arr:
        if not stack:
            ans.append(-1)
        else:
            if num > stack[-1]:
                ans.append(stack[-1])
            else:
                while stack and num <= stack[-1]:
                    stack.pop()
                if stack:
                    ans.append(stack[-1])
                else:
                    ans.append(-1)
        stack.append(num)
    return ans
arr = [4, 5, 2, 10, 8]
print(prevSmaller(arr))