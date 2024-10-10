"""
Q. Given an array of N integers. Every number in the array except one appears twice. Find the single number in the array.


Example 1:
Input Format:
 arr[] = {1,1,2,2,3,3,4,5,5,6,6}
Result:
 4
Explanation:
 Only the number 4 appears once in the array.

Example 2:
Input Format:
 arr[] = {1,1,3,5,5}
Result:
 3
Explanation:
 Only the number 3 appears once in the array.
"""


def search_single_element(nums):
    """
    1. Brute force approach
    2. use dict to store frequency
    3. return number with frequency 1
    4. Time Complexity: O(N)
    5. Space Complexity: O(N)    
    """
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



nums = [1,1,2,3,3,4,4,8,8]
print(search_single_element(nums))



def search_single_element(nums):
    """
    1. Brute force approach
    2. make -1 if two same number found
    3. Time Complexity: O(N)
    4. Space Complexity: O(N)    
    """
    single = -1

    for i in nums:
        if i == single:
            single = -1
        elif single == -1:
            single = i
    return single


nums = [1,1,3,5,5]
print(search_single_element(nums))



def search_single_element(nums):
    """
    1. Brute force approach
    2. use XOR operator
    3. Time Complexity: O(N)
    4. Space Complexity: O(N)    
    """
    XOR = 0
    for i in nums:
        XOR = XOR ^ i
    return XOR


nums = [1,1,2,2,3,3,4,5,5,6,6]
print(search_single_element(nums))


def search_single_element(nums):
    """
    1. Optimal Approach
    2. seperately check if array has single element
    3. seperately check for first index to avoid multiple edge cases
    4. seperately check for last index to avoid multiple edge cases
    5. check if prev current and next are not same
    6. (even, odd) to trim left -> if index is odd previous should be same or if index is even next should be same
    7. (odd, even) to trim right -> if index is odd next should be same or if index is even prev should be same
    8. Time Complexity: O(logN)
    9. Space Complexity: O(1)
    """
    n = len(nums)

    left = 0
    right = n - 1

    if n == 1:
        return nums[0]
    if nums[0] != nums[1]:
        return nums[0]
    if nums[n-1] != nums[n-2]:
        return nums[n-1]
    left = 1
    right = n - 2


    while left <= right:
        mid = (left+right) // 2
        #check if prev current and next are not same
        if nums[mid] != nums[mid-1] and nums[mid+1] != nums[mid]:
            return nums[mid]
        #(even, odd) to trim left -> if index is odd previous should be same or if index is even next should be same
        if (mid%2 == 1 and nums[mid] == nums[mid-1]) or (mid%2 == 0 and nums[mid] == nums[mid+1]):
            left = mid + 1
        #(odd, even) to trim right -> if index is odd next should be same or if index is even prev should be same
        elif (mid%2 == 1 and nums[mid] == nums[mid+1]) or (mid%2 == 0 and nums[mid] == nums[mid-1]):
            right = mid - 1
    

nums = [1,1,2,3,3,4,4,5,5,6,6] 
print(search_single_element(nums))


"""
Trim Left Half Example

        0 1 2 3 4 5 6 7 8 9 10
nums = [1,1,2,2,3,3,4,5,5,6,6]  left=1, right=9, mid=5
                                left=6, right=9, mid=7
                                left=6, right=6, mid=6
  0 1 2 3 4 5 6 7 8
 [1,1,2,2,3,3,4,5,5]            left=1, right=7, mid=4
                                left=5, right=7, mid=6

(even, odd) index elements are same then single element is on right half
(odd, even) index elements are same then single element is on left half


1. seperately check if array has single element
2. seperately check for first index to avoid multiple edge cases
3. seperately check for last index to avoid multiple edge cases
4. check if prev current and next are not same
5. (even, odd) to trim left -> if index is odd previous should be same or if index is even next should be same
6. (odd, even) to trim right -> if index is odd next should be same or if index is even prev should be same


Trim Right Half Example

        0 1 2 3 4 5 6 7 8 9 10
nums = [1,1,2,3,3,4,4,5,5,6,6]    left=1, right=9, mid=5
                                  left=1, right=4, mid=2



 0 1 2 3 4 5 6 7 8
[1,1,2,3,3,4,4,5,5]        left=1, right=7, mid=4
                           left=1, right=3, mid=2

"""