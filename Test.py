def singleNumber(nums):
    """
    1. Use XOR operator
    2. same number will be cancelled, unique will remain
    3. Time Complexity: O(N)
    4. Space Complexity: O(1)
    """
    ans = 0
    for i in nums:
        ans = ans ^ i
    return ans

nums = [2,2,1]
print(singleNumber(nums))