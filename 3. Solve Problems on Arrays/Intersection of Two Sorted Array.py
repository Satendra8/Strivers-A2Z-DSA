"""
Q. Find Intersection Of Two Sorted Arrays.

Example 1:
Input:
n = 6,m = 4.
arr1[] = {1, 2, 2, 2, 3, 4}  
arr2[] = {2, 2, 3, 3}
Output:
 {2, 2, 3}

Example 2:
Input:
n = 3,m = 3.
arr1[] = {1, 4, 5}  
arr2[] = {3, 4, 5}
Output:
 {4, 5}

"""



def intersection(arr1, arr2):
    """
    1. Brute Force Approach
    2. loop over arr1
    3. loop over arr2, match the element and keep track of a visited elements
    4. if elements matched and element is not visited yet
    5. append that in final list
    6. Time Complexity - O(N*M)
    7. Space Complexity - O(max(N,M)) and O(N+M) for returning output
    
    
    """
    n = len(arr1)
    m = len(arr2)
    i=j=0
    
    visited = [0]*m
    final_list = []
    
    for i in arr1:
        
        for j in range(m):
            if(arr1[i]==arr2[j] and visited[j]==0):
                final_list.append(arr1[i])
                visited[j] = 1
                break
    return final_list
    
arr1 = [1, 2, 2, 2, 3, 4]
arr2 = [2, 2, 3, 3]

print(intersection(arr1, arr2))



def intersection(arr1, arr2):
    """
    1. Optimal Approach
    2. Use 2 pointer approach
    3. use while loop till minimum of array
    4. if arr1 element is smaller, keep moving i pointer
    5. if arr1 element is greater, keep moving j pointer
    6. if equal store and move both i and j pointer
    7. Time Complexity - O(N)
    8. Space Complexity - O(1), O(max(M,N)) just for storing and returning output
    """
    n = len(arr1)
    m = len(arr2)
    i=j=0
    final_list= []
    while(i<n and j<m):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            final_list.append(arr1[i])
            i += 1
            j += 1

    return final_list
    
arr1 = [1, 4, 5]
arr2 = [3, 4, 5]

print(intersection(arr1, arr2))