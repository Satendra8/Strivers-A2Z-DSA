"""
Q. Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.

Example 2:

Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.

Example 3:

Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.
"""

def assign(root, row, col, ans):
    if not root:
        return
    if col in ans:
        if row in ans[col]:
            temp_arr = ans[col][row]
            temp_arr.append(root.val)
            temp_arr.sort()
            ans[col][row] = temp_arr
        else:
            ans[col][row] = [root.val]
    else:
        ans[col] = {row: [root.val]}

    assign(root.left, row+1, col-1, ans)
    assign(root.right, row+1, col+1, ans)

def verticalTraversal(root):
    """
    Better Approach
    1. calculate vertical for each node using preorder or other left = (row + 1, col - 1), right = (row + 1, col + 1)
    2. key inseting in dict in this format {col: {row: val}}
    3. sort dict by outer key
    4. sort dict by inner key
    5. flatten inner val and add it to final ans
    Time Complexity: O(NlogN) + O(NlogN + MlogM)) + O(N)
                    calculate    for sorting dict   flatten arr
                    vertical     both key, val are
                                    independent
    Space Complexity: O(N) + O(N) +     log(N)
                      dict   final_ans  temp arr
    """
    ans = {}
    assign(root, 0, 0, ans)
    final_ans = []
    print(ans)
    for key, val in sorted(ans.items()):
        temp = []
        for inner_key, inner_val in sorted(val.items()):
            temp.extend(inner_val)
        final_ans.append(temp)
    return final_ans
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(10)
root.right.left = Node(9)
root.right.right = Node(10)
root.left.left.right = Node(5)
root.left.left.right.right = Node(6)

print(verticalTraversal(root))
