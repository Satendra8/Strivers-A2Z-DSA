d = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}

def letter(s, index, ans, n, l):
    """
    1. base case: when index exceeds n (ans present at leaf node)
    2.             "23"
                /    |    \
            2,a     2,b    2,c
                            / |  \
        /   |  \    / |  \ 3,cd 3,ce 3,cf
                 3,bd 3,be 3,bf
    3,ad 3,ae 3,af

    3. call for each letter of number
    4. Time Complexity: 3^n (n is lenght of digits)
    5. space complexity: i * 3^n (average length of ans)    
    """
    if index >= n:
        #handle empty string case
        if ans:
            l.append(ans)
        return

    for char in d[s[index]]:
        letter(s, index+1, ans+char, n, l)
    
    return

s = "234"
n = len(s)
l = []
letter(s, 0, "", n, l)
print(l)
