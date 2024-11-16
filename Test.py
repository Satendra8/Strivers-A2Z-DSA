def characterReplacement(s, k):
    """
    Brute Force
    1. Generate all possible substr
    2. keep storing the frequency
    3. if substr exceeds k (validate k by length of substr - max frequency) break
    4. if substr below k keep updating maxx
    Time Complexity: O(N^2)
    Space Complexity: O(26)
    """
    n = len(s)
    maxx = 0

    for i in range(n):
        d = [0]*26
        for j in range(i, n):
            d[ord(s[j]) - 65] += 1
            maxl = max(d)
            if j - i + 1 - maxl <= k:
                maxx = max(maxx, j - i + 1)
            else:
                break
    return maxx


def characterReplacementBetter(s, k):
    n = len(s)
    maxx = 0
    left = 0
    d = [0]*26

    for right in range(n):
        d[ord(s[right]) - 65] += 1

        while right - left + 1 - max(d) > k:
            d[ord(s[left]) - 65] -= 1
            left += 1
        maxx = max(maxx, right - left + 1) 
    return maxx



def characterReplacementOptimal(s, k):
    """
    Optimal Approach
    There is no need to traverse over frequency array
    There is no need to update move left multiple steps, keep the window size at max and expand if better length found
    1. use pointer with sliding window
    2. keep storing the frequency
    3. if substr exceeds k (validate k by length of substr - max frequency) move the window
    4. if substr below k keep updating maxx
    Time Complexity: O(N)
    Space Complexity: O(26)
    """
    n = len(s)
    maxx = 0
    left = 0
    d = [0]*26
    max_freq = 0

    for right in range(n):
        d[ord(s[right]) - 65] += 1
        max_freq = max(max_freq, d[ord(s[right]) - 65])
        if right - left + 1 - max_freq > k:
            d[ord(s[left]) - 65] -= 1
            left += 1
        if right - left + 1 - max(d) <= k:
            maxx = max(maxx, right - left + 1) 
    return maxx


s = "ABABCCC"
k = 0
print(characterReplacementOptimal(s, k))


"""  0123456
s = "ABABCCC"
need count of max element
dict = {a:2, b:1} (max(d.values()))

   A  B  C
d [1, 1, 3]

n = 7
maxx = 5
i = 2
j = 6

"""