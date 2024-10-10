"""
Q. Given a string, find all the possible subsequences of the string.


Examples:

Example 1:
Input: str = "abc"
Output: a ab abc ac b bc c
Explanation: Printing all the 7 subsequence for the string "abc".

Example 2:
Input: str = "aa"
Output: a a aa 
Explanation: Printing all the 3 subsequences for the string "aa"

"""



def subsets(s, ans):
    """
    1. base case: s is empty print ans (ans is present at leaf node)
    2. make choice for s[0], append in ans
    3. make choice for s[0], don't use
    """

    if s == '':
        print(ans)
        return

    subsets(s[1:], ans+s[0])
    subsets(s[1:], ans)
    return


def subsetLeetcode(nums, index, n, ans, finalAns):
    """
    1. base case: if index exceeds n then print ans (ans is present at leaf node)
    2. make choice for s[inedx], don't use
    3. make choice for s[index], append in ans
    """
    if index >= n:
        finalAns.append(ans)
        return
    subsetLeetcode(nums, index+1, n, ans, finalAns)
    subsetLeetcode(nums, index+1, n, ans + [nums[index]], finalAns)
    return




nums = [1,2,3]
n = len(nums)
finalAns = []
subsetLeetcode(nums, 0, n, [], finalAns)
print(finalAns)
