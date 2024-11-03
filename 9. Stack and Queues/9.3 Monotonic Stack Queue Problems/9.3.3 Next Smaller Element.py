"""
Q. Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

Input 1:
    A = [4, 5, 2, 10, 8]
Output 1:
    G = [-1, 4, -1, 2, 2]
Explaination 1:
    index 1: No element less than 4 in left of 4, G[1] = -1
    index 2: A[1] is only element less than A[2], G[2] = A[1]
    index 3: No element less than 2 in left of 2, G[3] = -1
    index 4: A[3] is nearest element which is less than A[4], G[4] = A[3]
    index 4: A[3] is nearest element which is less than A[5], G[5] = A[3]
    
Input 2:
    A = [3, 2, 1]
Output 2:
    [-1, -1, -1]
Explaination 2:
    index 1: No element less than 3 in left of 3, G[1] = -1
    index 2: No element less than 2 in left of 2, G[2] = -1
    index 3: No element less than 1 in left of 1, G[3] = -1
"""

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