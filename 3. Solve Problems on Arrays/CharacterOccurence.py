"""
    1. Least repeating character in string
	2. Count of any particular element
	3. Count all occurence of all element
	4. Maximun repeating element
"""

def leastRepeatingCharacter(string):
    """
    Time Complexity - O(n)
    Space Complexity - O(1)
    """
    
    d = {}
    for i in string:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    
    return min(d, key=d.get)


def maximumRepeatingCharacter(string):
    """
    Time Complexity - O(n)
    Space Complexity - O(1)
    """
    
    d = {}
    for i in string:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    
    return max(d, key=d.get)


def countAllOccurences(string):
    """
    Time Complexity - O(n)
    Space Complexity - O(1)
    """
    
    d = {}
    for i in string:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    
    return d