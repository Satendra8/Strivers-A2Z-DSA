"""
Q. In the Tower of Hanoi puzzle, you are given n disks stacked in ascending order (smallest at the top) on the first of three rods. The goal is to move all disks to the third rod following two rules: only one disk can be moved at a time, and a disk can only be placed on top of a larger disk. Given the number of disks n and three rods labeled as from, to, and aux (starting rod, target rod, and auxiliary rod, respectively),  returns the total number of moves needed to transfer all disks from the starting rod to the target rod.

Examples:

Input: n = 2
Output: 3
Explanation: For n =2 , steps will be as follows in the example and total 3 steps will be taken.
move disk 1 from rod 1 to rod 2
move disk 2 from rod 1 to rod 3
move disk 1 from rod 2 to rod 3
Input: n = 3
Output: 7
Explanation: For N=3 , steps will be as follows in the example and total 7 steps will be taken.
move disk 1 from rod 1 to rod 3
move disk 2 from rod 1 to rod 2
move disk 1 from rod 3 to rod 2
move disk 3 from rod 1 to rod 3
move disk 1 from rod 2 to rod 1
move disk 2 from rod 2 to rod 3
move disk 1 from rod 1 to rod 3
Input: n = 0
Output: 0
Explanation: Total 0 steps will be taken.
"""

def towerOfHanoi(n, fromm, to, aux):
    """
    1. Hypothesis: move n-1 plates to aux
    2. Base case: if single plate then move directly to destination
    3. Induction: move last plate at destination, then move rest of the plate from aux to destination
    """
    if n == 1:
        print(f"move disk {n} from rod {fromm} to rod {to}")
        return
    towerOfHanoi(n-1, fromm, aux, to)
    print(f"move disk {n} from rod {fromm} to rod {to}")
    towerOfHanoi(n-1, aux, to, fromm)
    return

n = 2
towerOfHanoi(n, 1, 3, 2)