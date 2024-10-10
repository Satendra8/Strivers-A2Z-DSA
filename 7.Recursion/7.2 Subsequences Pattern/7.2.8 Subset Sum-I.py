def subsetSum(arr, index, ans, n, l):
    """
    1. base case: if index exceeds add it to the ans (ans is at leaf node)
    2. pick and add it to ans
    3. not pick
    4. Time Complexity: O(2^n)
    5. Space Complexity: O(2^n)
    """
    if index >= n:
        l.append(ans)
        return

    #pick
    subsetSum(arr, index+1, ans+arr[index], n, l)
    #not pick
    subsetSum(arr, index+1, ans, n, l)
    return

arr = [1,2,1]
n = 3
l = []
subsetSum(arr, 0, 0, n, l)
print(l)
