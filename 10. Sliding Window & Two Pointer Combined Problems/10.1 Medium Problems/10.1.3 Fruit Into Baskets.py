"""
Q. You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array of arr[], where arr[i]  is the type of fruit the ith tree produces.
You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow :

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of the baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array of fruits, return the maximum number of fruits you can pick.

Examples:

Input: arr[]= [2, 1, 2]
Output: 3
Explanation: We can pick one fruit from all three trees. Please note that the type of fruits is same in the 1st and 3rd baskets.
Input: arr[] = [3, 1, 2, 2, 2, 2]
Output: 5
Explanation: It's optimal to pick from the last 5 trees. Please note that we do not pick the first basket as we would have to stop at thrid tree which would result in only 2 fruits collected.

"""

def totalFruits(arr):
    """
    Brute Force Approach
    1. generate all possible sub array having k <= 2
    2. keep updating the max
    Time Complexity: O(N^2)
    Space Complexity: O(3)
    """
    n = len(arr)
    maxx = 0
    for i in range(n):
        s = set()
        k = 0
        for j in range(i, n):
            if arr[j] not in s:
                k += 1
            if k > 2:
                break
            s.add(arr[j])
            maxx = max(maxx, j - i + 1)
    return maxx




def totalFruitsBetter(arr):
    """
    Better Approach
    1. use two pointer with sliding window
    2. keep track of number and frequency
    3. use set, if size of set becomes > 2 keep moving left pointer
    4. and decrease frequency, if frequency become 0 remove the number
    5. keep updating maxx
    Time Complexity: O(2N)
    Space Complexity: O(3) // max 3 elements at a time
    """
    n = len(arr)
    maxx = 0
    left = 0
    d = {}

    for right in range(n):
        if arr[right] in d:
            d[arr[right]] += 1
        else:
            d[arr[right]] = 1
        
        while len(d) > 2:
            d[arr[left]] -= 1
            if d[arr[left]] == 0:
                d.pop(arr[left])
            left += 1
        maxx = max(maxx, right - left + 1)
    return maxx


def totalFruitsOptimal(arr):
    """
    Optimal Approach
    1. use two pointer and sliding window
    2. maitain a dict having number and frequency
    3. if len exceeds 2 move left pointer
    4. if frequency reduced to 0 delete key
    5. update maxx only if len of dict <= 2
    Time Complexity: O(N)
    Space Complexity: O(3)
    """
    n = len(arr)
    maxx = 0
    left = 0
    d = {}

    for right in range(n):
        if arr[right] in d:
            d[arr[right]] += 1
        else:
            d[arr[right]] = 1

        if len(d) > 2:
            d[arr[left]] -= 1
            if d[arr[left]] == 0:
                d.pop(arr[left])
            left += 1
        if len(d) <= 2:
            maxx = max(maxx, right - left + 1)
    return maxx

arr =  [3,3,3,1,2,1,1,2,3,3,4]
print(totalFruitsOptimal(arr))


"""    0 1 2 3 4 5 6 7 8 9 10
arr = [3,3,3,1,2,1,1,2,3,3,4]

left=8
right=9
maxx=5
d = {3:2, 4:1}


Dry Run Optimal Approach
       0 1 2 3 4 5 6 7 8 9 10
arr = [3,3,3,1,2,1,1,2,3,3,4]

left=5
right=10
maxx=5
d = {1:1,2:1,3:1, 4:1 }



"""