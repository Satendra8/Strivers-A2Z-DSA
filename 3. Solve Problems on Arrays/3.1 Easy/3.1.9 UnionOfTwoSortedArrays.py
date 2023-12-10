"""
Q. Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

Example 1:
Input:
n = 5,m = 5.
arr1[] = {1,2,3,4,5}  
arr2[] = {2,3,4,4,5}
Output:
 {1,2,3,4,5}

Explanation: 
Common Elements in arr1 and arr2  are:  2,3,4,5
Distnict Elements in arr1 are : 1
Distnict Elemennts in arr2 are : No distinct elements.
Union of arr1 and arr2 is {1,2,3,4,5} 

Example 2:
Input:
n = 10,m = 7.
arr1[] = {1,2,3,4,5,6,7,8,9,10}
arr2[] = {2,3,4,4,5,11,12}
Output: {1,2,3,4,5,6,7,8,9,10,11,12}
Explanation: 
Common Elements in arr1 and arr2  are:  2,3,4,5
Distnict Elements in arr1 are : 1,6,7,8,9,10
Distnict Elemennts in arr2 are : 11,12
Union of arr1 and arr2 is {1,2,3,4,5,6,7,8,9,10,11,12} 

"""

def unioun(arr1, arr2):
    """
    Time Complexity: O(m+n) // converting arr to set takes O(n), performing union is O(m+n)
    Space Complexity: O(m+n)
    """
    arr1 = list(set(arr1).union(set(arr2)))
    
    return arr1


def uniounOptimized(arr1, arr2):
    """
    Time Complexity: O(m+n)
    Space Complexity: O(m+n)
    """
    
    n = len(arr1)
    m = len(arr2)
    i=j=0
    temp = []
    prev = None
    
    while i<n or j<m:
        
        if j==m:
            if prev != arr1[i]:
                temp.append(arr1[i])
                prev = arr1[i]
            i += 1
        elif i==n:
            if prev != arr2[j]:
                temp.append(arr2[j])
                prev = arr2[j]
            j += 1
        
        elif arr1[i] < arr2[j]:
            if prev != arr1[i]:
                temp.append(arr1[i])
                prev = arr1[i]
            i += 1
        elif arr1[i] > arr2[j]:
            if prev != arr2[j]:
                temp.append(arr2[j])
                prev = arr2[j]
            j += 1
        else:
            if prev != arr1[i]:
                if prev != arr1[i]:
                    temp.append(arr1[i])
                    prev = arr1[i]
            i += 1
            j += 1
    return temp
    
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]



def uniounStriver(arr1, arr2):
    """
    Time Complexity: O(m+n)
    Space Complexity: O(m+n)
    """
    
    n = len(arr1)
    m = len(arr2)
    i=j=0
    temp = []
    prev = None
    
    while i<n and j<m:
        
        if arr1[i] < arr2[j]:
            if prev != arr1[i]:
                temp.append(arr1[i])
                prev = arr1[i]
            i += 1
        elif arr1[i] > arr2[j]:
            if prev != arr2[j]:
                temp.append(arr2[j])
                prev = arr2[j]
            j += 1
        else:
            if prev != arr1[i]:
                if prev != arr1[i]:
                    temp.append(arr1[i])
                    prev = arr1[i]
            i += 1
            j += 1
            
    # for remaining arr[i]
    while i < n:
        if prev != arr1[i]:
            temp.append(arr1[i])
            prev = arr1[i]
        i += 1
        
    # for remaining arr[j]
    while j < m:
        if prev != arr2[j]:
            temp.append(arr2[j])
            prev = arr2[j]
        j += 1

    return temp
    
arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 5]
    
print(uniounOptimized(arr1, arr2))