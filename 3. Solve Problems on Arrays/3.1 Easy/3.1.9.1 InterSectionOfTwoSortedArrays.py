"""
Q. Find the intersection of two sorted arrays. OR in other words, Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example 1:
Input: 
A: [1 2 3 3 4 5 6]
, B: [3 3 5]
Output: 3,3,5
Explanation: We are given two arrays A and B. 
The elements present in both the arrays  
are 3,3 and 5.

Example 2:
Input: 
A: [1 2 3 3 4 5 6]
, B: [3 5]
Output: 3,5
Explanation: We are given two arrays A and B. 
The elements present in both the arrays are 3 and 5.

"""

def intersection_of_two_sorted_array(arr1, arr2):
    M = len(arr1)
    N = len(arr2)
    new_array = []

    i=j=0

    while i<M and j<N:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            new_array.append(arr2[j])
            i += 1
            j += 1
    print(new_array)

arr1 = [1, 2, 3, 3, 4, 5, 6]
arr2 = [3, 5]
intersection_of_two_sorted_array(arr1, arr2)

#TODO post on leetcode