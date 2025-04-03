def getFloor(arr, x):
    floor = -1
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == x:
            return arr[mid]
        elif arr[mid] > x:
            end = mid - 1
        else:
            floor = arr[mid]
            start = mid + 1
    return floor


def getCeil(arr, x):
    ceil = -1
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == x:
            return arr[mid]
        elif arr[mid] > x:
            ceil = arr[mid]
            end = mid - 1
        else:
            start = mid + 1
    return ceil


def getFloorAndCeil(arr, x):
    """
    Binary Search
    1. if arr[mid] == k, floor and ceil is same
    2. if arr[mid] > k, move left, store ceil (possible ans)
    3. if arr[mid] < k, move right, store floor (possible ans)
    Time Complexity: O(logN)
    Space Complexity: O(1)
    """
    return (getFloor(arr, x), getCeil(arr, x))


x = 28 
arr = [80, 59, 26, 46]
print(getFloor(arr, x))