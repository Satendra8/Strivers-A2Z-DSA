"""
Q. You are given a string str of lowercase alphabates and an integer k.
Your task is to return the count all the possible substrings that have exactly 'k' distinct characters.


Sample Input 1 :
aacfssa    
3
Sample Output 1 :
5
Explanation of The Sample Input 1:
Given 'str' = “aacfssa”. We can see that the substrings with only 3 distinct characters are {aacf, acf, cfs, cfss, fssa}. 

Therefore, the answer will be 5.
Sample Input 2 :
qffds
4
Sample Output 2 :
1

"""




def countSubStrings(s: str, k: int) -> int:
    """
    1. Brute Force Approach
    2. find out all possible sunstring
    3. get and check lenght of all unique words in substring
    4. if length matches, increment the counter
    5. Time Complexity - O(N^3)
    6. Space Complexity - O(1)
    """
    n = len(s)
    i = 0
    counter = 0
    for i in range(n):
        for j in range(i+1, n+1):
            substr = s[i:j]
            new_set = set()
            for elem in substr:
                new_set.add(elem)
            if len(new_set) == k:
                counter += 1
    return counter


def countSubStrings(s: str, k: int) -> int:
    """
    1. Better Approach
    2. Genereate all substrings and keep storing in set.
    3. if count matches increment counter, if reaches break (no need to move forward always get greater length)
    4. Time Complexity - O(N^2)
    5. Space Complexity - O(1) - (not more than 26 - only lowercase characters)
    """
    n = len(s)
    counter = 0
    for i in range(n):
        set1 = set()
        for j in range(i, n):
            set1.add(s[j])
            if(len(set1) == k):
                counter += 1
            elif len(set1) > k:
                break
    return counter


def countSubStrings(s: str, k: int) -> int:
    """
    1. Other's Code
    2. Using  list and ASCII insted set
    3. if distinct chaeacters found increase count
    4. if count of distinct characters reaches k increment result
    4. Time Complexity - O(N^2)
    5. Space Complexity - O(1) - (not more than 26 - only lowercase characters)
    
    """
    n = len(s)
    RESULT = 0
    for i in range(n):
        COUNT = [0]*26
        DISTINCT_CHARS = 0
        for j in range(i, n):
            if COUNT[97 - ord(s[j])] == 0:
                DISTINCT_CHARS  += 1
            COUNT[97 - ord(s[j])] += 1
            
            if DISTINCT_CHARS == k:
                RESULT += 1
    return RESULT



def Kdistinct(s, k):
    """
    1. Optimal Approach
    2. Using Two Pointer Approch (Aquire and Release Method)
    3. Problem is brocken down into 2 parts
        a. Find all distinct substring whose lenght is atmost k
        b. Find all distinct substring whose lenght is atmost k-1
        then subtract a - b = (distinct substring whose length = k)
    4. Iterate till n, keep inserting element and their fequency in dict
    5. keep adding substring count => i-j+1
    6. if lenght of dict reaches k (Release => decrese frequency, remove key, increase left pointer)
    7. Time Complexity - O(N)
    8. Space Complexity - O(1) - (not more than 26 - only lowercase characters)
    """
    ans = 0
    d = {}
    n = len(s)
    i=j=0

    while i < n:
        if s[i] in d:
            d[s[i]] += 1
        else: 
            d[s[i]] = 1

        while(len(d) > k):
            d[s[j]] -= 1

            if d[s[j]] == 0:
                del d[s[j]]
            j += 1
        ans += (i-j+1)
        i += 1
    return ans

s = "aacfssa"
k = 3
final_ans = Kdistinct(s, k) - Kdistinct(s, k-1)
print(final_ans)