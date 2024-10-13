def checkPalindrom(s, first, last):
    if first > last:
        return True
    if s[first] != s[last]:
        return False
    
    return checkPalindrom(s, first+1, last-1)


def partition(s, index, ans, l, n):
    """
    1. base case: if index exceeds, appnend in ans
    2. loop over index to n partition furthur if is substr is palindrom
    3. substr is starting from index to i+1
    4. Time Complexity: O(n^n), n is lenght of string
    5. Space Complexity: O(n^n)
    """
    if index >= n:
        l.append(ans)
        return

    for i in range(index, n):
        substr = s[index:i+1]
        if checkPalindrom(substr, 0, len(substr)-1):
            partition(s, i+1, ans+[substr], l, n)
    return

s = "aab"
n = len(s)
l = []
partition(s, 0, [], l, n)
print(l)