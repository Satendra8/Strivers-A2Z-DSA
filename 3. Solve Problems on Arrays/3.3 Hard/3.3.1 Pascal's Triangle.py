"""
Q. Program to generate Pascal's Triangle

Problem Statement: This problem has 3 variations. They are stated below:

Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal's triangle.

Variation 2: Given the row number n. Print the n-th row of Pascal's triangle.

Variation 3: Given the number of rows n. Print the first n rows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown in the figure below:
"""

def pascalVariation1(r, c):
    """
    Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal's triangle.
    1. Formula nCr =     n!
                      ----------
                      r! * (n-r)!
    2. By Observation
        4C2 =  4x3x2x1     4x3
              ---------- = ---   (the above part go till the below part)
               2x1 x 2x1   2x1

    Time Complexity: O(r)     
    Space Complexity: O(1)
    """
    ans = 1

    for i in range(c):
        ans = ans * (r-i)
        ans = ans // (i+1)
    return ans


def pascalVariation2(r):
    """
    Variation 2: Given the row number n. Print the n-th row of Pascal's triangle.
    1. Using the variation 1 and geneate pascal for all places in a row
    Time Complexity: O(r*c)
    Space Complexity: O(1)
    """
    for i in range(r+1):
        print(pascalVariation1(r, i), end=" ")



def pascalVariation2Optimized(r):
    """
    Variation 2: Given the row number n. Print the n-th row of Pascal's triangle.
    1. By Observation

        5C0       5C1       5C2       5C3       5C4       5C5

        1         5         5x4      5x4x3    5x4x3x2    5x4x3x2x1
                 ----      -----    -------  ---------  -----------
                  1         2x1      3x2x1    4x3x2x1    5x4x3x2x1

                                r-i
    Pattern is : prev = prex * -----
                                i+1
    """
    prev = 1
    print(prev, end=" ")
    for i in range(r):
        prev = prev * (r - i) // (i + 1)
        print(prev, end=" ")


def pascalVariation3(n):
    """
    Variation 3: Given the number of rows n. Print the first n rows of Pascal's triangle.
    1. use the above variation2 approach
    2. run for all rows
    Time Complexity: O(r*c)
    Space Complexity: O(1)
    """
    ans = []
    for i in range(0, n+1):
        prev = 1
        temp = [prev]
        for j in range(i):
            prev = prev * (i - j) // (j + 1)
            temp.append(prev)
        ans.append(temp)
    return ans
n = 4
print(pascalVariation3(n))