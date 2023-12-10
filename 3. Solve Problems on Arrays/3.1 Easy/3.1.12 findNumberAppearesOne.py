"""
Q. Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

Example 1:
Input Format: arr[] = {2,2,1}
Result: 1
Explanation: In this array, only the element 1 appear once and so it is the answer.

Example 2:
Input Format: arr[] = {4,1,2,1,2}
Result: 4
Explanation: In this array, only element 4 appear once and the other elements appear twice. So, 4 is the answer.

"""
def findNumberAppearsOneBrute(nums):
    """
    Count number of each element.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in nums:
        if nums.count(i) == 1:
            return i
    return -1



def findNumberAppearsOneUsingDict(nums):
    """
    Use Dict
    Time Complexity: O(n)
    Space Complexity: O(n)

    """
    
    n = len(nums)
    nums.sort()
    print(nums)
    d = {}

    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for key, value in d.items():
        if value == 1:
            return key

    return -1



def findNumberAppearsOneBetter(nums):
    """
    Sort the array
    Time Complexity: O(n)
    Space Complexity: O(1)

    """
    
    n = len(nums)
    nums.sort()
    print(nums)

    for i in range(1, n, 2):
        if nums[i-1] != nums[i]:
            return nums[i-1]
    if n==2:
        return -1
    return nums[n-1]



def findNumberAppearsOneOptimal(nums):
    """
    Using XOR
    Time Complexity: O(n)
    Space Complexity: O(1)

    """
    XOR = 0
    
    for i in nums:
        XOR = XOR ^ i
    
    return XOR

arr = [4,1,2,1,2]
print(findNumberAppearsOneOptimal(arr))