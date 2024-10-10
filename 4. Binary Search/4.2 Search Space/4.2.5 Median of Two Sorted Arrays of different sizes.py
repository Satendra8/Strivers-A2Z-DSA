"""
Q. Given two sorted arrays arr1 and arr2 of size m and n respectively, return the median of the two sorted arrays. The median is defined as the middle value of a sorted list of numbers. In case the length of the list is even, the median is the average of the two middle elements.

Example 1:
Input Format:
 n1 = 3, arr1[] = {2,4,6}, n2 = 3, arr2[] = {1,3,5}
Result:
 3.5
Explanation:
 The array after merging 'a' and 'b' will be { 1, 2, 3, 4, 5, 6 }. As the length of the merged list is even, the median is the average of the two middle elements. Here two medians are 3 and 4. So the median will be the average of 3 and 4, which is 3.5.

Example 2:
Input Format:
 n1 = 3, arr1[] = {2,4,6}, n2 = 2, arr2[] = {1,3}
Result:
 3
Explanation:
 The array after merging 'a' and 'b' will be { 1, 2, 3, 4, 6 }. The median is simply 3.
"""

def findMedianSortedArrays(nums1, nums2):
    """
    1. Brute Force Approach
    2. add array
    3. sort the array
    4. if len is odd return mid element
    5. if even return average of mid and mid-1 element
    6. Time Complexity: O(m+n log(m+n))
    7. Space Complexity: O(m+n)
    """
    new_array = nums1 + nums2
    new_array.sort()
    n = len(new_array)

    mid = n//2
    if n % 2 == 1:
        return new_array[mid]
    else:
        print(new_array, mid)
        return (new_array[mid] + new_array[mid-1]) / 2



def findMedianSortedArrays(nums1, nums2):
    """
    1. Brute Force Approach
    2. take an empty array
    3. take two pointers and fill the array in sorted order
    4. if len is odd return mid element
    5. if even return average of mid and mid-1 element
    6. Time Complexity: O(m+n)
    7. Space Complexity: O(m+n)
    """
    new_array = []
    m = len(nums1)
    n = len(nums2)
    i=0
    j=0

    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            new_array.append(nums1[i])
            i += 1
        else:
            new_array.append(nums2[j])
            j += 1
    while i < m:
        new_array.append(nums1[i])
        i += 1

    while j < n:
        new_array.append(nums2[j])
        j += 1
    new_array_length = len(new_array)
    mid = new_array_length//2
    if new_array_length % 2 == 1:
        return new_array[mid]
    else:
        return (new_array[mid] + new_array[mid-1]) / 2


nums1 = [1,2]
nums2 = [3,4]
print(findMedianSortedArrays(nums1, nums2))



nums1 = [1,2]
nums2 = [3,4]
print(findMedianSortedArrays(nums1, nums2))


def findMedianSortedArrays(nums1, nums2):
    """
    1. Better Approach
    2. take index1 and index2, element1 and element2 instead whole array
    3. if index matches update then update elements
    4. if array lenght is odd return element1 only
    5. else return element1+element2 / 2
    6. Time Complexity: O(m+n)
    7. Space Complexity: O(1)
    """
    m = len(nums1)
    n = len(nums2)
    i=0
    j=0
    new_array_length = m + n
    ind1 = new_array_length // 2
    ind2 = ind1 - 1
    elem1 = -1
    elem2 = -1
    count = 0

    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            if count == ind1:
                elem1 = nums1[i]
            if count == ind2:
                elem2 = nums1[i]
            i += 1
        else:
            if count == ind1:
                elem1 = nums2[j]
            if count == ind2:
                elem2 = nums2[j]
            j += 1
        count += 1
    while i < m:
        if count == ind1:
                elem1 = nums1[i]
        if count == ind2:
            elem2 = nums1[i]
        i += 1
        count += 1
    while j < n:
        if count == ind1:
                elem1 = nums2[j]
        if count == ind2:
                elem2 = nums2[j]
        j += 1
        count += 1
    print(elem1, elem2)

    if new_array_length % 2 == 1:
        return elem1
    else:
        return (elem1+elem2)/2.0


nums1 = [1]
nums2 = [2,4]
print(findMedianSortedArrays(nums1, nums2))

"""
arr1 = [2,4,6]

arr2 = [1,3,5]

[1,2,3,4,5,6]

i=2
j=3

ind1 = 3
ind2 = 2

elem1 = 4
elem2 = 3

count = 5

"""