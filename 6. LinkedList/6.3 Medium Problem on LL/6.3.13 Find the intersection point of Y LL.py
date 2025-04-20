"""
Q. Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

Example 1:
Input:
List 1 = [1,3,1,2,4], List 2 = [3,2,4]
Output:
2
Explanation: Here, both lists intersecting nodes start from node 2.

Example 2:
Input:
 List1 = [1,2,7], List 2 = [2,8,1]
Output:
 Null
Explanation: Here, both lists do not intersect and thus no intersection node is present.

"""

class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


def printLL(head):
    mover = head
    while(mover):
        print(mover.data, end=" ")
        mover = mover.next
    print()


def countLL(head):
    temp = head
    counter = 0

    while(temp):
        counter += 1
        temp = temp.next
    return counter


def ArrayToDLL(arr):
    head = Node(arr[0])
    earlier = head

    for i in range(1, len(arr)):
        curr = Node(arr[i], earlier)
        earlier.next = curr
        earlier = curr
    return head


def findIntersection(head1, head2):
    """
    1. Brute Force Approach
    2. use set and insert element of head1
    3. now check if any node matches in head2
    4. Time Complexity: O(N+M)
    5. Space Complexity: O(N)
    """
    temp1 = head1
    temp2 = head2

    s = set()
    while(temp1):
        s.add(temp1)
        temp1 = temp1.next

    while(temp2):
        if temp2 in s:
            return temp2.data
        temp2 = temp2.next
    return None


def findIntersectionBetter(head1, head2):
    """
    1. Better Approach
    2. count lenght of both linked list
    3. move the larger linked list head to count1 - count2 steps
    4. move now both the node are at same distance from last node
    5. both both node 1 step and if match return that node
    6. Time Complexity: O(N+M)
    7. Space Complexity: O(1)
    """
    count1 = countLL(head1)
    count2 = countLL(head2)
    temp1 = head1
    temp2 = head2

    #move head 
    if count1 > count2:
        steps = count1 - count2
        while(steps):
            steps -= 1
            temp1 = temp1.next
    else:
        steps = count2 - count1
        while(steps):
            steps -= 1
            temp2 = temp2.next

    while(temp1 and temp2):
        if temp1 == temp2:
            return temp1.data
        temp1 = temp1.next
        temp2 = temp2.next
    return None



def findIntersectionOptimal(head1, head2):
    """
    1. Optimal Approach
    2. run the loop on both head simultaneously
    3. if head1 ends assign this pointer to head2
    4. if head2 ends assign this pointer to head1
    5. at this moment head with large length have skipped diffence of count of node
    6. now move pointers 1 step each and return matching
    7. Time Complexity: O(N+M)
    8. Space Complexity: O(1)
    """
    if head1 is None or head2 is None:
        return None
    temp1 = head1
    temp2 = head2

    #at second iteration temp1 and temp2 both will point to null hence loop will be breaked
    while temp1 != temp2:
        temp1 = temp1.next if temp1 else head2
        temp2 = temp2.next if temp2 else head1

    return temp1

arr1 = [1,3,1,2,4]
arr2 = [3,2,4]
head1 = ArrayToDLL(arr1)
head2 = ArrayToDLL(arr2)
# head2.next.next.next = head1.next.next
printLL(head2)
print(findIntersectionOptimal(head1, head2).data)



"""
Best Approach

arr1 = 1->3->1->2->4
arr2 = 3->2->1->2->4

common is 1


1. run the loop on both head simultaneously
2. if head1 ends assign this pointer to head2
3. if head2 ends assign this pointer to head1
4. at this moment head with large length have skipped diffence of count of node
5. now move pointers 1 step each and return matching


"""

def intersection(head1, head2):
    temp1 = head1
    temp2 = head2

    while temp1 and temp2:
        temp1 = temp1.next
        temp2 = temp2.next

    new1 = head1
    new2 = head2
    while temp1:
        new1 = new1.next
        temp1 = temp1.next
    while temp2:
        new2 = new2.next
        temp2 = temp2.next

    while new1 and new2:
        if new1 == new2:
            return new1.data
        new1 = new1.next
        new2 = new2.next
    return None