def totalFruits(arr):
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
    Space Complexity: O(1)
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