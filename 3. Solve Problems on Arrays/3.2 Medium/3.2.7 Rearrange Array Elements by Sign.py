"""
Q. There's an array 'A' of size 'N' with an equal number of positive and negative elements.
Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.

Note: Start the array with positive elements.

Example 1:

Input:
arr[] = {1,2,-4,-5}, N = 4
Output:
1 -4 2 -5

Explanation: 

Positive elements = 1,2
Negative elements = -4,-5
To maintain relative ordering, 1 must occur before 2, and -4 must occur before -5.

Example 2:
Input:
arr[] = {1,2,-3,-1,-2,-3}, N = 6
Output:
1 -3 2 -1 3 -2
Explanation: 

Positive elements = 1,2,3
Negative elements = -3,-1,-2
To maintain relative ordering, 1 must occur before 2, and 2 must occur before 3.
Also, -3 should come before -1, and -1 should come before -2.

"""





def rearrange_array_striver(arr):
    """
    1. Strivers approach
    2. Works when positive and negative are equal
    3. take 2 arrays pos and neg and store postive and negative elements
    4. insert positive on even index and negative on odd index

    Time Complexity: O(N) + O(N) = 2N
    Space Complexity: O(N)

    """
    n = len(arr)
    
    pos = []
    neg = []
    
    for i in arr:
        if i>0:
            pos.append(i)
        else:
            neg.append(i)
    for i in range(n//2):
        arr[i*2] = pos[i]
        arr[i*2+1] = neg[i]
    return arr
    
arr = [1,2,-4,-5]
print(rearrange_array_striver(arr))


def rearrange_array_optimized(arr):
    """
    1. Optimized Approach
    2. works when positive and negative are equal
    3. take 2 pointers pos and neg for tracking and increment them by 2
    4. take a new array and insert positive and negative element and return
    5. this is just reducing on extra loop

    Time Complexity: O(N)
    Space Complexity: O(N)

    """
    n = len(arr)
    new_arr = [0]*n
    pos = 0
    neg = 1
    
    for i in arr:
        if i>0:
            new_arr[pos] = i
            pos += 2
        else:
            new_arr[neg] = i
            neg += 2
    return new_arr
       
arr = [1,2,-3,-1,-2,3]
print(rearrange_array_optimized(arr))



def rearrange_array(arr):
    """
    Brute Force
    1. Work even if postive and negative numbers are not same
    2. take 2 arrays pos and neg and store postive and negative elements
    3. insert positive on even index and negative on odd index

    Time Complexity: O(N) + O(N) = 2N
    Space Complexity: O(N)
    
    """
    n = len(arr)
    
    all_pos = []
    all_neg = []
    
    for i in arr:
        if i>0:
            all_pos.append(i)
        else:
            all_neg.append(i)
    
    pos = len(all_pos)
    neg = len(all_neg)
    i = 0
    j = 0
    arr = []
    flag = True
    while i<pos and j<neg:
        print("i=>", i)
        if flag:
            arr.append(all_pos[i])
            i += 1
        else:
            arr.append(all_neg[j])
            j += 1
        flag = not flag

   
    for k in range(i, pos):
        arr.append(all_pos[k])
    
    for k in range(j, neg):
        arr.append(all_neg[k])
        
    return arr
       
arr = [1,2,-3,-1,-2,-3]
print(rearrange_array(arr))