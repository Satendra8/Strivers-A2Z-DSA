"""
Q.  Given an array of size n, sort the array using Merge Sort.

Example 1:
Input: N=5, arr[]={4,2,1,6,7}
Output: 1,2,4,6,7,


Example 2:
Input: N=7,arr[]={3,2,8,5,1,4,23}
Output: 1,2,3,4,5,8,23
"""

def merge(arr, left, mid, right):
    """
    1. assume two array left -> mid and mid+1 -> right
    2. compare both and put the smallest element in temp array
    3. assign back the temp element into array
    """
    lstart = left
    lend = mid

    rstart = mid+1
    rend = right

    temp = []
    while lstart <= lend and rstart <= rend:
        if arr[lstart] <= arr[rstart]:
            temp.append(arr[lstart])
            lstart += 1
        else:
            temp.append(arr[rstart])
            rstart += 1

    while lstart <= lend:
        temp.append(arr[lstart])
        lstart += 1
    
    while rstart <= rend:
        temp.append(arr[rstart])
        rstart += 1

    arr[left:right+1] = temp


def divide(arr, left, right):
    """
    1. divide the array in two parts
    2. left -> mid
    3. mid+1 -> right
    4. merge array
    """
    mid = (left+right) // 2
    if left >= right:
        return
    divide(arr, left, mid)
    divide(arr, mid+1, right)
    merge(arr, left, mid, right)


arr = [4,2,1,6,7]
divide(arr, 0, 4)
print(arr)
